#<=====>#
# Description
#<=====>#



#<=====>#
# Known To Do List
#<=====>#



#<=====>#
# Imports
#<=====>#
import re
import os
import sys
import time

from colorama import init, Fore, Back, Style
# Initialize colorama
init()

#<=====>#
# Variables
#<=====>#
__all__ = [
	'K', ' R', ' G', ' Y', ' B', ' M', ' C', ' W', ' LGy', ' DGy', ' LR', ' LG', ' LY', ' LB', ' LM', ' LC',
	'cs', 'cp', 'CLR', 'pallette',
	'demo1', 'demo2', 'demo3', 'demo4', 'demo5', 'demo6', 'demo7', 'demo8', 'demo9'
	]



pallette = {}

# Reds
pallette["indianred"]             = "#CD5C5C"      # indianred                             #CD5C5C  205   92   92  389
pallette["lightcoral"]            = "#F08080"      # lightcoral                            #F08080  240  128  128  496
pallette["salmon"]                = "#FA8072"      # salmon                                #FA8072  250  128  114  492
pallette["darksalmon"]            = "#E9967A"      # darksalmon                            #E9967A  233  150  122  505
pallette["lightsalmon"]           = "#FFA07A"      # lightsalmon                           #FFA07A  255  160  122  537
pallette["crimson"]               = "#DC143C"      # crimson                               #DC143C  220   20   60  300
pallette["red"]                   = "#FF0000"      # red                                   #FF0000  255    0    0  255
pallette["firebrick"]             = "#B22222"      # firebrick                             #B22222  178   34   34  246
pallette["darkred"]               = "#8B0000"      # darkred                               #8B0000  139    0    0  139

# Pinks
pallette["pink"]                  = "#FFC0CB"      # pink                                  #FFC0CB  255  192  203  650
pallette["lightpink"]             = "#FFB6C1"      # lightpink                             #FFB6C1  255  182  193  630
pallette["hotpink"]               = "#FF69B4"      # hotpink                               #FF69B4  255  105  180  540
pallette["deeppink"]              = "#FF1493"      # deeppink                              #FF1493  255   20  147  422
pallette["mediumvioletred"]       = "#C71585"      # mediumvioletred                       #C71585  199   21  133  353
pallette["palevioletred"]         = "#DB7093"      # palevioletred                         #DB7093  219  112  147  478

# Oranges
pallette["lightsalmon"]           = "#FFA07A"      # lightsalmon                           #FFA07A  255  160  122  537
pallette["coral"]                 = "#FF7F50"      # coral                                 #FF7F50  255  127   80  462
pallette["tomato"]                = "#FF6347"      # tomato                                #FF6347  255   99   71  425
pallette["orangered"]             = "#FF4500"      # orangered                             #FF4500  255   69    0  324
pallette["darkorange"]            = "#FF8C00"      # darkorange                            #FF8C00  255  140    0  395
pallette["orange"]                = "#FFA500"      # orange                                #FFA500  255  165    0  420

# Yellows
pallette["gold"]                  = "#FFD700"      # gold                                  #FFD700  255  215    0  470
pallette["yellow"]                = "#FFFF00"      # yellow                                #FFFF00  255  255    0  510
pallette["lightyellow"]           = "#FFFFE0"      # lightyellow                           #FFFFE0  255  255  224  734
pallette["lemonchiffon"]          = "#FFFACD"      # lemonchiffon                          #FFFACD  255  250  205  710
pallette["lightgoldenrodyellow"]  = "#FAFAD2"      # lightgoldenrodyellow                  #FAFAD2  250  250  210  710
pallette["papayawhip"]            = "#FFEFD5"      # papayawhip                            #FFEFD5  255  239  213  707
pallette["moccasin"]              = "#FFE4B5"      # moccasin                              #FFE4B5  255  228  181  664
pallette["peachpuff"]             = "#FFDAB9"      # peachpuff                             #FFDAB9  255  218  185  658
pallette["palegoldenrod"]         = "#EEE8AA"      # palegoldenrod                         #EEE8AA  238  232  170  640
pallette["darkkhaki"]             = "#BDB76B"      # darkkhaki                             #BDB76B  189  183  107  479
pallette["khaki"]                 = "#F0E68C"      # khaki                                 #F0E68C  240  230  140  610

