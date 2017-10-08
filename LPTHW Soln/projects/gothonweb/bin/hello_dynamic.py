import web

urls = (
    '/hi', 'hi', '/(.*)', 'hello' 
)

app = web.application(urls, globals(), True)

class hello:
    """docstring for .
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg"""
    def GET(self, name):
        if name=='':
            name = 'Vivek'
        #i = web.input(name = 'Vivek Shah')
        return 'Hello, ' + web.websafe(name) + '!'


class hi:
    """docstring for
        super(, self).__init__()
        def __init__(self, arg):
        self.arg = arg"""
    def GET(self):
        return "HI"



if __name__ == '__main__':
    app.run()
