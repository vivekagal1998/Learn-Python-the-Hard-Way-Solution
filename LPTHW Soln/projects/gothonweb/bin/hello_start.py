import web

urls = (
    '/', 'hi', '/bye', 'bye', '/Python', 'Python'
)

app = web.application(urls, globals(), True)

class hi:
    """docstring for .
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg"""
    def GET(self):
        return """
        What the heck is
        this guys this is
        Vivek Shah and Welcome
        to my first Python tutorial"""

class Python:
    """docstring for
    def __init__(self, arg):
        super, self).__init__()
        self.arg = arg"""
    def GET(self):
        return "I am Currently Learning Python Web FrameWorks"


class bye:
    """docstring for
    def __init__(self, arg):
        super, self).__init__()
        self.arg = arg"""
    def GET(self):
        return "Bye Bye Web"

if __name__ == '__main__':
    app.run()