# Purples
pallette["lavender"]              = "#E6E6FA"      # lavender                              #E6E6FA  230  230  250  710
pallette["thistle"]               = "#D8BFD8"      # thistle                               #D8BFD8  216  191  216  623
pallette["plum"]                  = "#DDA0DD"      # plum                                  #DDA0DD  221  160  221  602
pallette["violet"]                = "#EE82EE"      # violet                                #EE82EE  238  130  238  606
pallette["orchid"]                = "#DA70D6"      # orchid                                #DA70D6  218  112  214  544
pallette["fuchsia"]               = "#FF00FF"      # fuchsia                               #FF00FF  255    0  255  510
pallette["magenta"]               = "#FF00FF"      # magenta                               #FF00FF  255    0  255  510
pallette["mediumorchid"]          = "#BA55D3"      # mediumorchid                          #BA55D3  186   85  211  482
pallette["mediumpurple"]          = "#9370DB"      # mediumpurple                          #9370DB  147  112  219  478
pallette["rebeccapurple"]         = "#663399"      # rebeccapurple                         #663399  102   51  153  306
pallette["blueviolet"]            = "#8A2BE2"      # blueviolet                            #8A2BE2  138   43  226  407
pallette["darkviolet"]            = "#9400D3"      # darkviolet                            #9400D3  148    0  211  359
pallette["darkorchid"]            = "#9932CC"      # darkorchid                            #9932CC  153   50  204  407
pallette["darkmagenta"]           = "#8B008B"      # darkmagenta                           #8B008B  139    0  139  278
pallette["purple"]                = "#800080"      # purple                                #800080  128    0  128  256
pallette["indigo"]                = "#4B0082"      # indigo                                #4B0082   75    0  130  205
pallette["slateblue"]             = "#6A5ACD"      # slateblue                             #6A5ACD  106   90  205  401
pallette["darkslateblue"]         = "#483D8B"      # darkslateblue                         #483D8B   72   61  139  272
pallette["mediumslateblue"]       = "#7B68EE"      # mediumslateblue                       #7B68EE  123  104  238  465

# Greens
pallette["greenyellow"]           = "#ADFF2F"      # greenyellow                           #ADFF2F  173  255   47  475
pallette["chartreuse"]            = "#7FFF00"      # chartreuse                            #7FFF00  127  255    0  382
pallette["lawngreen"]             = "#7CFC00"      # lawngreen                             #7CFC00  124  252    0  376
pallette["lime"]                  = "#00FF00"      # lime                                  #00FF00    0  255    0  255
pallette["limegreen"]             = "#32CD32"      # limegreen                             #32CD32   50  205   50  305
pallette["palegreen"]             = "#98FB98"      # palegreen                             #98FB98  152  251  152  555
pallette["lightgreen"]            = "#90EE90"      # lightgreen                            #90EE90  144  238  144  526
pallette["mediumspringgreen"]     = "#00FA9A"      # mediumspringgreen                     #00FA9A    0  250  154  404
pallette["springgreen"]           = "#00FF7F"      # springgreen                           #00FF7F    0  255  127  382
pallette["mediumseagreen"]        = "#3CB371"      # mediumseagreen                        #3CB371   60  179  113  352
pallette["seagreen"]              = "#2E8B57"      # seagreen                              #2E8B57   46  139   87  272
pallette["forestgreen"]           = "#228B22"      # forestgreen                           #228B22   34  139   34  207
pallette["green"]                 = "#008000"      # green                                 #008000    0  128    0  128
pallette["darkgreen"]             = "#006400"      # darkgreen                             #006400    0  100    0  100
pallette["yellowgreen"]           = "#9ACD32"      # yellowgreen                           #9ACD32  154  205   50  409
pallette["olivedrab"]             = "#6B8E23"      # olivedrab                             #6B8E23  107  142   35  284
pallette["olive"]                 = "#808000"      # olive                                 #808000  128  128    0  256
pallette["darkolivegreen"]        = "#556B2F"      # darkolivegreen                        #556B2F   85  107   47  239
pallette["mediumaquamarine"]      = "#66CDAA"      # mediumaquamarine                      #66CDAA  102  205  170  477
pallette["darkseagreen"]          = "#8FBC8F"      # darkseagreen                          #8FBC8F  143  188  143  474
pallette["lightseagreen"]         = "#20B2AA"      # lightseagreen                         #20B2AA   32  178  170  380
pallette["darkcyan"]              = "#008B8B"      # darkcyan                              #008B8B    0  139  139  278
pallette["teal"]                  = "#008080"      # teal                                  #008080    0  128  128  256

