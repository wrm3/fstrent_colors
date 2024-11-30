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
	'KoK', ' RoK', ' GoK', ' YoK', ' BoK', ' MoK', ' CoK', ' WoK', ' LGyoK', ' DGyoK', ' LRoK', ' LGoK', ' LYoK', ' LBoK', ' LMoK', ' LCoK'
	]


#<=====>#
# Classes
#<=====>#



#<=====>#
# Functions
#<=====>#

def KoK(in_str, print_tf=True, *args, **kwargs):
	if print_tf:
		cp(in_str, font_color='black', bg_color='black', *args, **kwargs)
	else:
		return cs(text=in_str, font_color='black', bg_color='black', *args, **kwargs)

#<=====>#
		
def RoK(in_str, print_tf=True, *args, **kwargs):
	if print_tf:
		cp(in_str, font_color='red', bg_color='black', *args, **kwargs)
	else:
		return cs(text=in_str, font_color='red', bg_color='black', *args, **kwargs)

#<=====>#

def GoK(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='green', bg_color='black', *args, **kwargs)
	else: return cs(text=in_str, font_color='green', bg_color='black', *args, **kwargs)

#<=====>#

def YoK(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='yellow', bg_color='black', *args, **kwargs)
	else: return cs(text=in_str, font_color='yellow', bg_color='black', *args, **kwargs)

#<=====>#

def BoK(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='blue', bg_color='black', *args, **kwargs)
	else: return cs(text=in_str, font_color='blue', bg_color='black', *args, **kwargs)

#<=====>#

def MoK(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='magenta', bg_color='black', *args, **kwargs)
	else: return cs(text=in_str, font_color='magenta', bg_color='black', *args, **kwargs)

#<=====>#

def CoK(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='cyan', bg_color='black', *args, **kwargs)
	else: return cs(text=in_str, font_color='cyan', bg_color='black', *args, **kwargs)

#<=====>#

def WoK(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='white', bg_color='black', *args, **kwargs)
	else: return cs(text=in_str, font_color='white', bg_color='black', *args, **kwargs)

#<=====>#

def LGyoK(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_grey', bg_color='black', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_grey', bg_color='black', *args, **kwargs)

#<=====>#

def DGyoK(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='dark_grey', bg_color='black', *args, **kwargs)
	else: return cs(text=in_str, font_color='dark_grey', bg_color='black', *args, **kwargs)

#<=====>#

def LRoK(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_red', bg_color='black', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_red', bg_color='black', *args, **kwargs)

#<=====>#

def LGoK(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_green', bg_color='black', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_green', bg_color='black', *args, **kwargs)

#<=====>#

def LYoK(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_yellow', bg_color='black', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_yellow', bg_color='black', *args, **kwargs)

#<=====>#

def LBoK(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_blue', bg_color='black', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_blue', bg_color='black', *args, **kwargs)

#<=====>#

def LMoK(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_magenta', bg_color='black', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_magenta', bg_color='black', *args, **kwargs)

#<=====>#

def LCoK(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_cyan', bg_color='black', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_cyan', bg_color='black', *args, **kwargs)

#<=====>#
# Assignments Post
#<=====>#



#<=====>#
# Default Run
#<=====>#



