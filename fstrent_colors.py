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
from typing import Optional, Union, Dict, List
from colorama import init, Fore, Back, Style

from fstrent_colors_base import (
    cs, cp, pallette, CLR
)
from fstrent_colors_base import (
    K, R, G, Y, B, M, C, W, LGy, DGy, LR, LG, LY, LB, LM, LC,
)

from fstrent_colors_on_black import (
    KoK, RoK, GoK, YoK, BoK, MoK, CoK, WoK, LGyoK, DGyoK, LRoK, LGoK, LYoK, LBoK, LMoK, LCoK,
)

from fstrent_colors_on_white import (
    KoW, RoW, GoW, YoW, BoW, MoW, CoW, WoW, LGyoW, DGyoW, LRoW, LGoW, LYoW, LBoW, LMoW, LCoW,
)

from fstrent_colors_on_gray import (
    KoLGy, RoLGy, GoLGy, YoLGy, BoLGy, MoLGy, CoLGy, WoLGy, LGyoLGy, DGyoLGy, LRoLGy, LGoLGy, LYoLGy, LBoLGy, LMoLGy, LCoLGy,
)
from fstrent_colors_on_gray import (
    KoDGy, RoDGy, GoDGy, YoDGy, BoDGy, MoDGy, CoDGy, WoDGy, LGyoDGy, DGyoDGy, LRoDGy, LGoDGy, LYoDGy, LBoDGy, LMoDGy, LCoDGy,
)

from fstrent_colors_on_blue import (
    KoB, RoB, GoB, YoB, BoB, MoB, CoB, WoB, LGyoB, DGyoB, LRoB, LGoB, LYoB, LBoB, LMoB, LCoB,
)
from fstrent_colors_on_blue import (
    KoLB, RoLB, GoLB, YoLB, BoLB, MoLB, CoLB, WoLB, LGyoLB, DGyoLB, LRoLB, LGoLB, LYoLB, LBoLB, LMoLB, LCoLB,
)

from fstrent_colors_on_cyan import (
    KoC, RoC, GoC, YoC, BoC, MoC, CoC, WoC, LGyoC, DGyoC, LRoC, LGoC, LYoC, LBoC, LMoC, LCoC,
)
from fstrent_colors_on_cyan import (
    KoLC, RoLC, GoLC, YoLC, BoLC, MoLC, CoLC, WoLC, LGyoLC, DGyoLC, LRoLC, LGoLC, LYoLC, LBoLC, LMoLC, LCoLC,
)

from fstrent_colors_on_green import (
    KoG, RoG, GoG, YoG, BoG, MoG, CoG, WoG, LGyoG, DGyoG, LRoG, LGoG, LYoG, LBoG, LMoG, LCoG,
)
from fstrent_colors_on_green import (
    KoLG, RoLG, GoLG, YoLG, BoLG, MoLG, CoLG, WoLG, LGyoLG, DGyoLG, LRoLG, LGoLG, LYoLG, LBoLG, LMoLG, LCoLG,
)

from fstrent_colors_on_magenta import (
    KoM, RoM, GoM, YoM, BoM, MoM, CoM, WoM, LGyoM, DGyoM, LRoM, LGoM, LYoM, LBoM, LMoM, LCoM,
)
from fstrent_colors_on_magenta import (
    KoLM, RoLM, GoLM, YoLM, BoLM, MoLM, CoLM, WoLM, LGyoLM, DGyoLM, LRoLM, LGoLM, LYoLM, LBoLM, LMoLM, LCoLM,
)

from fstrent_colors_on_red import (
    KoR, RoR, GoR, YoR, BoR, MoR, CoR, WoR, LGyoR, DGyoR, LRoR, LGoR, LYoR, LBoR, LMoR, LCoR,
)
from fstrent_colors_on_red import (
    KoLR, RoLR, GoLR, YoLR, BoLR, MoLR, CoLR, WoLR, LGyoLR, DGyoLR, LRoLR, LGoLR, LYoLR, LBoLR, LMoLR, LCoLR,
)

from fstrent_colors_on_yellow import (
    KoY, RoY, GoY, YoY, BoY, MoY, CoY, WoY, LGyoY, DGyoY, LRoY, LGoY, LYoY, LBoY, LMoY, LCoY,
)
from fstrent_colors_on_yellow import (
    KoLY, RoLY, GoLY, YoLY, BoLY, MoLY, CoLY, WoLY, LGyoLY, DGyoLY, LRoLY, LGoLY, LYoLY, LBoLY, LMoLY, LCoLY,
)

# Initialize colorama
init()

