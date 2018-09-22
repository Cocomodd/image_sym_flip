import cherrypy, zipfile, io
from PIL import Image
from flip.pic_functions import sym_right_img, sym_left_img, resize


class Cattac(object):
    @cherrypy.expose
    def cattac(self, image, name):
        i = Image.open(image.file)

        i_names = ["o", "l", "r"]

        imgs = [
            resize(i),
            sym_left_img(i),
            sym_right_img(i)
        ]

        zip_buffer = io.BytesIO()
        zip_file = zipfile.ZipFile(zip_buffer, "w")

        for i, img in enumerate(imgs):
            buffer = io.BytesIO()
            img.save(buffer, format="jpeg")
            zip_file.writestr(i_names[i]+".jpg", buffer.getvalue())

        zip_file.close()

        cherrypy.response.headers['Content-Type'] = "application/zip"
        cherrypy.response.headers['Content-Disposition'] = 'attachment; filename=test'

        return zip_buffer.getvalue()


cherrypy.quickstart(Cattac())
