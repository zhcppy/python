import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RedirectHandler):
    def get(self):
        self.write("hello word")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()