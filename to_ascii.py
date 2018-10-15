from PIL import Image
from tools import file_name_ignore_extension

ASCII_CHARS = ['@', '%', '#', '*', '+', '=', '-', '.', '.', ' ']
RGB_LENGTH = 255


# def main():
#     img_name = './test_jiang.jpg'
#     out_txt_name = file_name_ignore_extension(img_name) + '_in_ascii_compressed.txt'
#     init_img = Image.open(img_name)
#     width, height = init_img.size
#     height *= 0.5
#
#     scale_factor = 0.2
#     new_width, new_height = int(width * scale_factor), int(height * scale_factor)
#     scaled_img = rescale_img(init_img, new_width, new_height)
#
#     file_out(img_pixels_to_asciis(scaled_img), out_txt_name, new_width, new_height)


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


def file_out(ascii_list, file_name, width, height):
    f = open(file_name, 'w+')
    for h in range(0, height):
        f.write(''.join(ascii_list[h*width : h*width + width]) + '\n')


def file_name_ignore_extension(file_name):
    return file_name.rsplit('.', 1)[0]


if __name__ == '__main__':
    main()