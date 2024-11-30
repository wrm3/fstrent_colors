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
	'KoC', 'RoC', 'GoC', 'YoC', 'BoC', 'MoC', 'CoC', 'WoC', 'LGyoC', 'DGyoC', 'LRoC', 'LGoC', 'LYoC', 'LBoC', 'LMoC', 'LCoC',
	'KoLC', 'RoLC', 'GoLC', 'YoLC', 'BoLC', 'MoLC', 'CoLC', 'WoLC', 'LGyoLC', 'DGyoLC', 'LRoLC', 'LGoLC', 'LYoLC', 'LBoLC', 'LMoLC', 'LCoLC'
]


#<=====>#
# Classes
#<=====>#



#<=====>#
# Functions
#<=====>#

def KoC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='black', bg_color='cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='black', bg_color='cyan', *args, **kwargs)

#<=====>#

def RoC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='red', bg_color='cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='red', bg_color='cyan', *args, **kwargs)

#<=====>#

def GoC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='green', bg_color='cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='green', bg_color='cyan', *args, **kwargs)

#<=====>#

def YoC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='yellow', bg_color='cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='yellow', bg_color='cyan', *args, **kwargs)

#<=====>#

def BoC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='blue', bg_color='cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='blue', bg_color='cyan', *args, **kwargs)

#<=====>#

def MoC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='magenta', bg_color='cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='magenta', bg_color='cyan', *args, **kwargs)

#<=====>#

def CoC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='cyan', bg_color='cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='cyan', bg_color='cyan', *args, **kwargs)

#<=====>#

def WoC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='white', bg_color='cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='white', bg_color='cyan', *args, **kwargs)

#<=====>#

def LGyoC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_grey', bg_color='cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_grey', bg_color='cyan', *args, **kwargs)

#<=====>#

def DGyoC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='dark_grey', bg_color='cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='dark_grey', bg_color='cyan', *args, **kwargs)

#<=====>#

def LRoC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_red', bg_color='cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_red', bg_color='cyan', *args, **kwargs)

#<=====>#

def LGoC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_green', bg_color='cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_green', bg_color='cyan', *args, **kwargs)

#<=====>#

def LYoC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_yellow', bg_color='cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_yellow', bg_color='cyan', *args, **kwargs)

#<=====>#

def LBoC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_blue', bg_color='cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_blue', bg_color='cyan', *args, **kwargs)

#<=====>#

def LMoC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_magenta', bg_color='cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_magenta', bg_color='cyan', *args, **kwargs)

#<=====>#

def LCoC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_cyan', bg_color='cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_cyan', bg_color='cyan', *args, **kwargs)

#<=====>#

def KoLC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='black', bg_color='light_cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='black', bg_color='light_cyan', *args, **kwargs)

#<=====>#

def RoLC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='red', bg_color='light_cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='red', bg_color='light_cyan', *args, **kwargs)

#<=====>#

def GoLC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='green', bg_color='light_cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='green', bg_color='light_cyan', *args, **kwargs)

#<=====>#

def YoLC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='yellow', bg_color='light_cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='yellow', bg_color='light_cyan', *args, **kwargs)

#<=====>#

def BoLC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='blue', bg_color='light_cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='blue', bg_color='light_cyan', *args, **kwargs)

#<=====>#

def MoLC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='magenta', bg_color='light_cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='magenta', bg_color='light_cyan', *args, **kwargs)

#<=====>#

def CoLC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='cyan', bg_color='light_cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='cyan', bg_color='light_cyan', *args, **kwargs)

#<=====>#

def WoLC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='white', bg_color='light_cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='white', bg_color='light_cyan', *args, **kwargs)

#<=====>#

def LGyoLC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_grey', bg_color='light_cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_grey', bg_color='light_cyan', *args, **kwargs)

#<=====>#

def DGyoLC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='dark_grey', bg_color='light_cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='dark_grey', bg_color='light_cyan', *args, **kwargs)

#<=====>#

def LRoLC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_red', bg_color='light_cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_red', bg_color='light_cyan', *args, **kwargs)

#<=====>#

def LGoLC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_green', bg_color='light_cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_green', bg_color='light_cyan', *args, **kwargs)

#<=====>#

def LYoLC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_yellow', bg_color='light_cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_yellow', bg_color='light_cyan', *args, **kwargs)

#<=====>#

def LBoLC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_blue', bg_color='light_cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_blue', bg_color='light_cyan', *args, **kwargs)

#<=====>#

def LMoLC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_magenta', bg_color='light_cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_magenta', bg_color='light_cyan', *args, **kwargs)

#<=====>#

def LCoLC(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_cyan', bg_color='light_cyan', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_cyan', bg_color='light_cyan', *args, **kwargs)

#<=====>#
# Assignments Post
#<=====>#



#<=====>#
# Default Run
#<=====>#


