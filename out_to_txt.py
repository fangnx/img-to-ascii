from to_ascii import *


def main():
    img_name = './test_jiang.jpg'
    out_txt_name = file_name_ignore_extension(img_name) + '_in_ascii_compressed.txt'
    init_img = Image.open(img_name)
    width, height = init_img.size
    height *= 0.5

    scale_factor = 0.2
    new_width, new_height = int(width * scale_factor), int(height * scale_factor)
    scaled_img = rescale_img(init_img, new_width, new_height)

    file_out(img_pixels_to_asciis(scaled_img), out_txt_name, new_width, new_height)