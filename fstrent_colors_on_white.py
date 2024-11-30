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
	'KoW', ' RoW', ' GoW', ' YoW', ' BoW', ' MoW', ' CoW', ' WoW', ' LGyoW', ' DGyoW', ' LRoW', ' LGoW', ' LYoW', ' LBoW', ' LMoW', ' LCoW'
	]


#<=====>#
# Classes
#<=====>#



#<=====>#
# Functions
#<=====>#

def KoW(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='black', bg_color='white', *args, **kwargs)
	else: return cs(text=in_str, font_color='black', bg_color='white', *args, **kwargs)

#<=====>#

def RoW(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='red', bg_color='white', *args, **kwargs)
	else: return cs(text=in_str, font_color='red', bg_color='white', *args, **kwargs)

#<=====>#

def GoW(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='green', bg_color='white', *args, **kwargs)
	else: return cs(text=in_str, font_color='green', bg_color='white', *args, **kwargs)

#<=====>#

def YoW(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='yellow', bg_color='white', *args, **kwargs)
	else: return cs(text=in_str, font_color='yellow', bg_color='white', *args, **kwargs)

#<=====>#

def BoW(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='blue', bg_color='white', *args, **kwargs)
	else: return cs(text=in_str, font_color='blue', bg_color='white', *args, **kwargs)

#<=====>#

def MoW(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='magenta', bg_color='white', *args, **kwargs)
	else: return cs(text=in_str, font_color='magenta', bg_color='white', *args, **kwargs)

#<=====>#

def CoW(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='cyan', bg_color='white', *args, **kwargs)
	else: return cs(text=in_str, font_color='cyan', bg_color='white', *args, **kwargs)

#<=====>#

def WoW(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='white', bg_color='white', *args, **kwargs)
	else: return cs(text=in_str, font_color='white', bg_color='white', *args, **kwargs)

#<=====>#

def LGyoW(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_grey', bg_color='white', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_grey', bg_color='white', *args, **kwargs)

#<=====>#

def DGyoW(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='dark_grey', bg_color='white', *args, **kwargs)
	else: return cs(text=in_str, font_color='dark_grey', bg_color='white', *args, **kwargs)

#<=====>#

def LRoW(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_red', bg_color='white', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_red', bg_color='white', *args, **kwargs)

#<=====>#

def LGoW(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_green', bg_color='white', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_green', bg_color='white', *args, **kwargs)

#<=====>#

def LYoW(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_yellow', bg_color='white', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_yellow', bg_color='white', *args, **kwargs)

#<=====>#

def LBoW(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_blue', bg_color='white', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_blue', bg_color='white', *args, **kwargs)

#<=====>#

def LMoW(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_magenta', bg_color='white', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_magenta', bg_color='white', *args, **kwargs)

#<=====>#

def LCoW(in_str, print_tf=True, *args, **kwargs):
	if print_tf: cp(in_str, font_color='light_cyan', bg_color='white', *args, **kwargs)
	else: return cs(text=in_str, font_color='light_cyan', bg_color='white', *args, **kwargs)

#<=====>#
# Assignments Post
#<=====>#



#<=====>#
# Default Run
#<=====>#



