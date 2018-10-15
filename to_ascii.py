from PIL import Image
from tools import file_name_ignore_extension


ASCII_CHARS = ['@', '%', '#', '*', '+', '=', '-', '.', '.', ' ']
RGB_LENGTH = 255


def rescale_img(img, new_width, new_height):
    return img.resize((new_width, new_height))


def assign_pixel_to_ascii(pixel):
    division = int(RGB_LENGTH / len(ASCII_CHARS))
    pixel_avg_rgb = int((pixel[0] + pixel[1] + pixel[2]) / 3)
    ascii_index = int(pixel_avg_rgb / division)
    if ascii_index == 10:
        ascii_index = 9
    return ASCII_CHARS[ascii_index]


def img_pixels_to_asciis(img):
    pixels_in_ascii = [assign_pixel_to_ascii(pixel) for pixel in list(img.getdata())]
    return pixels_in_ascii

