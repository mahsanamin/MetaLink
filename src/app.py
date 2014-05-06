# coding: utf-8

#http://webpy.org/
#https://pypi.python.org/pypi/xlrd/0.9.2

import web
from mapper import Mapper
from controllers.uploadController import UploadController

class Index:
    def GET(self):
        return "Meta Link Version 1.0"
        

class Uploader:
    def GET(self):
        print "Uploader GET"
        controllerObj = UploadController()
        return controllerObj.getHandler(Mapper.render)
    def POST(self):
        print "Uploader POST"
        controllerObj = UploadController()
        return controllerObj.postHandler(Mapper.render)

class MyApp(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))
 
if __name__ == "__main__":
    app = MyApp(Mapper.urls, globals())
    app.run(port=9999)