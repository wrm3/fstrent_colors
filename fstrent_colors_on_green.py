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
	'KoG', ' RoG', ' GoG', ' YoG', ' BoG', ' MoG', ' CoG', ' WoG', ' LGyoG', ' DGyoG', ' LRoG', ' LGoG', ' LYoG', ' LBoG', ' LMoG', ' LCoG',
	'KoLG', ' RoLG', ' GoLG', ' YoLG', ' BoLG', ' MoLG', ' CoLG', ' WoLG', ' LGyoLG', ' DGyoLG', ' LRoLG', ' LGoLG', ' LYoLG', ' LBoLG', ' LMoLG', ' LCoLG'
	]


#<=====>#
# Classes
#<=====>#



#<=====>#
# Functions
#<=====>#

def KoG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='black', bg_color='green', *args, **kwargs)
	else: return cs(text=in_str, font_color='black', bg_color='green', *args, **kwargs)

#<=====>#

def RoG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='red', bg_color='green', *args, **kwargs)
	else: return cs(text=in_str, font_color='red', bg_color='green', *args, **kwargs)

#<=====>#

def GoG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='green', bg_color='green', *args, **kwargs)
	else: return cs(text=in_str, font_color='green', bg_color='green', *args, **kwargs)

#<=====>#

def YoG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='yellow', bg_color='green', *args, **kwargs)
	else: return cs(text=in_str, font_color='yellow', bg_color='green', *args, **kwargs)

#<=====>#

def BoG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='blue', bg_color='green', *args, **kwargs)
	else: return cs(text=in_str, font_color='blue', bg_color='green', *args, **kwargs)

#<=====>#

def MoG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='magenta', bg_color='green', *args, **kwargs)
	else: return cs(text=in_str, font_color='magenta', bg_color='green', *args, **kwargs)

#<=====>#

def CoG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='cyan', bg_color='green', *args, **kwargs)
	else: return cs(text=in_str, font_color='cyan', bg_color='green', *args, **kwargs)

#<=====>#

def WoG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='white', bg_color='green', *args, **kwargs)
	else: return cs(text=in_str, font_color='white', bg_color='green', *args, **kwargs)

#<=====>#

def LGyoG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_grey', bg_color='green', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_grey', bg_color='green', *args, **kwargs)

#<=====>#

def DGyoG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='dark_grey', bg_color='green', *args, **kwargs)
	else: return cs(text=in_str, font_color='dark_grey', bg_color='green', *args, **kwargs)

#<=====>#

def LRoG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_red', bg_color='green', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_red', bg_color='green', *args, **kwargs)

#<=====>#

def LGoG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_green', bg_color='green', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_green', bg_color='green', *args, **kwargs)

#<=====>#

def LYoG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_yellow', bg_color='green', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_yellow', bg_color='green', *args, **kwargs)

#<=====>#

def LBoG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_blue', bg_color='green', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_blue', bg_color='green', *args, **kwargs)

#<=====>#

def LMoG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_magenta', bg_color='green', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_magenta', bg_color='green', *args, **kwargs)

#<=====>#

def LCoG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_cyan', bg_color='green', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_cyan', bg_color='green', *args, **kwargs)

#<=====>#

def KoLG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='black', bg_color='light_green', *args, **kwargs)
	else: return cs(text=in_str, font_color='black', bg_color='light_green', *args, **kwargs)

#<=====>#

def RoLG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='red', bg_color='light_green', *args, **kwargs)
	else: return cs(text=in_str, font_color='red', bg_color='light_green', *args, **kwargs)

#<=====>#

def GoLG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='green', bg_color='light_green', *args, **kwargs)
	else: return cs(text=in_str, font_color='green', bg_color='light_green', *args, **kwargs)

#<=====>#

def YoLG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='yellow', bg_color='light_green', *args, **kwargs)
	else: return cs(text=in_str, font_color='yellow', bg_color='light_green', *args, **kwargs)

#<=====>#

def BoLG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='blue', bg_color='light_green', *args, **kwargs)
	else: return cs(text=in_str, font_color='blue', bg_color='light_green', *args, **kwargs)

#<=====>#

def MoLG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='magenta', bg_color='light_green', *args, **kwargs)
	else: return cs(text=in_str, font_color='magenta', bg_color='light_green', *args, **kwargs)

#<=====>#

def CoLG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='cyan', bg_color='light_green', *args, **kwargs)
	else: return cs(text=in_str, font_color='cyan', bg_color='light_green', *args, **kwargs)

#<=====>#

def WoLG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='white', bg_color='light_green', *args, **kwargs)
	else: return cs(text=in_str, font_color='white', bg_color='light_green', *args, **kwargs)

#<=====>#

def LGyoLG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_grey', bg_color='light_green', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_grey', bg_color='light_green', *args, **kwargs)

#<=====>#

def DGyoLG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='dark_grey', bg_color='light_green', *args, **kwargs)
	else: return cs(text=in_str, font_color='dark_grey', bg_color='light_green', *args, **kwargs)

#<=====>#

def LRoLG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_red', bg_color='light_green', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_red', bg_color='light_green', *args, **kwargs)

#<=====>#

def LGoLG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_green', bg_color='light_green', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_green', bg_color='light_green', *args, **kwargs)

#<=====>#

def LYoLG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_yellow', bg_color='light_green', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_yellow', bg_color='light_green', *args, **kwargs)

#<=====>#

def LBoLG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_blue', bg_color='light_green', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_blue', bg_color='light_green', *args, **kwargs)

#<=====>#

def LMoLG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_magenta', bg_color='light_green', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_magenta', bg_color='light_green', *args, **kwargs)

#<=====>#

def LCoLG(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_cyan', bg_color='light_green', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_cyan', bg_color='light_green', *args, **kwargs)

#<=====>#
# Assignments Post
#<=====>#



#<=====>#
# Default Run
#<=====>#



