import random
import string
import cherrypy

class Generator(object):
    @cherrypy.expose
    def index(self):
        return"""
            <html>
            <head> </head>
            <body>
                <form method="get" action="generate">
                    <input type="text" value="10" name="length" />
                    <button type="submit"> Let it rain! </button>
                </form>
            </body>
            </html"""
    
    @cherrypy.expose
    def generate(self, length=10):
        return ''.join(random.sample(string.hexdigits, int(length)))

if __name__ == "__main__":
    cherrypy.quickstart(Generator())
