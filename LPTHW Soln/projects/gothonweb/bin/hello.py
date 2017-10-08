import web

urls = (
  '/', 'hello',
  '/bye', 'bye')

app = web.application(urls, globals(), autoreload=True)

render = web.template.render('/media/vivek/Coding Stuffs/LPTHW Soln/projects/gothonweb/bin/templates', base='base')

class hello(object):
    def GET(self):
        return render.hello("Templates demo", "hello", "A long time ago...")

class bye(object):
    def GET(self):
        return render.bye("Templates demo", "Bye", "14", "8", "25", "42", "19")

if __name__ == "__main__":
    app.run()
