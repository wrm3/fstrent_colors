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
	'KoB', ' RoB', ' GoB', ' YoB', ' BoB', ' MoB', ' CoB', ' WoB', ' LGyoB', ' DGyoB', ' LRoB', ' LGoB', ' LYoB', ' LBoB', ' LMoB', ' LCoB',
	'KoLB', ' RoLB', ' GoLB', ' YoLB', ' BoLB', ' MoLB', ' CoLB', ' WoLB', ' LGyoLB', ' DGyoLB', ' LRoLB', ' LGoLB', ' LYoLB', ' LBoLB', ' LMoLB', ' LCoLB'
	]


#<=====>#
# Classes
#<=====>#



#<=====>#
# Functions
#<=====>#

def KoB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='black', bg_color='blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='black', bg_color='blue', *args, **kwargs)

#<=====>#

def RoB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='red', bg_color='blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='red', bg_color='blue', *args, **kwargs)

#<=====>#

def GoB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='green', bg_color='blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='green', bg_color='blue', *args, **kwargs)

#<=====>#

def YoB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='yellow', bg_color='blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='yellow', bg_color='blue', *args, **kwargs)

#<=====>#

def BoB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='blue', bg_color='blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='blue', bg_color='blue', *args, **kwargs)

#<=====>#

def MoB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='magenta', bg_color='blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='magenta', bg_color='blue', *args, **kwargs)

#<=====>#

def CoB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='cyan', bg_color='blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='cyan', bg_color='blue', *args, **kwargs)

#<=====>#

def WoB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='white', bg_color='blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='white', bg_color='blue', *args, **kwargs)

#<=====>#

def LGyoB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_grey', bg_color='blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_grey', bg_color='blue', *args, **kwargs)

#<=====>#

def DGyoB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='dark_grey', bg_color='blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='dark_grey', bg_color='blue', *args, **kwargs)

#<=====>#

def LRoB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_red', bg_color='blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_red', bg_color='blue', *args, **kwargs)

#<=====>#

def LGoB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_green', bg_color='blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_green', bg_color='blue', *args, **kwargs)

#<=====>#

def LYoB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_yellow', bg_color='blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_yellow', bg_color='blue', *args, **kwargs)

#<=====>#

def LBoB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_blue', bg_color='blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_blue', bg_color='blue', *args, **kwargs)

#<=====>#

def LMoB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_magenta', bg_color='blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_magenta', bg_color='blue', *args, **kwargs)

#<=====>#

def LCoB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_cyan', bg_color='blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_cyan', bg_color='blue', *args, **kwargs)

#<=====>#

def KoLB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='black', bg_color='light_blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='black', bg_color='light_blue', *args, **kwargs)

#<=====>#

def RoLB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='red', bg_color='light_blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='red', bg_color='light_blue', *args, **kwargs)

#<=====>#

def GoLB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='green', bg_color='light_blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='green', bg_color='light_blue', *args, **kwargs)

#<=====>#

def YoLB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='yellow', bg_color='light_blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='yellow', bg_color='light_blue', *args, **kwargs)

#<=====>#

def BoLB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='blue', bg_color='light_blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='blue', bg_color='light_blue', *args, **kwargs)

#<=====>#

def MoLB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='magenta', bg_color='light_blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='magenta', bg_color='light_blue', *args, **kwargs)

#<=====>#

def CoLB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='cyan', bg_color='light_blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='cyan', bg_color='light_blue', *args, **kwargs)

#<=====>#

def WoLB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='white', bg_color='light_blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='white', bg_color='light_blue', *args, **kwargs)

#<=====>#

def LGyoLB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_grey', bg_color='light_blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_grey', bg_color='light_blue', *args, **kwargs)

#<=====>#

def DGyoLB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='dark_grey', bg_color='light_blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='dark_grey', bg_color='light_blue', *args, **kwargs)

#<=====>#

def LRoLB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_red', bg_color='light_blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_red', bg_color='light_blue', *args, **kwargs)

#<=====>#

def LGoLB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_green', bg_color='light_blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_green', bg_color='light_blue', *args, **kwargs)

#<=====>#

def LYoLB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_yellow', bg_color='light_blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_yellow', bg_color='light_blue', *args, **kwargs)

#<=====>#

def LBoLB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_blue', bg_color='light_blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_blue', bg_color='light_blue', *args, **kwargs)

#<=====>#

def LMoLB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_magenta', bg_color='light_blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_magenta', bg_color='light_blue', *args, **kwargs)

#<=====>#

def LCoLB(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_cyan', bg_color='light_blue', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_cyan', bg_color='light_blue', *args, **kwargs)

#<=====>#
# Assignments Post
#<=====>#



#<=====>#
# Default Run
#<=====>#


