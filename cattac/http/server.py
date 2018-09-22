import cherrypy
from cattac.lib.Zip import Zip


class Cattac(object):
    @cherrypy.expose
    def cattac(self, image, name):
        cherrypy.response.headers['Content-Type'] = "application/zip"
        cherrypy.response.headers['Content-Disposition'] = "attachment; "+name+".zip"

        return Zip(image, name).get_zip()


cherrypy.quickstart(Cattac())
