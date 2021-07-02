"""Converts an image to Braille unicode

Usage:
    Image2Braille (<srcimg>) [options] ((-a | --ASCII) | (-b | --braille))
    Image2Braille -h | --help
    Image2Braille -v | --version

Arguments:
    srcimg      source path to an image file to be converted.

Options:
    -h --help               display this help and exit.
    -v --version            output version information and exit.
    -o --output=<File>      write result to FILE instead of standard output.
    -r --resize=<size>      image size in pixles.
    -m --monospace          makes the out put monospaced.
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

def parse_img_str(img_width, img_str):
    img_str_len = len(img_str)
    img = ''

    #Split the string based on width of the image   
    for i in range(0, img_str_len, img_width):
        img += img_str[i:i+img_width] + '\n'

    return img

def main():
    """main"""

    args = docopt(__doc__, version='1.0.0')

    schema = Schema({
        '--help' : Use(bool),
        '--version' : Use(bool),
        '--resize' : Or(None, Use(int), error='New size must be an integer'),
        '--monospace' : Use(bool),
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
    monospace_flag = False

    #convert image to greyscale image
    greyscale_image = imgmanip.to_greyscale(image)

    if args['--resize']:
        print('Image is resized')
	    #resize image
        greyscale_image = imgmanip.resize(greyscale_image, args['--resize'])

    if args['--monospace']:
        print('Image is monospaced')
        monospace_flag = True

    if args['--ASCII']:
        print('image is ASCIIfied')
        ascii_str = imgmanip.pixle_to_ascii(greyscale_image)
        img_str = parse_img_str(greyscale_image.width, ascii_str)

    if args['--braille']:
        print('image is brailleified')
        braille_str = imgmanip.pixle_to_braille(greyscale_image, monospace_flag)
        img_str = parse_img_str(greyscale_image.width//2, braille_str)

    if args['--output']:
        print('Desination path', args['--output'])
        out_file_flag = True
    
    #Write the converted image to stdio or file
    write(args['--output'], out_file_flag, img_str)

if __name__ == '__main__':
    main()
