import web
from utils.util import Util

class UploadController:
    def getHandler(self,renderer):
        print "in uploader"
        return renderer.uploader(0,"Uploader")
        
    def postHandler(self,renderer):
        
        form = web.input(userfile=None,comment=None) 
        tempDir=Util.createDirForTempFiles()
        print ("temp dir created " + str(tempDir))
        
        try:
            filePath= Util.createTempFileWithData(tempDir,form.userfile)
            print("File Path is " + str(filePath))
            workBook=Util.openWorkBook(filePath)
            self.workBookToJson(workBook)
            
        except Exception, e:
            print "IN Excepetion"
            print str(e)
        finally:
            Util.deleteTempDir(tempDir)
            
        return renderer.uploader(0,"Uploader")
        
    def workBookToJson(self,workBook):
        
        for sheetName in workBook.sheet_names():
            # do code here
            print sheetName
            currSheet=workBook.sheet_by_name(sheetName)
            print "no of rows are " + str(currSheet.nrows)
            print "no of cols are " + str(currSheet.ncols)
            
            self.findTablesInSheet(currSheet)
            
            #===================================================================
            # if(currSheet.nrows > 0):
            #     #print a row
            #     currRow = currSheet.row(0)
            #     print currRow
            #     
            #     #print a cell
            #     if(currSheet.ncols > 0):
            #         # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
            #         cell_type = currSheet.cell_type(0, 0) # rownum,colnum
            #         cell_value = currSheet.cell_value(0, 0)
            #         
            #         print "cell type is " + str(cell_type)
            #         print "cell value is " + str(cell_value)
            #===================================================================
        return {}
    
    def findTablesInSheet(self,currSheet):
        for row_index in xrange(currSheet.nrows):
            for col_index in xrange(currSheet.ncols):
                print Util.cellUnicodeVal(currSheet, row_index, col_index)
