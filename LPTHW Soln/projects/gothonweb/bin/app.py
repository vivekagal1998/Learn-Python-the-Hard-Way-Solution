import web

url = (
    '/', 'index'
)

app = web.application(url, globals())
#greet="Hello World"
class index:
    """docstring for
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg
        """
    def GET(self):
        greet = "Hello World"
        return greet

if __name__ == '__main__':
    app.run()
