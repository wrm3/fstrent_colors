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
	'KoLGy', ' RoLGy', ' GoLGy', ' YoLGy', ' BoLGy', ' MoLGy', ' CoLGy', ' WoLGy', ' LGyoLGy', ' DGyoLGy', ' LRoLGy', ' LGoLGy', ' LYoLGy', ' LBoLGy', ' LMoLGy', ' LCoLGy',
	'KoDGy', ' RoDGy', ' GoDGy', ' YoDGy', ' BoDGy', ' MoDGy', ' CoDGy', ' WoDGy', ' LGyoDGy', ' DGyoDGy', ' LRoDGy', ' LGoDGy', ' LYoDGy', ' LBoDGy', ' LMoDGy', ' LCoDGy'
	]


#<=====>#
# Classes
#<=====>#



#<=====>#
# Functions
#<=====>#

def KoLGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='black', bg_color='light_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='black', bg_color='light_grey', *args, **kwargs)

#<=====>#

def RoLGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='red', bg_color='light_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='red', bg_color='light_grey', *args, **kwargs)

#<=====>#

def GoLGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='green', bg_color='light_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='green', bg_color='light_grey', *args, **kwargs)

#<=====>#

def YoLGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='yellow', bg_color='light_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='yellow', bg_color='light_grey', *args, **kwargs)

#<=====>#

def BoLGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='blue', bg_color='light_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='blue', bg_color='light_grey', *args, **kwargs)

#<=====>#

def MoLGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='magenta', bg_color='light_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='magenta', bg_color='light_grey', *args, **kwargs)

#<=====>#

def CoLGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='cyan', bg_color='light_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='cyan', bg_color='light_grey', *args, **kwargs)

#<=====>#

def WoLGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='white', bg_color='light_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='white', bg_color='light_grey', *args, **kwargs)

#<=====>#

def LGyoLGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_grey', bg_color='light_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_grey', bg_color='light_grey', *args, **kwargs)

#<=====>#

def DGyoLGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='dark_grey', bg_color='light_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='dark_grey', bg_color='light_grey', *args, **kwargs)

#<=====>#

def LRoLGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_red', bg_color='light_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_red', bg_color='light_grey', *args, **kwargs)

#<=====>#

def LGoLGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_green', bg_color='light_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_green', bg_color='light_grey', *args, **kwargs)

#<=====>#

def LYoLGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_yellow', bg_color='light_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_yellow', bg_color='light_grey', *args, **kwargs)

#<=====>#

def LBoLGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_blue', bg_color='light_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_blue', bg_color='light_grey', *args, **kwargs)

#<=====>#

def LMoLGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_magenta', bg_color='light_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_magenta', bg_color='light_grey', *args, **kwargs)

#<=====>#

def LCoLGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_cyan', bg_color='light_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_cyan', bg_color='light_grey', *args, **kwargs)

#<=====>#

def KoDGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='black', bg_color='dark_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='black', bg_color='dark_grey', *args, **kwargs)

#<=====>#

def RoDGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='red', bg_color='dark_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='red', bg_color='dark_grey', *args, **kwargs)

#<=====>#

def GoDGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='green', bg_color='dark_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='green', bg_color='dark_grey', *args, **kwargs)

#<=====>#

def YoDGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='yellow', bg_color='dark_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='yellow', bg_color='dark_grey', *args, **kwargs)

#<=====>#

def BoDGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='blue', bg_color='dark_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='blue', bg_color='dark_grey', *args, **kwargs)

#<=====>#

def MoDGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='magenta', bg_color='dark_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='magenta', bg_color='dark_grey', *args, **kwargs)

#<=====>#

def CoDGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='cyan', bg_color='dark_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='cyan', bg_color='dark_grey', *args, **kwargs)

#<=====>#

def WoDGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='white', bg_color='dark_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='white', bg_color='dark_grey', *args, **kwargs)

#<=====>#

def LGyoDGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_grey', bg_color='dark_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_grey', bg_color='dark_grey', *args, **kwargs)

#<=====>#

def DGyoDGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='dark_grey', bg_color='dark_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='dark_grey', bg_color='dark_grey', *args, **kwargs)

#<=====>#

def LRoDGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_red', bg_color='dark_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_red', bg_color='dark_grey', *args, **kwargs)

#<=====>#

def LGoDGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_green', bg_color='dark_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_green', bg_color='dark_grey', *args, **kwargs)

#<=====>#

def LYoDGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_yellow', bg_color='dark_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_yellow', bg_color='dark_grey', *args, **kwargs)

#<=====>#

def LBoDGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_blue', bg_color='dark_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_blue', bg_color='dark_grey', *args, **kwargs)

#<=====>#

def LMoDGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_magenta', bg_color='dark_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_magenta', bg_color='dark_grey', *args, **kwargs)

#<=====>#

def LCoDGy(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_cyan', bg_color='dark_grey', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_cyan', bg_color='dark_grey', *args, **kwargs)

#<=====>#
# Assignments Post
#<=====>#



#<=====>#
# Default Run
#<=====>#