# Blues
pallette["aqua"]                  = "#00FFFF"      # aqua                                  #00FFFF    0  255  255  510
pallette["cyan"]                  = "#00FFFF"      # cyan                                  #00FFFF    0  255  255  510
pallette["lightcyan"]             = "#E0FFFF"      # lightcyan                             #E0FFFF  224  255  255  734
pallette["paleturquoise"]         = "#AFEEEE"      # paleturquoise                         #AFEEEE  175  238  238  651
pallette["aquamarine"]            = "#7FFFD4"      # aquamarine                            #7FFFD4  127  255  212  594
pallette["turquoise"]             = "#40E0D0"      # turquoise                             #40E0D0   64  224  208  496
pallette["mediumturquoise"]       = "#48D1CC"      # mediumturquoise                       #48D1CC   72  209  204  485
pallette["darkturquoise"]         = "#00CED1"      # darkturquoise                         #00CED1    0  206  209  415
pallette["cadetblue"]             = "#5F9EA0"      # cadetblue                             #5F9EA0   95  158  160  413
pallette["steelblue"]             = "#4682B4"      # steelblue                             #4682B4   70  130  180  380
pallette["lightsteelblue"]        = "#B0C4DE"      # lightsteelblue                        #B0C4DE  176  196  222  594
pallette["powderblue"]            = "#B0E0E6"      # powderblue                            #B0E0E6  176  224  230  630
pallette["lightblue"]             = "#ADD8E6"      # lightblue                             #ADD8E6  173  216  230  619
pallette["skyblue"]               = "#87CEEB"      # skyblue                               #87CEEB  135  206  235  576
pallette["lightskyblue"]          = "#87CEFA"      # lightskyblue                          #87CEFA  135  206  250  591
pallette["deepskyblue"]           = "#00BFFF"      # deepskyblue                           #00BFFF    0  191  255  446
pallette["dodgerblue"]            = "#1E90FF"      # dodgerblue                            #1E90FF   30  144  255  429
pallette["cornflowerblue"]        = "#6495ED"      # cornflowerblue                        #6495ED  100  149  237  486
pallette["mediumslateblue"]       = "#7B68EE"      # mediumslateblue                       #7B68EE  123  104  238  465
pallette["royalblue"]             = "#4169E1"      # royalblue                             #4169E1   65  105  225  395
pallette["blue"]                  = "#0000FF"      # blue                                  #0000FF    0    0  255  255
pallette["mediumblue"]            = "#0000CD"      # mediumblue                            #0000CD    0    0  205  205
pallette["darkblue"]              = "#00008B"      # darkblue                              #00008B    0    0  139  139
pallette["navy"]                  = "#000080"      # navy                                  #000080    0    0  128  128
pallette["midnightblue"]          = "#191970"      # midnightblue                          #191970   25   25  112  162

