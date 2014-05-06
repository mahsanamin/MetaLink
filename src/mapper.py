import web

class Mapper():
    urls    = ( \
                '/','Index', \
                '/index','Index', \
                '/uploader','Uploader' \
               )
    render  = web.template.render('templates')