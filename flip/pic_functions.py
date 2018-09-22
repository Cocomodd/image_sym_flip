from PIL import Image


def resize(img):
    """
    Resize the given image to a thumbnail of 500px max
    :param img: Image
    :return: Image
    """
    size = (500, 500)
    img.thumbnail(size)
    return img


def sym_left_img(img):
    """
    Makes the given image symetrical along a vertical axis going through the center of the image
    Left side
    :param img: Image
    :return: Image
    """
    cropped = img.crop(box=(0, 0, img.width / 2, img.height))
    mirror = cropped.transpose(Image.FLIP_LEFT_RIGHT)
    combine = Image.new('RGB', (cropped.width * 2, cropped.height), 'white')
    combine.paste(cropped, (0, 0, cropped.width, cropped.height))
    combine.paste(mirror, (cropped.width, 0, cropped.width * 2, cropped.height))
    return combine


def sym_right_img(img):
    """
    Makes the given image symetrical along a vertical axis going through the center of the image
    Right side
    :param img: Image
    :return: Image
    """
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    return sym_left_img(img)

