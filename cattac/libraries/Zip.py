import zipfile
import io
from PIL import Image
from flip.text_functions import sym_left, sym_right
from flip.pic_functions import sym_right_img, sym_left_img, resize


class Zip:
    LEFT_PREFIX = "l_"
    RIGHT_PREFIX = "r_"
    ORIGINAL_PREFIX = "o_"

    def __init__(self, image, name):
        self.image = image
        self.name = name

    def get_name(self):
        name_l = self.LEFT_PREFIX+sym_left(self.name)
        name_r = self.RIGHT_PREFIX+sym_right(self.name)

        return [self.ORIGINAL_PREFIX+self.name, name_l, name_r]

    def get_images(self):
        i = Image.open(self.image.file)

        imgs = [
            resize(i),
            sym_left_img(i),
            sym_right_img(i)
        ]

        return imgs

    def get_zip(self):
        i_names = self.get_name()

        zip_buffer = io.BytesIO()
        zip_file = zipfile.ZipFile(zip_buffer, "w")

        for i, img in enumerate(self.get_images()):
            buffer = io.BytesIO()
            img.save(buffer, format="jpeg")
            zip_file.writestr(i_names[i] + ".jpg", buffer.getvalue())

        zip_file.close()

        return zip_buffer.getvalue()
