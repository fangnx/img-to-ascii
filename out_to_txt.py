from to_ascii import *


def main():
    img_name = './test_bao.jpeg'
    out_txt_name = file_name_ignore_extension(img_name) + '_in_ascii_compressed.txt'
    img = Image.open(img_name)
    width, height = img.size
    height *= 0.5

    scale_factor = 0.4
    new_width, new_height = int(width * scale_factor), int(height * scale_factor)
    scaled_img = rescale_img(img, new_width, new_height)

    txt_out(img_pixels_to_asciis(scaled_img), out_txt_name, new_width, new_height)


def txt_out(ascii_list, file_name, width, height):
    f = open(file_name, 'w+')
    for h in range(0, height):
        f.write(''.join(ascii_list[h*width : h*width + width]) + '\n')


if __name__ == '__main__':
    main()