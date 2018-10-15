from PIL import Image, ImageDraw
from to_ascii import *


def main():
    img_density_factor = 6

    img_name = './test_jiang.jpg'
    in_img = Image.open(img_name)
    width, height = in_img.size

    out_img = Image.new(mode='RGB',
                        size=(width * img_density_factor, height * img_density_factor),
                        color=(255, 255, 255))

    asciis_to_img(in_img, out_img, img_density_factor, width, height)

    out_img.save((file_name_ignore_extension(img_name) + '_in_ascii.jpg'))


def asciis_to_img(in_img, out_img, density, width, height):
    draw = ImageDraw.Draw(out_img)
    ascii_list = img_pixels_to_asciis(in_img)

    for h in range(0, height):
        for w in range(0, width):
            draw.text(xy=(w * density, h * density), text=''.join(ascii_list[h*width + w]), fill=(0, 0, 0))


if __name__ == '__main__':
    main()

