"""Converts an image to Braille unicode

Usage:
    Image2Braille (<srcimg>) [--output=<File>] [--resize=<size>] ((-a | --ASCII) | (-b | --braille))
    Image2Braille -h | --help
    Image2Braille -v | --version

Arguments:
    srcimg      source path to an image file to be converted.

Options:
    -h --help               display this help and exit.
    -v --version            output version information and exit.
    -o --output=<File>      write result to FILE instead of standard output.
    -r --resize=<size>      image size in pixles.
    -a --ASCII              Converts an image to ASCII.
    -b --braille            Converts an image to unicode braille.
"""

import image_manip as imgmanip
import os
from docopt import docopt
from PIL import Image
from schema import Schema, And, Or, Use, SchemaError

def write(file, file_bool, char_string):
    if file_bool:
        #save ascii image to file
        with open(file, 'w', encoding='utf-8') as f:
            f.write(char_string)
    else:
        #write ascii image to stdio   
        print(char_string)    

def parse_ascii_str(img_width, ascii_str):
    ascii_str_len = len(ascii_str)
    ascii_img = ''

    #Split the string based on width of the image   
    for i in range(0, ascii_str_len, img_width//2):
        ascii_img += ascii_str[i:i+img_width//2] + '\n'

    return ascii_img

def main():
    """main"""

    args = docopt(__doc__, version='1.0.0')

    schema = Schema({
        '--help' : Use(bool),
        '--version' : Use(bool),
        '--resize' : Or(None, Use(int), error='New size must be an integer'),
        '--ASCII' : Use(bool),
        '--braille' : Use(bool),
        '--output' : Or(None, Use(str)),
        '<srcimg>' : Use(Image.open, error='Image does not exist')
    })
    try:
        args = schema.validate(args)
    except SchemaError as e:
        print(e)
        exit(__doc__)

    image = args['<srcimg>']
    out_file_flag = False

    #convert image to greyscale image
    greyscale_image = imgmanip.to_greyscale(image)

    if args['--resize']:
        print('Image is resized')
	    #resize image
        greyscale_image = imgmanip.resize(greyscale_image, 100)

    if args['--ASCII']:
        print('image is ASCIIfied')
        ascii_str = imgmanip.pixel_to_ascii(greyscale_image)
    
    if args['--braille']:
        print('image is brailleified')
        ascii_str = imgmanip.pixle_to_braille(greyscale_image)

    if args['--output']:
        print('Desination path', args['--output'])
        out_file_flag = True
    
    ascii_img = parse_ascii_str(greyscale_image.width, ascii_str)

    #Write the converted image to stdio or file
    write(args['--output'], out_file_flag, ascii_img)

if __name__ == '__main__':
    main()
