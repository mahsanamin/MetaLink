
import tempfile,json 
from time import gmtime, strftime
import logging
import msgpack
import gzip, zipfile
import hashlib
import os,sys
import time,datetime
import traceback
import shutil
import re
import xlrd
from matplotlib.pyplot import switch_backend

class Util():
    
    @staticmethod
    def getDictValue(aDict,aKey,aDefaultVal=None):
        if aDict.has_key(aKey):
            return aDict[aKey]
        else:
            aDefaultVal
        
    @staticmethod
    def isEmptySheet(aWorkBook,sheetName):
        aSheet=aWorkBook.sheet_by_name(sheetName)
        if int(aSheet.nrows) == 0:
            return True
        else:
            return False
        
    @staticmethod
    def openWorkBook(filePath):
        try:
            workBook = xlrd.open_workbook(filePath)
            
            return workBook
        except Exception:
            raise Exception("can not open work book at path " + str(filePath))
   
   
    @staticmethod
    def cellVal(currSheet,row_index,col_index):
        #supports unicoded
        try:
            cell_type = currSheet.cell_type(row_index, col_index) # rownum,colnum
            cell_value = currSheet.cell_value(row_index, col_index)
        
            if(cell_type == xlrd.XL_CELL_TEXT):
                return str(cell_value.encode("utf-8"))
        
            return str(cell_value)
        except:
            print "Exception while working with Row=%i and Col=%i -------- Cell_Type = %s and Celll_Value =%s " % (row_index, col_index, str(cell_type), str(cell_value))
        
    @staticmethod
    def checkColumnNameStyle(colName):
        #first check the column is custom or system
        #trim/strip the column from both side... i.e there should be no space
        colName = colName.strip()
        compiledRe = re.compile('(\w*)[|](\w+)[(][a-z]+[)]')
        returnVal = False
        if compiledRe.match(colName):
            returnVal = True
    
        return returnVal
        
    @staticmethod
    def createDirForTempFiles(subDirName = ""):
        return tempfile.mkdtemp( prefix="gbptmpDir_", dir="/tmp")
        
    @staticmethod
    def createDbFileName(fileDir):
        filePath = fileDir + "/" + "_dt.dat"
        return filePath
    
    @staticmethod
    def createTempFileWithData(fileDir,fileData,customName=None):
        if(customName):
            filePath = fileDir + "/" +customName
            dataFile = open(filePath,"w")
            dataFile.write(fileData)
            dataFile.close()
            return customName
        else:
            temp = tempfile.NamedTemporaryFile( prefix="temp_", dir=fileDir, delete=False)
            open(temp.name, 'wb').write(fileData)
            temp.close()
            return temp.name
    
    @staticmethod
    def deleteTempDir(filesDir):
        shutil.rmtree(path=filesDir)
    
    @staticmethod
    def dictToJson(finalDict):
        j = json.dumps(finalDict,separators=(',', ':'))
        return j 
    
    @staticmethod
    def getCurrentTime():
        return strftime("%Y-%m-%d %H:%M:%S", gmtime())
    
    @staticmethod
    def packTheDict(fileDict):
        packedDict = msgpack.packb(fileDict)
        return packedDict
    
    @staticmethod
    def unpackThePackedDict(packedDict):
        unpackedDict = msgpack.unpackb(packedDict)
        return unpackedDict
    
    @staticmethod
    def createTempFile(data):
        temp = tempfile.NamedTemporaryFile(delete=False)
        open(temp.name, 'wb').write(str(data))
    
        temp.close()
        return temp.name
    
    @staticmethod
    def gzipTheFile(sqliteFileName):
        zipFileName=sqliteFileName+".gz"
        
        existingFile = open(sqliteFileName, 'rb')
        newFile = gzip.open(zipFileName, 'wb')
        newFile.writelines(existingFile)
        newFile.close()
        existingFile.close()
        return newFile.name
    
    @staticmethod
    def zipTheFile(src,dst):
        path = "%s.zip" % (dst)
        zf = zipfile.ZipFile(path, "w")
        abs_src = os.path.abspath(src)
        for dirname, files in os.walk(src):
            for filename in files:
                absname = os.path.abspath(os.path.join(dirname, filename))
                arcname = absname[len(abs_src) + 1:]
                zf.write(absname, arcname)
        zf.close()
        return path
    
    
    @staticmethod
    def getSh1OfStr(aStr):
        sh1 = hashlib.sha1()
        sh1.update(str(aStr))
        return sh1.hexdigest()    

    @staticmethod
    def getCurrentEPOCHTime():
        currentTime = datetime.datetime.utcnow()
        stamp = time.mktime(currentTime.timetuple())
        return float(stamp) 
    
    @staticmethod
    def printStackTraceInConsole():
        exc_traceback = sys.exc_info()
        logging.info(str(exc_traceback))
        traceback.print_exc()
    
    @staticmethod
    def printExceptionInConsole(exception):
        Util.log("Exception is:" + str(exception))
        Util.printStackTraceInConsole()
    
    @staticmethod
    def encriptDecryptClientFile(clientFileData,salt):
        if len(clientFileData) > len(salt):
            count = (int(len(clientFileData) / len(salt))) +1
            salt =  salt * count
        result =  ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(clientFileData,salt))
        
        return result
    
    @staticmethod
    def getCastedValue(aValue,aTypeString):
        if not aValue or aValue == "":
            return None
        if aTypeString.lower() == "int" :
            return int(float(aValue))
        elif aTypeString.lower() == "float" :
            return float(aValue)
        elif aTypeString.lower() == "long" :
            return long(float(aValue))
        else:
            return aValue

    @staticmethod
    def getArrIndexForValue(arr,value,default_value=None):
        try:
            return arr.index(value)
        except ValueError:
            return default_value
        
        return default_value
    
    @staticmethod
    def getIndexOfStringInString(aSourceString,aSearchableString,aDefaultValue=None):
        try:
            return aSourceString.index(aSearchableString)
        except ValueError:
            return aDefaultValue
        
        return aDefaultValue
    
        