from PIL import Image

from .text_functions import sym_left, sym_right
from .pic_functions import sym_right_img, sym_left_img, resize
from os import listdir
from os.path import join, abspath, splitext


def main():

    dir_path = './pics_originals/'
    save_path = './pics_flipped/'
    for f in listdir(dir_path):

        abs_path = abspath((join(dir_path, f)))
        fn, fext = splitext(f)
        i = Image.open(abs_path)
        i = resize(i)

        i.save(save_path+"{}_original{}".format(fn, fext))

        sym_l = sym_left_img(i)
        sym_l.save(save_path+"{}_{}{}".format(fn, sym_left(fn), fext))

        sym_r = sym_right_img(i)
        sym_r.save(save_path+"{}_{}{}".format(fn, sym_right(fn), fext))
        print(abs_path+" flipped")


if __name__ == "__main__":
    main()



