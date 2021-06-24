"""
image manipulation and data extraction
"""

import math
import pixle_data as PD

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
pixle_OBJECT_LIST = []
pixle_HASH_LIST = []

def resize(image, new_width=200):
    """resizes image"""
    width, height = image.size
    new_height = math.floor(new_width * height / width)
    return image.resize((new_width, new_height))

def to_greyscale(image):
    """Converts image to grayscale"""
    return image.convert("L")

def index_exists(data, index):
    """Checks if an index in a list exists and returns element at the spesified position"""
    pixle = -1
    if index < len(data):
        pixle = data[index]

    return pixle

def extract_pixledata_matrix(image):
    """
	    extracts data from image in rows of thre
        and makes a 2x3 matrix of pixles.
    """
    pixles = list(image.getdata())
    img_width = image.width
    length = len(pixles)
    for i in range(0, length, img_width * 3):
        row1 = pixles[i:i + img_width]
        row2 = pixles[i + img_width:i + img_width * 2]
        row3 = pixles[i + img_width * 2:i + img_width * 3]


        for	j in range(0, len(row1), 2):
            pixle_OBJECT_LIST.append(PD.PixleDataMatrix(\
			index_exists(row1, j), index_exists(row2, j), index_exists(row3, j),\
			index_exists(row1, j + 1), index_exists(row2, j + 1), index_exists(row3, j + 1)))

def pixle_to_braille(image):
    """Converts a pixle matrix to braille unicode"""
    extract_pixledata_matrix(image)

    ascii_str = ""
    #i = 0
    for pixle_object in pixle_OBJECT_LIST:
        #print(i, end = ", ")

        pixle_object.set_braille_char()

        #print(str(i) + pixle_object.get_braille_bit_rep() + "," + pixle_object.get_braille_char())
        #print(str(i) + pixle_object.get_braille_char())
        # if len(pixle_object.braille_char) < 1:
            # print(i, end = "")
            # print(pixle_object.braille_char)
        # i = i + 1
        ascii_str += pixle_object.get_braille_char()

    return ascii_str


def pixle_to_ascii(image):
    """Converts a pixle matrix to ASCII_CHARS"""
    extract_pixledata_matrix(image)

    ascii_str = ""
    for pixle_object in pixle_OBJECT_LIST:
        pixle_HASH_LIST.append(pixle_object.calc_ascii(25))


    for i in range(0, len(pixle_HASH_LIST), image.width):
        for j in range(i, i + image.width):
            ascii_str += ASCII_CHARS[pixle_HASH_LIST[j][0]]
            ascii_str += ASCII_CHARS[pixle_HASH_LIST[j][1]]

        for j in range(i, i + image.width):
            ascii_str += ASCII_CHARS[pixle_HASH_LIST[j][2]]
            ascii_str += ASCII_CHARS[pixle_HASH_LIST[j][3]]

        for j in range(i, i + image.width):
            ascii_str += ASCII_CHARS[pixle_HASH_LIST[j][4]]
            ascii_str += ASCII_CHARS[pixle_HASH_LIST[j][5]]

    return ascii_str
