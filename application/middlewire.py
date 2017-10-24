from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    def write_error(self, status_code=500, **kwargs):
        print('something get wrong')


