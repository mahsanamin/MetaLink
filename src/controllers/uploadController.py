


import web
from utils.util import Util
from rules import Rules

class MCell():
    rowIndex = -1,
    colIndex = -1
    
    def __init__(self,rowIndex,colIndex):
        self.rowIndex = rowIndex
        self.colIndex = colIndex

class MField():
    fieldName = None
    fieldType = "string"
    
class UploadController:
    def getHandler(self,renderer):
        print "in uploader"
        return renderer.uploader(0,"Uploader")
        
    def postHandler(self,renderer):
        
        web.header('Content-type','application/octet-stream')
        web.header('Content-transfer-encoding','base64') 
        
        form = web.input(userfile=None,comment=None) 
        tempDir=Util.createDirForTempFiles()
        result = "Success!"
        
        print ("temp dir created " + str(tempDir))
        
        try:
            filePath= Util.createTempFileWithData(tempDir,form.userfile)
            print("File Path is " + str(filePath))
            workBook=Util.openWorkBook(filePath)
            result = Util.dictToJson(self.workBookToJson(workBook))
            
            metaSheet=workBook.sheet_by_name(Rules.metaSheetName)
            fileName = Util.cellVal(metaSheet,0,1)
            if(not fileName):
                fileName = "data.py"
            
            attachmentName =  'attachment; filename="%s" ' % (fileName)
            web.header('Content-Disposition',attachmentName)
            
            
        except Exception, e:
            print "IN Excepetion"
            Util.printStackTraceInConsole()
            result = "Failed %s " % str(e)
            print str(e)
        finally:
            Util.deleteTempDir(tempDir)
        
        return result
        
        return renderer.uploader(0,result)
        
    def workBookToJson(self,workBook):
        
        totalDict = {}
        
        for sheetName in workBook.sheet_names():

            if sheetName == Rules.metaSheetName:
                continue
            # do code here
            currSheet=workBook.sheet_by_name(sheetName)
            print "sheet name is " + str(sheetName)
            print "no of rows are " + str(currSheet.nrows)
            print "no of cols are " + str(currSheet.ncols)
            
            tableStartCell = self.findTablesInSheet(currSheet)
            print "table cell is " + str(tableStartCell.colIndex)
            
            sheetDict = self.tableToDictionary(currSheet,tableStartCell.rowIndex, tableStartCell.colIndex)
            
            if(sheetDict):
                totalDict[sheetName] = sheetDict 
            
        return totalDict
    
    def findTablesInSheet(self,currSheet):
        for row_index in xrange(currSheet.nrows):
            for col_index in xrange(currSheet.ncols):
                cellValue = Util.cellVal(currSheet, row_index, col_index)
                print cellValue
                if cellValue == Rules.idColumnName: #means table is started (in case if sheet has multiple tables)
                    return MCell(rowIndex=row_index,colIndex=col_index)
                
        return None
                    
    def verifyTableKeyNames(self):
        None
    
    def extractField(self,aRawColumn):
        #verify field pattern first
        aRawColumn = aRawColumn.replace(" ","") # remove spaces for the column
        
        print (aRawColumn)
        columnStyleOk = Util.checkColumnNameStyle(aRawColumn)
        field = None
        if(columnStyleOk):
            pipeSignIndex = aRawColumn.index('|')
            firstBracketIndex = aRawColumn.index('(')

            columnName = aRawColumn[pipeSignIndex+1:firstBracketIndex]
            columnType = aRawColumn[firstBracketIndex+1:-1] 
            
            field = MField()
            field.fieldName = columnName
            field.fieldType = columnType
            
            isFieldTypeValid = Util.getDictValue(Rules.dataTypes, columnType, False)
            
            if not isFieldTypeValid:
                raise Exception ("Field type is not valid...")
            
        else:
            raise Exception("Column name  not valid " + str(aRawColumn))
        
        return field
        
    
    def tableToDictionary(self,currSheet, rowIndex,colIndex):
        #returns a Cell having endColX and endColY
        
        dictColumns = {} # for checking duplicaton if column is duplicated throw exception
        arrColumns = [] # for making the json.
        cellValue = Util.cellVal(currSheet, rowIndex, colIndex) # initialize 
        
        while (colIndex < currSheet.ncols and cellValue != ""): # read the row till empty cell is found it is ok to put a condition on empty cell 
            cellValue = Util.cellVal(currSheet, rowIndex, colIndex)
            
            field = None
            if(cellValue != Rules.idColumnName):
                field = self.extractField(cellValue)
                if(not field):
                    raise Exception ("something wrong with column %s " % (cellValue))
                
                anyFieldAlready = Util.getDictValue(dictColumns, field.fieldName)
                
                if(anyFieldAlready):
                    raise Exception("The filed %s is already available kindly rename it to something else for this sheet col=(%d) " % (field.fieldName,colIndex ))
                
                dictColumns[field.fieldName] = field.fieldType
                arrColumns.append(field)
                
                #print "field name is %s and field type is %s " % (field.fieldName,str(field.fieldType)) 
                    
            colIndex = colIndex + 1
            
        mainDataDict = {}
        for row_index in xrange(currSheet.nrows): 
            
            col = 0
            if(row_index==0):#skip the first row
                continue
            
            idKeyValue = long(float(Util.cellVal(currSheet, row_index, col))) # pick the 0th column value
            currRow = mainDataDict[str(idKeyValue)] = {}
            for column in arrColumns:
                cellValue = Util.cellVal(currSheet, row_index, col+1)
                
                cellValue = Util.getCastedValue(cellValue,column.fieldType)
                if(cellValue):
                    currRow[column.fieldName] = cellValue 
                col = col + 1
            
        return mainDataDict
            
            
        # add all the columns in dict 
                
