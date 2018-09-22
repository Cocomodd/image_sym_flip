from PIL import Image


def resize(img):
    size300 = (500, 500)
    img.thumbnail(size300)
    return img


def sym_left_img(img):

    cropped = img.crop(box=(0, 0, img.width / 2, img.height))

    mirror = cropped.transpose(Image.FLIP_LEFT_RIGHT)
    combine = Image.new('RGB', (cropped.width * 2, cropped.height), 'white')
    combine.paste(cropped, (0, 0, cropped.width, cropped.height))
    combine.paste(mirror, (cropped.width, 0, cropped.width * 2, cropped.height))
    return combine


def sym_right_img(img):
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    return sym_left_img(img)

