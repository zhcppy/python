import tornado.ioloop
import tornado.web

"""
Tornado 是一个Python web框架和异步网络库，起初由 FriendFeed 开发. 
通过使用非阻塞网络I/O，Tornado可以支撑上万级的连接，处理长连接，WebSockets，和其他需要与每个用户保持长久连接的应用.
"""


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