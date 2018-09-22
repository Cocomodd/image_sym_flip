def flip(string_to_flip):
    """
    Flips the given string
    :param string_to_flip:
    :return: string flipped
    """
    return string_to_flip[::-1]


def get_half_str(string_to_half):
    """
    Cuts the string in the middle and keeps the middle char if odd number
    :param string_to_half:
    :return: string halved
    """
    if len(string_to_half) % 2 == 0:
        return string_to_half[:len(string_to_half) // 2]
    else:
        return string_to_half[:len(string_to_half) // 2 + 1]


def sym_left(string_to_sym_left):
    """
    Returns symmetric string from left side
    :param string_to_sym_left:
    :return: symmetric string
    """
    half = get_half_str(string_to_sym_left)
    if len(string_to_sym_left) % 2 == 0:
        return half+flip(half)
    else:
        return half+flip(half[:-1])


def sym_right(string_to_sym_right):
    """
    Returns symmetric string from left side
    :param string_to_sym_right:
    :return: symmetric string
    """
    return sym_left(flip(string_to_sym_right))