# Browns
pallette["cornsilk"]              = "#FFF8DC"      # cornsilk                              #FFF8DC  255  248  220  723
pallette["blanchedalmond"]        = "#FFEBCD"      # blanchedalmond                        #FFEBCD  255  235  205  695
pallette["bisque"]                = "#FFE4C4"      # bisque                                #FFE4C4  255  228  196  679
pallette["navajowhite"]           = "#FFDEAD"      # navajowhite                           #FFDEAD  255  222  173  650
pallette["wheat"]                 = "#F5DEB3"      # wheat                                 #F5DEB3  245  222  179  646
pallette["burlywood"]             = "#DEB887"      # burlywood                             #DEB887  222  184  135  541
pallette["tan"]                   = "#D2B48C"      # tan                                   #D2B48C  210  180  140  530
pallette["rosybrown"]             = "#BC8F8F"      # rosybrown                             #BC8F8F  188  143  143  474
pallette["sandybrown"]            = "#F4A460"      # sandybrown                            #F4A460  244  164   96  504
pallette["goldenrod"]             = "#DAA520"      # goldenrod                             #DAA520  218  165   32  415
pallette["darkgoldenrod"]         = "#B8860B"      # darkgoldenrod                         #B8860B  184  134   11  329
pallette["peru"]                  = "#CD853F"      # peru                                  #CD853F  205  133   63  401
pallette["chocolate"]             = "#D2691E"      # chocolate                             #D2691E  210  105   30  345
pallette["saddlebrown"]           = "#8B4513"      # saddlebrown                           #8B4513  139   69   19  227
pallette["sienna"]                = "#A0522D"      # sienna                                #A0522D  160   82   45  287
pallette["brown"]                 = "#A52A2A"      # brown                                 #A52A2A  165   42   42  249
pallette["maroon"]                = "#800000"      # maroon                                #800000  128    0    0  128

# Whites
pallette["white"]                 = "#FFFFFF"      # white                                 #FFFFFF  255  255  255  765
pallette["snow"]                  = "#FFFAFA"      # snow                                  #FFFAFA  255  250  250  755
pallette["honeydew"]              = "#F0FFF0"      # honeydew                              #F0FFF0  240  255  240  735
pallette["mintcream"]             = "#F5FFFA"      # mintcream                             #F5FFFA  245  255  250  750
pallette["azure"]                 = "#F0FFFF"      # azure                                 #F0FFFF  240  255  255  750
pallette["aliceblue"]             = "#F0F8FF"      # aliceblue                             #F0F8FF  240  248  255  743
pallette["ghostwhite"]            = "#F8F8FF"      # ghostwhite                            #F8F8FF  248  248  255  751
pallette["whitesmoke"]            = "#F5F5F5"      # whitesmoke                            #F5F5F5  245  245  245  735
pallette["seashell"]              = "#FFF5EE"      # seashell                              #FFF5EE  255  245  238  738
pallette["beige"]                 = "#F5F5DC"      # beige                                 #F5F5DC  245  245  220  710
pallette["oldlace"]               = "#FDF5E6"      # oldlace                               #FDF5E6  253  245  230  728
pallette["floralwhite"]           = "#FFFAF0"      # floralwhite                           #FFFAF0  255  250  240  745
pallette["ivory"]                 = "#FFFFF0"      # ivory                                 #FFFFF0  255  255  240  750
pallette["antiquewhite"]          = "#FAEBD7"      # antiquewhite                          #FAEBD7  250  235  215  700
pallette["linen"]                 = "#FAF0E6"      # linen                                 #FAF0E6  250  240  230  720
pallette["lavenderblush"]         = "#FFF0F5"      # lavenderblush                         #FFF0F5  255  240  245  740
pallette["mistyrose"]             = "#FFE4E1"      # mistyrose                             #FFE4E1  255  228  225  708

