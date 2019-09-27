class Middleware(object):
    def __init__(self, wsgi_app, request, *args):
        self.wsgi_app = wsgi_app
        self.requst = request
        print("初始化...")

    def __call__(self, *args, **kwargs):
        print("开始...")
        ret = self.wsgi_app(*args, **kwargs)
        print(self.request)
        print("结束...")
        return ret


class PermissionMiddleware(Middleware):
    def __init__(self, name):
        super().__init__()
        self.name = name
