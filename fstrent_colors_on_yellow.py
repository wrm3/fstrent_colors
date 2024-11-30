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
from fstrent_colors_base import cs, cp

#<=====>#
# Variables
#<=====>#
__all__ = [
	'KoY', ' RoY', ' GoY', ' YoY', ' BoY', ' MoY', ' CoY', ' WoY', ' LGyoY', ' DGyoY', ' LRoY', ' LGoY', ' LYoY', ' LBoY', ' LMoY', ' LCoY',
	'KoLY', ' RoLY', ' GoLY', ' YoLY', ' BoLY', ' MoLY', ' CoLY', ' WoLY', ' LGyoLY', ' DGyoLY', ' LRoLY', ' LGoLY', ' LYoLY', ' LBoLY', ' LMoLY', ' LCoLY'
	]


#<=====>#
# Classes
#<=====>#



#<=====>#
# Functions
#<=====>#

def KoY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='black', bg_color='yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='black', bg_color='yellow', *args, **kwargs)

#<=====>#

def RoY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='red', bg_color='yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='red', bg_color='yellow', *args, **kwargs)

#<=====>#

def GoY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='green', bg_color='yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='green', bg_color='yellow', *args, **kwargs)

#<=====>#

def YoY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='yellow', bg_color='yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='yellow', bg_color='yellow', *args, **kwargs)

#<=====>#

def BoY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='blue', bg_color='yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='blue', bg_color='yellow', *args, **kwargs)

#<=====>#

def MoY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='magenta', bg_color='yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='magenta', bg_color='yellow', *args, **kwargs)

#<=====>#

def CoY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='cyan', bg_color='yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='cyan', bg_color='yellow', *args, **kwargs)

#<=====>#

def WoY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='white', bg_color='yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='white', bg_color='yellow', *args, **kwargs)

#<=====>#

def LGyoY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_grey', bg_color='yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_grey', bg_color='yellow', *args, **kwargs)

#<=====>#

def DGyoY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='dark_grey', bg_color='yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='dark_grey', bg_color='yellow', *args, **kwargs)

#<=====>#

def LRoY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_red', bg_color='yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_red', bg_color='yellow', *args, **kwargs)

#<=====>#

def LGoY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_green', bg_color='yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_green', bg_color='yellow', *args, **kwargs)

#<=====>#

def LYoY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_yellow', bg_color='yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_yellow', bg_color='yellow', *args, **kwargs)

#<=====>#

def LBoY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_blue', bg_color='yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_blue', bg_color='yellow', *args, **kwargs)

#<=====>#

def LMoY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_magenta', bg_color='yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_magenta', bg_color='yellow', *args, **kwargs)

#<=====>#

def LCoY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_cyan', bg_color='yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_cyan', bg_color='yellow', *args, **kwargs)

#<=====>#

def KoLY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='black', bg_color='light_yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='black', bg_color='light_yellow', *args, **kwargs)

#<=====>#

def RoLY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='red', bg_color='light_yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='red', bg_color='light_yellow', *args, **kwargs)

#<=====>#

def GoLY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='green', bg_color='light_yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='green', bg_color='light_yellow', *args, **kwargs)

#<=====>#

def YoLY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='yellow', bg_color='light_yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='yellow', bg_color='light_yellow', *args, **kwargs)

#<=====>#

def BoLY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='blue', bg_color='light_yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='blue', bg_color='light_yellow', *args, **kwargs)

#<=====>#

def MoLY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='magenta', bg_color='light_yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='magenta', bg_color='light_yellow', *args, **kwargs)

#<=====>#

def CoLY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='cyan', bg_color='light_yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='cyan', bg_color='light_yellow', *args, **kwargs)

#<=====>#

def WoLY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='white', bg_color='light_yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='white', bg_color='light_yellow', *args, **kwargs)

#<=====>#

def LGyoLY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_grey', bg_color='light_yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_grey', bg_color='light_yellow', *args, **kwargs)

#<=====>#

def DGyoLY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='dark_grey', bg_color='light_yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='dark_grey', bg_color='light_yellow', *args, **kwargs)

#<=====>#

def LRoLY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_red', bg_color='light_yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_red', bg_color='light_yellow', *args, **kwargs)

#<=====>#

def LGoLY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_green', bg_color='light_yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_green', bg_color='light_yellow', *args, **kwargs)

#<=====>#

def LYoLY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_yellow', bg_color='light_yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_yellow', bg_color='light_yellow', *args, **kwargs)

#<=====>#

def LBoLY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_blue', bg_color='light_yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_blue', bg_color='light_yellow', *args, **kwargs)

#<=====>#

def LMoLY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_magenta', bg_color='light_yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_magenta', bg_color='light_yellow', *args, **kwargs)

#<=====>#

def LCoLY(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_cyan', bg_color='light_yellow', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_cyan', bg_color='light_yellow', *args, **kwargs)

#<=====>#
# Assignments Post
#<=====>#



#<=====>#
# Default Run
#<=====>#



