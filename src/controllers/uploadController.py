


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
        return renderer.uploader(0,"Uploader")
        
    def postHandler(self,renderer):
        
        form = web.input(userfile={},comment=None)
        
        submittedFileName = str(form['userfile'].filename)
        
        if Util.getIndexOfStringInString(submittedFileName, ".csv", None):
            pass # do stuff with csv to xlsx
        
        tempDir=Util.createDirForTempFiles()
        result = "Success!"
        
        isError = 0
        
        try:
            
            filePath= Util.createTempFileWithData(tempDir,form['userfile'].value)
            
            workBook=Util.openWorkBook(filePath)
            result = Util.dictToJson(self.workBookToJson(workBook))
            fileName = None
            
            try:
                metaSheet=workBook.sheet_by_name(Rules.metaSheetName)
                fileName = Util.cellVal(metaSheet,0,1)
            except:
                None
                
            if(not fileName):
                fileName = "data.py"
            
            attachmentName =  'attachment; filename="%s" ' % (fileName)
            web.header('Content-type','application/octet-stream')
            web.header('Content-transfer-encoding','base64')
            web.header('Content-Disposition',attachmentName)
            
            return result
            
        except Exception, e:
            isError = 1
            print "IN Excepetion"
            Util.printStackTraceInConsole()
            result = "Failed %s " % str(e)
            print str("result it %s " % result)
        finally:
            Util.deleteTempDir(tempDir)
        
        return renderer.uploader(isError,result)
        
    def workBookToJson(self,workBook):
        
        totalDict = {}
        
        for sheetName in workBook.sheet_names():

            if sheetName == Rules.metaSheetName:
                continue
            # do code here
            currSheet=workBook.sheet_by_name(sheetName)
            
            tableStartCell = self.findTablesInSheet(currSheet)
            sheetDict = None
            
            if(tableStartCell):
                sheetDict = self.tableToDictionary(currSheet,tableStartCell.rowIndex, tableStartCell.colIndex)
            else:
                print "Warning skipping sheet %s " % sheetName
            
            if(sheetDict):
                totalDict[sheetName] = sheetDict 
            
        return totalDict
    
    def findTablesInSheet(self,currSheet):
        for row_index in xrange(currSheet.nrows):
            for col_index in xrange(currSheet.ncols):
                cellValue = Util.cellVal(currSheet, row_index, col_index)
                if cellValue == Rules.idColumnName: #means table is started (in case if sheet has multiple tables)
                    return MCell(rowIndex=row_index,colIndex=col_index)
                
        return None
                    
    def verifyTableKeyNames(self):
        None
    
    def extractField(self,aRawColumn):
        #verify field pattern first
        aRawColumn = aRawColumn.replace(" ","") # remove spaces for the column
        
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
            # don't throw exception just ignore the column
            #raise Exception("Column name  not valid " + str(aRawColumn))
            None
        
        return field
        
    
    def tableToDictionary(self,currSheet, rowIndex,colIndex):
        #returns a Cell having endColX and endColY
        
        dictColumns = {} # for checking duplicaton if column is duplicated throw exception
        arrColumns = [] # for making the json.
        cellValue = Util.cellVal(currSheet, rowIndex, colIndex) # initialize 
        
        while (colIndex < currSheet.ncols and cellValue != ""): # read the row till empty cell is found it is ok to put a condition on empty cell 
            cellValue = Util.cellVal(currSheet, rowIndex, colIndex)
            
            field = None
            
            if(cellValue == Rules.idColumnName):
                field = MField()
                field.fieldName = Rules.idColumnName
                field.fieldType = "int"
            else:
                field = self.extractField(cellValue)
                if(not field):
                    print "Sheet::%s   Warnning --- Ignore column '%s'" % (currSheet.name,cellValue)
                    colIndex = colIndex + 1
                    continue
                
            anyFieldAlready = Util.getDictValue(dictColumns, field.fieldName)
            
            if(anyFieldAlready):
                raise Exception("Sheet %s The filed %s is already available kindly rename it to something else for this sheet col=(%d) " % (currSheet.name, field.fieldName,colIndex ))
            
            dictColumns[field.fieldName] = field.fieldType
            arrColumns.append(field)
                
                #print "field name is %s and field type is %s " % (field.fieldName,str(field.fieldType)) 
            colIndex = colIndex + 1
            
        mainDataDict = {}
        dataDict = mainDataDict[Rules.dataName] = {}
        
        for row_index in xrange(currSheet.nrows): 
            col = 0
            if(row_index==0):#skip the first row
                continue
            
            try:
                idKeyValue = long(float(Util.cellVal(currSheet, row_index, col))) # pick the 0th column value
            except Exception , e:
                raise Exception("Exception %s while working with Sheet ('%s')  Row_No=%i and Col=%i -------- Celll_Value =%s " % (str(e), currSheet.name,row_index, col, str(Util.cellVal(currSheet, row_index, col))))
                
            currRow = dataDict[str(idKeyValue)] = {}
            for column in arrColumns:
                cellValue = Util.cellVal(currSheet, row_index, col)
                try:
                    cellValue = Util.getCastedValue(cellValue,column.fieldType)
                except Exception , e:
                    print (str(e))
                    print "exception in sheet %s in row =%i col=%i " % (currSheet.name,row_index,col)
                    raise Exception("exception %s  %s sheet in row =%i col=%i " % (str(e), currSheet.name,row_index,col))
                
                if(cellValue):
                    currRow[column.fieldName] = cellValue 
                
                col = col + 1
        
        jsonForKey = Util.dictToJson(dataDict)
        key = Util.getSh1OfStr(jsonForKey)
        # do encryption here once done with other work
        
        mainDataDict[Rules.keyName] = key 
            
        return mainDataDict
            
            
        # add all the columns in dict 
                
