import tornado.ioloop
import tornado.web
from .middlewire import BaseHandler
import os

setting = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "login_url": "/login",
    "xsrf_cookies": True,
}

class MainHandler(BaseHandler):
    def initialize(self,a):
        print(a)

    def get(self):
        self.write({'msg':{'data':'hello world'}})

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler,dict(a='11')),
        (r'/static/*',tornado.web.StaticFileHandler,dict(path=setting['static_path']))
    ],**{'debug':True})

