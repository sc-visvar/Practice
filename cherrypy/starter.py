import cherrypy
import random
import string

class Helloworld(object):
    @cherrypy.expose
    def index(self):
        return 'Hello world!'
    
    @cherrypy.expose
    def generate(self, length=10):
        return ''.join(random.sample(string.hexdigits, int(length)))
    

if __name__ == "__main__":
    cherrypy.quickstart(Helloworld())
