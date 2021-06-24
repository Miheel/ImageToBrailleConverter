"""
converts an image to Braille unicode
"""

import image_manip as imgmanip
from PIL import Image
#import PIL.Image


def main():
    """main"""

    in_path = "ahegao.png"
    out_path = in_path.split('.')[0]

    try:
        image = Image.open(in_path)
    except FileNotFoundError as err:
        print(err)
        #print("Unable to find image ", path)

	#resize image
    #image = imgmanip.resize(image)

    #convert image to greyscale image
    greyscale_image = imgmanip.to_greyscale(image)

    # convert greyscale image to ascii characters
    #ascii_str = imgmanip.pixel_to_ascii(greyscale_image)
    ascii_str = imgmanip.pixle_to_braille(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""

    #Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width//2):
        ascii_img += ascii_str[i:i+img_width//2] + "\n"
    #print(ascii_img)

    #save the string to a file
    with open(out_path, "w", encoding='utf-8') as f:
        f.write(ascii_img)

if __name__ == '__main__':
    main()
