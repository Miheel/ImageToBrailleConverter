"""A class to hold and manage a 2x3 pixle matrix"""

BRAILLE = [('000000', '⠀'), ('011101', '⠮'), ('000010', '⠐'), ('001111', '⠼'), ('110101', '⠫'),
           ('100101', '⠩'), ('111101', '⠯'), ('001000', '⠄'), ('111011', '⠷'), ('011111', '⠾'),
           ('100001', '⠡'), ('001101', '⠬'), ('000001', '⠠'), ('001001', '⠤'), ('000101', '⠨'),
           ('001100', '⠌'), ('001011', '⠴'), ('010000', '⠂'), ('011000', '⠆'), ('010010', '⠒'),
           ('010011', '⠲'), ('010001', '⠢'), ('011010', '⠖'), ('011011', '⠶'), ('011001', '⠦'),
           ('001010', '⠔'), ('100011', '⠱'), ('000011', '⠰'), ('110001', '⠣'), ('111111', '⠿'),
           ('001110', '⠜'), ('100111', '⠹'), ('000100', '⠈'), ('100000', '⠁'), ('110000', '⠃'),
           ('100100', '⠉'), ('100110', '⠙'), ('100010', '⠑'), ('110100', '⠋'), ('110110', '⠛'),
           ('110010', '⠓'), ('010100', '⠊'), ('010110', '⠚'), ('101000', '⠅'), ('111000', '⠇'),
           ('101100', '⠍'), ('101110', '⠝'), ('101010', '⠕'), ('111100', '⠏'), ('111110', '⠟'),
           ('111010', '⠗'), ('011100', '⠎'), ('011110', '⠞'), ('101001', '⠥'), ('111001', '⠧'),
           ('010111', '⠺'), ('101101', '⠭'), ('101111', '⠽'), ('101011', '⠵'), ('010101', '⠪'),
           ('110011', '⠳'), ('110111', '⠻'), ('000110', '⠘'), ('000111', '⠸')]

class PixleDataMatrix:
    """
    A class to represent a 2x3 pixel matrix

	Attributes
	----------
    braille_char : str
	    a unicode char representatino of a 2x3 matrix
	pixel_1 : int
        first pixel position upper left
	pixel_2 : int
        seconed pixel position middle left
	pixel_3 : int
        third pixel position lower left
	pixel_4 : int
        fourth pixel position upper right
	pixel_5 : int
        fifth pixel position middle right
	pixel_6 : int
        sixth pixel position lower right

	"""
    braille_char = "⠀"

    def __init__(self, pixel_1, pixel_2, pixel_3, pixel_4, pixel_5, pixel_6):
        """Constructor"""
        self.pixel_1 = pixel_1
        self.pixel_2 = pixel_2
        self.pixel_3 = pixel_3
        self.pixel_4 = pixel_4
        self.pixel_5 = pixel_5
        self.pixel_6 = pixel_6

    def calc_ascii(self, divisor):
        """calulates the coresonding ascii char a given pixel value will have"""
        pixel_ascii_hash = []
        pixel_ascii_hash.append(self.pixel_1 // divisor)
        pixel_ascii_hash.append(self.pixel_2 // divisor)
        pixel_ascii_hash.append(self.pixel_3 // divisor)

        pixel_ascii_hash.append(self.pixel_4 // divisor)
        pixel_ascii_hash.append(self.pixel_5 // divisor)
        pixel_ascii_hash.append(self.pixel_6 // divisor)


        return pixel_ascii_hash

    def set_braille_char(self, mono_flag):
        """sets the coresponding braille char to a pixel matrix by comparing the pixels light value
           and constructing a bit pattersn to represent a the unicode char"""
        str_rep = ""

        temp_str_rep = list('000000')
        gray = 128
        if self.pixel_1 <= gray:
            temp_str_rep[0] = "1"

        if self.pixel_2 <= gray:
            temp_str_rep[1] = "1"

        if self.pixel_3 <= gray:
            temp_str_rep[2] = "1"

        if self.pixel_4 <= gray:
            temp_str_rep[3] = "1"

        if self.pixel_5 <= gray:
            temp_str_rep[4] = "1"

        if self.pixel_6 <= gray:
            temp_str_rep[5] = "1"


        str_rep = ''.join([str(elem) for elem in temp_str_rep])
        #print(str_rep)
        if str_rep == '000000' and mono_flag:
            self.braille_char = [('001000', '⠄')]
        else:
            self.braille_char = [dot_rep for dot_rep in BRAILLE if dot_rep[0] == str_rep]

    def get_braille_char(self):
        """return a brail unicode char"""
        return self.braille_char[0][1]

    def get_braille_bit_rep(self):
        """return a bit representaion of a braille unicode char"""
        return self.braille_char[0][0]



#('000000', '⠀'),
#('011101', '⠮'),
#('000010', '⠐'),
#('001111', '⠼'),
#('110101', '⠫'),
#('100101', '⠩'),
#('111101', '⠯'),
#('001000', '⠄'),
#('111011', '⠷'),
#('011111', '⠾'),
#('100001', '⠡'),
#('001101', '⠬'),
#('000001', '⠠'),
#('001001', '⠤'),
#('000101', '⠨'),
#('001100', '⠌'),
#('001011', '⠴'),
#('010000', '⠂'),
#('011000', '⠆'),
#('010010', '⠒'),
#('010011', '⠲'),
#('010001', '⠢'),
#('011010', '⠖'),
#('011011', '⠶'),
#('011001', '⠦'),
#('001010', '⠔'),
#('100011', '⠱'),
#('000011', '⠰'),
#('110001', '⠣'),
#('111111', '⠿'),
#('001110', '⠜'),
#('100111', '⠹'),
#('000100', '⠈'),
#('100000', '⠁'),
#('110000', '⠃'),
#('100100', '⠉'),
#('100110', '⠙'),
#('100010', '⠑'),
#('110100', '⠋'),
#('110110', '⠛'),
#('110010', '⠓'),
#('010100', '⠊'),
#('010110', '⠚'),
#('101000', '⠅'),
#('111000', '⠇'),
#('101100', '⠍'),
#('101110', '⠝'),
#('101010', '⠕'),
#('111100', '⠏'),
#('111110', '⠟'),
#('111010', '⠗'),
#('011100', '⠎'),
#('011110', '⠞'),
#('101001', '⠥'),
#('111001', '⠧'),
#('010111', '⠺'),
#('101101', '⠭'),
#('101111', '⠽'),
#('101011', '⠵'),
#('010101', '⠪'),
#('110011', '⠳'),
#('110111', '⠻'),
#('000110', '⠘'),
#('000111', '⠸')
