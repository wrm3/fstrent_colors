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
	'KoR', ' RoR', ' GoR', ' YoR', ' BoR', ' MoR', ' CoR', ' WoR', ' LGyoR', ' DGyoR', ' LRoR', ' LGoR', ' LYoR', ' LBoR', ' LMoR', ' LCoR',
	'KoLR', ' RoLR', ' GoLR', ' YoLR', ' BoLR', ' MoLR', ' CoLR', ' WoLR', ' LGyoLR', ' DGyoLR', ' LRoLR', ' LGoLR', ' LYoLR', ' LBoLR', ' LMoLR', ' LCoLR'
	]


#<=====>#
# Classes
#<=====>#



#<=====>#
# Functions
#<=====>#

def KoR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='black', bg_color='red', *args, **kwargs)
	else: return cs(text=in_str, font_color='black', bg_color='red', *args, **kwargs)

#<=====>#

def RoR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='red', bg_color='red', *args, **kwargs)
	else: return cs(text=in_str, font_color='red', bg_color='red', *args, **kwargs)

#<=====>#

def GoR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='green', bg_color='red', *args, **kwargs)
	else: return cs(text=in_str, font_color='green', bg_color='red', *args, **kwargs)

#<=====>#

def YoR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='yellow', bg_color='red', *args, **kwargs)
	else: return cs(text=in_str, font_color='yellow', bg_color='red', *args, **kwargs)

#<=====>#

def BoR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='blue', bg_color='red', *args, **kwargs)
	else: return cs(text=in_str, font_color='blue', bg_color='red', *args, **kwargs)

#<=====>#

def MoR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='magenta', bg_color='red', *args, **kwargs)
	else: return cs(text=in_str, font_color='magenta', bg_color='red', *args, **kwargs)

#<=====>#

def CoR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='cyan', bg_color='red', *args, **kwargs)
	else: return cs(text=in_str, font_color='cyan', bg_color='red', *args, **kwargs)

#<=====>#

def WoR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='white', bg_color='red', *args, **kwargs)
	else: return cs(text=in_str, font_color='white', bg_color='red', *args, **kwargs)

#<=====>#

def LGyoR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_grey', bg_color='red', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_grey', bg_color='red', *args, **kwargs)

#<=====>#

def DGyoR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='dark_grey', bg_color='red', *args, **kwargs)
	else: return cs(text=in_str, font_color='dark_grey', bg_color='red', *args, **kwargs)

#<=====>#

def LRoR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_red', bg_color='red', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_red', bg_color='red', *args, **kwargs)

#<=====>#

def LGoR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_green', bg_color='red', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_green', bg_color='red', *args, **kwargs)

#<=====>#

def LYoR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_yellow', bg_color='red', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_yellow', bg_color='red', *args, **kwargs)

#<=====>#

def LBoR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_blue', bg_color='red', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_blue', bg_color='red', *args, **kwargs)

#<=====>#

def LMoR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_magenta', bg_color='red', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_magenta', bg_color='red', *args, **kwargs)

#<=====>#

def LCoR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_cyan', bg_color='red', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_cyan', bg_color='red', *args, **kwargs)

#<=====>#

def KoLR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='black', bg_color='light_red', *args, **kwargs)
	else: return cs(text=in_str, font_color='black', bg_color='light_red', *args, **kwargs)

#<=====>#

def RoLR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='red', bg_color='light_red', *args, **kwargs)
	else: return cs(text=in_str, font_color='red', bg_color='light_red', *args, **kwargs)

#<=====>#

def GoLR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='green', bg_color='light_red', *args, **kwargs)
	else: return cs(text=in_str, font_color='green', bg_color='light_red', *args, **kwargs)

#<=====>#

def YoLR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='yellow', bg_color='light_red', *args, **kwargs)
	else: return cs(text=in_str, font_color='yellow', bg_color='light_red', *args, **kwargs)

#<=====>#

def BoLR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='blue', bg_color='light_red', *args, **kwargs)
	else: return cs(text=in_str, font_color='blue', bg_color='light_red', *args, **kwargs)

#<=====>#

def MoLR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='magenta', bg_color='light_red', *args, **kwargs)
	else: return cs(text=in_str, font_color='magenta', bg_color='light_red', *args, **kwargs)

#<=====>#

def CoLR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='cyan', bg_color='light_red', *args, **kwargs)
	else: return cs(text=in_str, font_color='cyan', bg_color='light_red', *args, **kwargs)

#<=====>#

def WoLR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='white', bg_color='light_red', *args, **kwargs)
	else: return cs(text=in_str, font_color='white', bg_color='light_red', *args, **kwargs)

#<=====>#

def LGyoLR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_grey', bg_color='light_red', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_grey', bg_color='light_red', *args, **kwargs)

#<=====>#

def DGyoLR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='dark_grey', bg_color='light_red', *args, **kwargs)
	else: return cs(text=in_str, font_color='dark_grey', bg_color='light_red', *args, **kwargs)

#<=====>#

def LRoLR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_red', bg_color='light_red', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_red', bg_color='light_red', *args, **kwargs)

#<=====>#

def LGoLR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_green', bg_color='light_red', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_green', bg_color='light_red', *args, **kwargs)

#<=====>#

def LYoLR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_yellow', bg_color='light_red', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_yellow', bg_color='light_red', *args, **kwargs)

#<=====>#

def LBoLR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_blue', bg_color='light_red', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_blue', bg_color='light_red', *args, **kwargs)

#<=====>#

def LMoLR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_magenta', bg_color='light_red', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_magenta', bg_color='light_red', *args, **kwargs)

#<=====>#

def LCoLR(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_cyan', bg_color='light_red', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_cyan', bg_color='light_red', *args, **kwargs)

#<=====>#
# Assignments Post
#<=====>#



#<=====>#
# Default Run
#<=====>#