#<=====>#
# Variables
#<=====>#
__all__ = [
	'cs', 'cp', 'pallette', 'CLR',
	'K', ' R', ' G', ' Y', ' B', ' M', ' C', ' W', ' LGy', ' DGy', ' LR', ' LG', ' LY', ' LB', ' LM', ' LC',

	'KoK', ' RoK', ' GoK', ' YoK', ' BoK', ' MoK', ' CoK', ' WoK', ' LGyoK', ' DGyoK', ' LRoK', ' LGoK', ' LYoK', ' LBoK', ' LMoK', ' LCoK',
	'KoW', ' RoW', ' GoW', ' YoW', ' BoW', ' MoW', ' CoW', ' WoW', ' LGyoW', ' DGyoW', ' LRoW', ' LGoW', ' LYoW', ' LBoW', ' LMoW', ' LCoW',

	'KoLGy', ' RoLGy', ' GoLGy', ' YoLGy', ' BoLGy', ' MoLGy', ' CoLGy', ' WoLGy', ' LGyoLGy', ' DGyoLGy', ' LRoLGy', ' LGoLGy', ' LYoLGy', ' LBoLGy', ' LMoLGy', ' LCoLGy',
	'KoDGy', ' RoDGy', ' GoDGy', ' YoDGy', ' BoDGy', ' MoDGy', ' CoDGy', ' WoDGy', ' LGyoDGy', ' DGyoDGy', ' LRoDGy', ' LGoDGy', ' LYoDGy', ' LBoDGy', ' LMoDGy', ' LCoDGy',

	'KoB', ' RoB', ' GoB', ' YoB', ' BoB', ' MoB', ' CoB', ' WoB', ' LGyoB', ' DGyoB', ' LRoB', ' LGoB', ' LYoB', ' LBoB', ' LMoB', ' LCoB',
	'KoC', ' RoC', ' GoC', ' YoC', ' BoC', ' MoC', ' CoC', ' WoC', ' LGyoC', ' DGyoC', ' LRoC', ' LGoC', ' LYoC', ' LBoC', ' LMoC', ' LCoC',
	'KoG', ' RoG', ' GoG', ' YoG', ' BoG', ' MoG', ' CoG', ' WoG', ' LGyoG', ' DGyoG', ' LRoG', ' LGoG', ' LYoG', ' LBoG', ' LMoG', ' LCoG',
	'KoM', ' RoM', ' GoM', ' YoM', ' BoM', ' MoM', ' CoM', ' WoM', ' LGyoM', ' DGyoM', ' LRoM', ' LGoM', ' LYoM', ' LBoM', ' LMoM', ' LCoM',
	'KoR', ' RoR', ' GoR', ' YoR', ' BoR', ' MoR', ' CoR', ' WoR', ' LGyoR', ' DGyoR', ' LRoR', ' LGoR', ' LYoR', ' LBoR', ' LMoR', ' LCoR',
	'KoY', ' RoY', ' GoY', ' YoY', ' BoY', ' MoY', ' CoY', ' WoY', ' LGyoY', ' DGyoY', ' LRoY', ' LGoY', ' LYoY', ' LBoY', ' LMoY', ' LCoY',

	'KoLB', ' RoLB', ' GoLB', ' YoLB', ' BoLB', ' MoLB', ' CoLB', ' WoLB', ' LGyoLB', ' DGyoLB', ' LRoLB', ' LGoLB', ' LYoLB', ' LBoLB', ' LMoLB', ' LCoLB',
	'KoLC', ' RoLC', ' GoLC', ' YoLC', ' BoLC', ' MoLC', ' CoLC', ' WoLC', ' LGyoLC', ' DGyoLC', ' LRoLC', ' LGoLC', ' LYoLC', ' LBoLC', ' LMoLC', ' LCoC',
	'KoLG', ' RoLG', ' GoLG', ' YoLG', ' BoLG', ' MoLG', ' CoLG', ' WoLG', ' LGyoLG', ' DGyoLG', ' LRoLG', ' LGoLG', ' LYoLG', ' LBoLG', ' LMoLG', ' LCoLG',
	'KoLM', ' RoLM', ' GoLM', ' YoLM', ' BoLM', ' MoLM', ' CoLM', ' WoLM', ' LGyoLM', ' DGyoLM', ' LRoLM', ' LGoLM', ' LYoLM', ' LBoLM', ' LMoLM', ' LCoLM',
	'KoLR', ' RoLR', ' GoLR', ' YoLR', ' BoLR', ' MoLR', ' CoLR', ' WoLR', ' LGyoLR', ' DGyoLR', ' LRoLR', ' LGoLR', ' LYoLR', ' LBoLR', ' LMoLR', ' LCoLR',
	'KoLY', ' RoLY', ' GoLY', ' YoLY', ' BoLY', ' MoLY', ' CoLY', ' WoLY', ' LGyoLY', ' DGyoLY', ' LRoLY', ' LGoLY', ' LYoLY', ' LBoLY', ' LMoLY', ' LCoLY'
	]


#<=====>#
# Classes
#<=====>#



#<=====>#
# Functions
#<=====>#



#<=====>#
# Assignments Post
#<=====>#



#<=====>#
# Default Run
#<=====>#