# Grays
pallette["gainsboro"]             = "#DCDCDC"      # gainsboro                             #DCDCDC  220  220  220  660
pallette["lightgray"]             = "#D3D3D3"      # lightgray                             #D3D3D3  211  211  211  633
pallette["silver"]                = "#C0C0C0"      # silver                                #C0C0C0  192  192  192  576
pallette["darkgray"]              = "#A9A9A9"      # darkgray                              #A9A9A9  169  169  169  507
pallette["gray"]                  = "#808080"      # gray                                  #808080  128  128  128  384
pallette["dimgray"]               = "#696969"      # dimgray                               #696969  105  105  105  315
pallette["lightslategray"]        = "#778899"      # lightslategray                        #778899  119  136  153  408
pallette["slategray"]             = "#708090"      # slategray                             #708090  112  128  144  384
pallette["darkslategray"]         = "#2F4F4F"      # darkslategray                         #2F4F4F   47   79   79  205
pallette["black"]                 = "#000000"      # black                                 #000000    0    0    0    0


#<=====>#
# Classes
#<=====>#

class CLR:
	# Dictionary of HTML5 named colors with complete 147 entries
	pallette = pallette

	str_close = "\033[0m"

	hex_color_pattern = re.compile(r'#[0-9A-Fa-f]{6}\b')

	#<=====>#

	def __init__(self):

		# Check for a specific environment variable set by Windows Terminal
		# WT_SESSION is a common variable set by Windows Terminal
		self.probably_will_work = False
		if not self.probably_will_work:
			term_check = os.getenv('WT_SESSION')
			if term_check:
				self.probably_will_work = True

		if not self.probably_will_work:
			term_check = os.getenv('TERM_PROGRAM')
			if term_check and term_check == 'vscode':
				self.probably_will_work = True

	#<=====>#

	def rand_hex(self):
		"""
		Generates a random hex color code.
		Returns:
			str: A hex color code.
		"""
		# Randomly generate RGB values
		R = random.randint(0, 255)
		G = random.randint(0, 255)
		B = random.randint(0, 255)
		# Format as a hex color code
		return f"#{R:02X}{G:02X}{B:02X}"

	#<=====>#

	def name2hex(self, color_name):
		"""Convert color name to hex code."""
		color_map = {
			'black': '#000000',
			'red': '#FF0000',
			'green': '#00FF00',
			'yellow': '#FFFF00',
			'blue': '#0000FF',
			'magenta': '#FF00FF',
			'cyan': '#00FFFF',
			'white': '#FFFFFF',
			'light_grey': '#D3D3D3',  # Fix for light grey
			'dark_grey': '#A9A9A9',
			'light_red': '#FF6666',
			'light_green': '#90EE90',
			'light_yellow': '#FFFFE0',
			'light_blue': '#ADD8E6',
			'light_magenta': '#FFB6C1',
			'light_cyan': '#E0FFFF'
		}
		return color_map.get(color_name.lower(), '#FFFFFF')

	#<=====>#

	def hex2int(self, x):
		return int(x, 16)

	#<=====>#

	def hex2rgb(self, x):
		r = self.hex2int(x[1:3])
		g = self.hex2int(x[3:5])
		b = self.hex2int(x[5:7])
		return r, g, b

	#<=====>#

	def int2hex(self, x):
		return format(x, '02x')

	#<=====>#

	def lumi_get(self, x):
		r = self.hex2int(x[1:3])
		g = self.hex2int(x[3:5])
		b = self.hex2int(x[5:7])
		l = round(0.2126 * r + 0.7152 * g + 0.0722 * b,2)
		return l

	#<=====>#

	def lumi_inv_hex(self, x):
		lumi = c.lumi_get(x)
		if lumi >= 191:
			inv_color = self.name2hex('black')
		elif lumi >= 127:
			inv_color = self.name2hex('red')
		elif lumi >= 63:
			inv_color = self.name2hex('yellow')
		else:
			inv_color = self.name2hex('white')
		return inv_color

	#<=====>#

	def inv_hex(self, color_cd):
		r = self.hex2int(color_cd[1:3])
		g = self.hex2int(color_cd[3:5])
		b = self.hex2int(color_cd[5:7])
		r_inv = 255 - r
		g_inv = 255 - g
		b_inv = 255 - b
		r_new = self.int2hex(r_inv)
		g_new = self.int2hex(g_inv)
		b_new = self.int2hex(b_inv)
		inv_color = '#{}{}{}'.format(r_new, g_new, b_new)
		return inv_color

	#<=====>#

	def color_string(self, text, font_color, bg_color='black', bold=False, italic=False, length=0, align='left'):
		if length: length = int(length)
		"""
		Returns a colorized string using ANSI escape sequences.
		:param text: The text to be colorized.
		:param font_color: The font color (name or hex).
		:param bg_color: The background color (name or hex).
		:param bold: Boolean to indicate if text should be bold.
		:param italic: Boolean to indicate if text should be italic.
		:return: A string with ANSI escape codes.
		"""

		length_str = max(length, len(text))

		if align == 'left': align_str = '<'
		elif align == 'center': align_str = '^'
		elif align == 'right': align_str = '>'
		else: align_str = ''

		text = f'{text:{align_str}{length_str}}'

		if not self.probably_will_work:
