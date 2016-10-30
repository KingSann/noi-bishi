from tornado import httpserver,ioloop,web,gen,httpclient
from base_handler import BaseHandler
from tools import *
import bishi

class MainHandler(BaseHandler):
    def get(self):
        msg = self.get_argument('msg',None)
        self.render('index.html',msg=msg,page_title='XOJ',page_type='index')

class TestHandler(BaseHandler):

    def get(self):
        self.render('test.html',msg=None,page_title='测试页 -XOJ',page_type='test')
        

if __name__ == '__main__':

    settings={
        'cookie_secret': conf.COOKIESECRET,
        'template_path':'./templates',
        'static_path':'./static',
        'debug':True,
        'login_url':'/login',
        'xsrf_cookies':True,
    }

    application = web.Application(handlers=[

        (r'/',bishi.BishiHandler),

    ],**settings)

    application.listen(8080)
    ioloop.IOLoop.instance().start()
