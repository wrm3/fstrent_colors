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
	'KoM', ' RoM', ' GoM', ' YoM', ' BoM', ' MoM', ' CoM', ' WoM', ' LGyoM', ' DGyoM', ' LRoM', ' LGoM', ' LYoM', ' LBoM', ' LMoM', ' LCoM',
	'KoLM', ' RoLM', ' GoLM', ' YoLM', ' BoLM', ' MoLM', ' CoLM', ' WoLM', ' LGyoLM', ' DGyoLM', ' LRoLM', ' LGoLM', ' LYoLM', ' LBoLM', ' LMoLM', ' LCoLM'
	]


#<=====>#
# Classes
#<=====>#



#<=====>#
# Functions
#<=====>#

#<=====>#

def KoM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='black', bg_color='magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='black', bg_color='magenta', *args, **kwargs)

#<=====>#

def RoM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='red', bg_color='magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='red', bg_color='magenta', *args, **kwargs)

#<=====>#

def GoM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='green', bg_color='magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='green', bg_color='magenta', *args, **kwargs)

#<=====>#

def YoM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='yellow', bg_color='magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='yellow', bg_color='magenta', *args, **kwargs)

#<=====>#

def BoM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='blue', bg_color='magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='blue', bg_color='magenta', *args, **kwargs)

#<=====>#

def MoM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='magenta', bg_color='magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='magenta', bg_color='magenta', *args, **kwargs)

#<=====>#

def CoM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='cyan', bg_color='magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='cyan', bg_color='magenta', *args, **kwargs)

#<=====>#

def WoM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='white', bg_color='magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='white', bg_color='magenta', *args, **kwargs)

#<=====>#

def LGyoM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_grey', bg_color='magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_grey', bg_color='magenta', *args, **kwargs)

#<=====>#

def DGyoM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='dark_grey', bg_color='magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='dark_grey', bg_color='magenta', *args, **kwargs)

#<=====>#

def LRoM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_red', bg_color='magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_red', bg_color='magenta', *args, **kwargs)

#<=====>#

def LGoM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_green', bg_color='magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_green', bg_color='magenta', *args, **kwargs)

#<=====>#

def LYoM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_yellow', bg_color='magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_yellow', bg_color='magenta', *args, **kwargs)

#<=====>#

def LBoM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_blue', bg_color='magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_blue', bg_color='magenta', *args, **kwargs)

#<=====>#

def LMoM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_magenta', bg_color='magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_magenta', bg_color='magenta', *args, **kwargs)

#<=====>#

def LCoM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_cyan', bg_color='magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_cyan', bg_color='magenta', *args, **kwargs)

#<=====>#

def KoLM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='black', bg_color='light_magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='black', bg_color='light_magenta', *args, **kwargs)

#<=====>#

def RoLM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='red', bg_color='light_magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='red', bg_color='light_magenta', *args, **kwargs)

#<=====>#

def GoLM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='green', bg_color='light_magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='green', bg_color='light_magenta', *args, **kwargs)

#<=====>#

def YoLM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='yellow', bg_color='light_magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='yellow', bg_color='light_magenta', *args, **kwargs)

#<=====>#

def BoLM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='blue', bg_color='light_magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='blue', bg_color='light_magenta', *args, **kwargs)

#<=====>#

def MoLM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='magenta', bg_color='light_magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='magenta', bg_color='light_magenta', *args, **kwargs)

#<=====>#

def CoLM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='cyan', bg_color='light_magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='cyan', bg_color='light_magenta', *args, **kwargs)

#<=====>#

def WoLM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='white', bg_color='light_magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='white', bg_color='light_magenta', *args, **kwargs)

#<=====>#

def LGyoLM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_grey', bg_color='light_magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_grey', bg_color='light_magenta', *args, **kwargs)

#<=====>#

def DGyoLM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='dark_grey', bg_color='light_magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='dark_grey', bg_color='light_magenta', *args, **kwargs)

#<=====>#

def LRoLM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_red', bg_color='light_magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_red', bg_color='light_magenta', *args, **kwargs)

#<=====>#

def LGoLM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_green', bg_color='light_magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_green', bg_color='light_magenta', *args, **kwargs)

#<=====>#

def LYoLM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_yellow', bg_color='light_magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_yellow', bg_color='light_magenta', *args, **kwargs)

#<=====>#

def LBoLM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_blue', bg_color='light_magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_blue', bg_color='light_magenta', *args, **kwargs)

#<=====>#

def LMoLM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_magenta', bg_color='light_magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_magenta', bg_color='light_magenta', *args, **kwargs)

#<=====>#

def LCoLM(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_cyan', bg_color='light_magenta', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_cyan', bg_color='light_magenta', *args, **kwargs)

#<=====>#
# Assignments Post
#<=====>#



#<=====>#
# Default Run
#<=====>#