#			print(term_check)
			return text

		# Resolve named colors or validate hex codes

		if not self.hex_color_pattern.match(font_color):
			font_color = self.name2hex(font_color)
		if not self.hex_color_pattern.match(bg_color):
			bg_color = self.name2hex(bg_color)

		font_r, font_g, font_b = int(font_color[1:3], 16), int(font_color[3:5], 16), int(font_color[5:7], 16)
		bg_r, bg_g, bg_b = int(bg_color[1:3], 16), int(bg_color[3:5], 16), int(bg_color[5:7], 16)

		# Build the ANSI escape sequence for styles and colors
		style_code = ''
		if bold:
			style_code += '\x1b[1m'
		if italic:
			style_code += '\x1b[3m'
		r = f"{style_code}\x1b[38;2;{font_r};{font_g};{font_b}m\x1b[48;2;{bg_r};{bg_g};{bg_b}m{text}\x1b[0m"
		r += self.str_close
		return r

	#<=====>#

	def color_print(self, text, font_color, bg_color='black', bold=False, italic=False, length=0, align='left'):
		"""
		Prints a colorized string to the terminal using ANSI escape sequences.
		:param text: The text to be printed.
		:param font_color: The font color (name or hex).
		:param bg_color: The background color (name or hex).
		:param bold: Boolean to indicate if text should be bold.
		:param italic: Boolean to indicate if text should be italic.
		"""
		colorized_text = self.color_string(text, font_color, bg_color, bold, italic, length, align)
		print(colorized_text)

	#<=====>#

	def demo1(self):
		return "Demo 1"

	#<=====>#

	def demo2(self):
		return "Demo 2"

	#<=====>#

	def demo3(self):
		return "Demo 3"

	#<=====>#

	def demo4(self):
		return "Demo 4"

	#<=====>#

	def demo5(self):
		return "Demo 5"

	#<=====>#

	def demo6(self):
		return "Demo 6"

	#<=====>#

	def demo7(self):
		return "Demo 7"

	#<=====>#

	def demo8(self):
		return "Demo 8"

	#<=====>#

	def demo9(self):
		return "Demo 9"

#<=====>#
# Functions
#<=====>#

def cs(text, font_color, bg_color='black', bold=False, italic=False, length=0, align='left'):
	r = c.color_string(text, font_color=font_color, bg_color=bg_color, bold=bold, italic=italic, length=length, align=align)
	return r

#<=====>#

def cp(text, font_color, bg_color='black', bold=False, italic=False, length=0, align='left'):
	c.color_print(text, font_color=font_color, bg_color=bg_color, bold=bold, italic=italic, length=length, align=align)

#<=====>#

def K(in_str, print_tf=True, *args, **kwargs):
	if print_tf:
		cp(in_str, font_color='black', *args, **kwargs)
	else:
		return cs(text=in_str, font_color='black', *args, **kwargs)

#<=====>#

