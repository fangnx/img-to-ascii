from PIL import Image
from to_ascii import *


def main():
    img_name = './test_jiang.jpg'
    out_jpg_name = file_name_ignore_extension(img_name) + '_in_ascii.jpg'
    init_img = Image.open(img_name)
    width, height = init_img.size

    file_out(img_pixels_to_asciis(init_img), out_jpg_name, width, height)


def asciis_to_jpg(txt_file)：
        








if __name__ == '__main__':
    main()




