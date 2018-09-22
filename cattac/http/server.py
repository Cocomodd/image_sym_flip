import cherrypy
from cattac.http.config.config import config
from cattac.libraries.Zip import Zip


class Cattac(object):
    @cherrypy.expose
    def cattac(self, image, name):
        cherrypy.response.headers['Content-Type'] = "application/zip"
        cherrypy.response.headers['Content-Disposition'] = "attachment; "+name+".zip"

        return Zip(image, name).get_zip()


cherrypy.config.update(config())
cherrypy.quickstart(Cattac())