def R(in_str, print_tf=True, *args, **kwargs):
	if print_tf:
		cp(in_str, font_color='red', *args, **kwargs)
	else:
		return cs(text=in_str, font_color='red', *args, **kwargs)

#<=====>#

def G(in_str, print_tf=True, *args, **kwargs):
	if print_tf:
		cp(in_str, font_color='green', *args, **kwargs)
	else:
		return cs(text=in_str, font_color='green', *args, **kwargs)

#<=====>#

def Y(in_str, print_tf=True, *args, **kwargs):
	if print_tf:
		cp(in_str, font_color='yellow', *args, **kwargs)
	else:
		return cs(text=in_str, font_color='yellow', *args, **kwargs)

#<=====>#

def B(in_str, print_tf=True, *args, **kwargs):
	if print_tf:
		cp(in_str, font_color='blue', *args, **kwargs)
	else:
		return cs(text=in_str, font_color='blue', *args, **kwargs)

#<=====>#

def M(in_str, print_tf=True, *args, **kwargs):
	if print_tf:
		cp(in_str, font_color='magenta', *args, **kwargs)
	else:
		return cs(text=in_str, font_color='magenta', *args, **kwargs)

#<=====>#

def C(in_str, print_tf=True, *args, **kwargs):
	if print_tf:
		cp(in_str, font_color='cyan', *args, **kwargs)
	else:
		return cs(text=in_str, font_color='cyan', *args, **kwargs)

#<=====>#

def W(in_str, print_tf=True, *args, **kwargs):
	if print_tf:
		cp(in_str, font_color='white', *args, **kwargs)
	else:
		return cs(text=in_str, font_color='white', *args, **kwargs)

#<=====>#

def LGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf:
		cp(in_str, font_color='light_grey', *args, **kwargs)
	else:
		return cs(text=in_str, font_color='light_grey', *args, **kwargs)

#<=====>#

def DGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf:
		cp(in_str, font_color='dark_grey', *args, **kwargs)
	else:
		return cs(text=in_str, font_color='dark_grey', *args, **kwargs)

#<=====>#

def LR(in_str, print_tf=True, *args, **kwargs):
	if print_tf:
		cp(in_str, font_color='light_red', *args, **kwargs)
	else:
		return cs(text=in_str, font_color='light_red', *args, **kwargs)

#<=====>#

def LG(in_str, print_tf=True, *args, **kwargs):
	if print_tf:
		cp(in_str, font_color='light_green', *args, **kwargs)
	else:
		return cs(text=in_str, font_color='light_green', *args, **kwargs)

#<=====>#

def LY(in_str, print_tf=True, *args, **kwargs):
	if print_tf:
		cp(in_str, font_color='light_yellow', *args, **kwargs)
	else:
		return cs(text=in_str, font_color='light_yellow', *args, **kwargs)

#<=====>#

def LB(in_str, print_tf=True, *args, **kwargs):
	if print_tf:
		cp(in_str, font_color='light_blue', *args, **kwargs)
	else:
		return cs(text=in_str, font_color='light_blue', *args, **kwargs)

#<=====>#

def LM(in_str, print_tf=True, *args, **kwargs):
	if print_tf:
		cp(in_str, font_color='light_magenta', *args, **kwargs)
	else:
		return cs(text=in_str, font_color='light_magenta', *args, **kwargs)

#<=====>#

def LC(in_str, print_tf=True, *args, **kwargs):
	if print_tf:
		cp(in_str, font_color='light_cyan', *args, **kwargs)
	else:
		return cs(text=in_str, font_color='light_cyan', *args, **kwargs)

#<=====>#
# Assignments Post
#<=====>#

c = CLR()

#<=====>#
# Default Run
#<=====>#

if __name__ == "__main__":
	# Example usage
	cp('demos','white','green')
	c.demo1()
	c.demo2()
	c.demo3()
	c.demo4()
	c.demo5()
	c.demo6()
	c.demo7()
	c.demo8()
	c.demo9()
