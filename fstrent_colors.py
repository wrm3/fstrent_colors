"""FSTrent Colors - Enhanced colors options for terminal output."""

__version__ = "0.1.0"

# Re-export everything from base
from fstrent_colors_base import (
    cs, cp, pallette, CLR,
    K, R, G, Y, B, M, C, W, LGy, DGy, LR, LG, LY, LB, LM, LC,
    demo1, demo2, demo3, demo4, demo5, 
    demo6, demo7, demo8, demo9
)

# Re-export from color-on-color modules
from fstrent_colors_on_black import (
    KoK, RoK, GoK, YoK, BoK, MoK, CoK, WoK, LGyoK, DGyoK, LRoK, LGoK, LYoK, LBoK, LMoK, LCoK,
)

from fstrent_colors_on_white import (
    KoW, RoW, GoW, YoW, BoW, MoW, CoW, WoW, LGyoW, DGyoW, LRoW, LGoW, LYoW, LBoW, LMoW, LCoW,
)

from fstrent_colors_on_gray import (
    KoLGy, RoLGy, GoLGy, YoLGy, BoLGy, MoLGy, CoLGy, WoLGy, LGyoLGy, DGyoLGy, LRoLGy, LGoLGy, LYoLGy, LBoLGy, LMoLGy, LCoLGy,
    KoDGy, RoDGy, GoDGy, YoDGy, BoDGy, MoDGy, CoDGy, WoDGy, LGyoDGy, DGyoDGy, LRoDGy, LGoDGy, LYoDGy, LBoDGy, LMoDGy, LCoDGy,
)

from fstrent_colors_on_blue import (
    KoB, RoB, GoB, YoB, BoB, MoB, CoB, WoB, LGyoB, DGyoB, LRoB, LGoB, LYoB, LBoB, LMoB, LCoB,
    KoLB, RoLB, GoLB, YoLB, BoLB, MoLB, CoLB, WoLB, LGyoLB, DGyoLB, LRoLB, LGoLB, LYoLB, LBoLB, LMoLB, LCoLB,
)

from fstrent_colors_on_cyan import (
    KoC, RoC, GoC, YoC, BoC, MoC, CoC, WoC, LGyoC, DGyoC, LRoC, LGoC, LYoC, LBoC, LMoC, LCoC,
    KoLC, RoLC, GoLC, YoLC, BoLC, MoLC, CoLC, WoLC, LGyoLC, DGyoLC, LRoLC, LGoLC, LYoLC, LBoLC, LMoLC, LCoLC,
)

from fstrent_colors_on_green import (
    KoG, RoG, GoG, YoG, BoG, MoG, CoG, WoG, LGyoG, DGyoG, LRoG, LGoG, LYoG, LBoG, LMoG, LCoG,
    KoLG, RoLG, GoLG, YoLG, BoLG, MoLG, CoLG, WoLG, LGyoLG, DGyoLG, LRoLG, LGoLG, LYoLG, LBoLG, LMoLG, LCoLG,
)

from fstrent_colors_on_magenta import (
    KoM, RoM, GoM, YoM, BoM, MoM, CoM, WoM, LGyoM, DGyoM, LRoM, LGoM, LYoM, LBoM, LMoM, LCoM,
    KoLM, RoLM, GoLM, YoLM, BoLM, MoLM, CoLM, WoLM, LGyoLM, DGyoLM, LRoLM, LGoLM, LYoLM, LBoLM, LMoLM, LCoLM,
)

from fstrent_colors_on_red import (
    KoR, RoR, GoR, YoR, BoR, MoR, CoR, WoR, LGyoR, DGyoR, LRoR, LGoR, LYoR, LBoR, LMoR, LCoR,
    KoLR, RoLR, GoLR, YoLR, BoLR, MoLR, CoLR, WoLR, LGyoLR, DGyoLR, LRoLR, LGoLR, LYoLR, LBoLR, LMoLR, LCoLR,
)

from fstrent_colors_on_yellow import (
    KoY, RoY, GoY, YoY, BoY, MoY, CoY, WoY, LGyoY, DGyoY, LRoY, LGoY, LYoY, LBoY, LMoY, LCoY,
    KoLY, RoLY, GoLY, YoLY, BoLY, MoLY, CoLY, WoLY, LGyoLY, DGyoLY, LRoLY, LGoLY, LYoLY, LBoLY, LMoLY, LCoLY,
)

# Define __all__ to control what gets imported with "from fstrent_colors import *"
__all__ = [
    'cs', 'cp', 'pallette', 'CLR',
    'K', 'R', 'G', 'Y', 'B', 'M', 'C', 'W', 'LGy', 'DGy', 'LR', 'LG', 'LY', 'LB', 'LM', 'LC',
    'demo1', 'demo2', 'demo3', 'demo4', 'demo5', 'demo6', 'demo7', 'demo8', 'demo9',
    'KoK', 'RoK', 'GoK', 'YoK', 'BoK', 'MoK', 'CoK', 'WoK',
    'LGyoK', 'DGyoK', 'LRoK', 'LGoK', 'LYoK', 'LBoK', 'LMoK', 'LCoK',
    'KoW', 'RoW', 'GoW', 'YoW', 'BoW', 'MoW', 'CoW', 'WoW',
    'LGyoW', 'DGyoW', 'LRoW', 'LGoW', 'LYoW', 'LBoW', 'LMoW', 'LCoW',
    'KoLGy', 'RoLGy', 'GoLGy', 'YoLGy', 'BoLGy', 'MoLGy', 'CoLGy', 'WoLGy',
    'LGyoLGy', 'DGyoLGy', 'LRoLGy', 'LGoLGy', 'LYoLGy', 'LBoLGy', 'LMoLGy', 'LCoLGy',
    'KoDGy', 'RoDGy', 'GoDGy', 'YoDGy', 'BoDGy', 'MoDGy', 'CoDGy', 'WoDGy',
    'LGyoDGy', 'DGyoDGy', 'LRoDGy', 'LGoDGy', 'LYoDGy', 'LBoDGy', 'LMoDGy', 'LCoDGy',
    'KoB', 'RoB', 'GoB', 'YoB', 'BoB', 'MoB', 'CoB', 'WoB',
    'LGyoB', 'DGyoB', 'LRoB', 'LGoB', 'LYoB', 'LBoB', 'LMoB', 'LCoB',
    'KoLB', 'RoLB', 'GoLB', 'YoLB', 'BoLB', 'MoLB', 'CoLB', 'WoLB',
    'LGyoLB', 'DGyoLB', 'LRoLB', 'LGoLB', 'LYoLB', 'LBoLB', 'LMoLB', 'LCoLB',
    'KoC', 'RoC', 'GoC', 'YoC', 'BoC', 'MoC', 'CoC', 'WoC',
    'LGyoC', 'DGyoC', 'LRoC', 'LGoC', 'LYoC', 'LBoC', 'LMoC', 'LCoC',
    'KoLC', 'RoLC', 'GoLC', 'YoLC', 'BoLC', 'MoLC', 'CoLC', 'WoLC',
    'LGyoLC', 'DGyoLC', 'LRoLC', 'LGoLC', 'LYoLC', 'LBoLC', 'LMoLC', 'LCoLC',
    'KoG', 'RoG', 'GoG', 'YoG', 'BoG', 'MoG', 'CoG', 'WoG',
    'LGyoG', 'DGyoG', 'LRoG', 'LGoG', 'LYoG', 'LBoG', 'LMoG', 'LCoG',
    'KoLG', 'RoLG', 'GoLG', 'YoLG', 'BoLG', 'MoLG', 'CoLG', 'WoLG',
    'LGyoLG', 'DGyoLG', 'LRoLG', 'LGoLG', 'LYoLG', 'LBoLG', 'LMoLG', 'LCoLG',
    'KoM', 'RoM', 'GoM', 'YoM', 'BoM', 'MoM', 'CoM', 'WoM',
    'LGyoM', 'DGyoM', 'LRoM', 'LGoM', 'LYoM', 'LBoM', 'LMoM', 'LCoM',
    'KoLM', 'RoLM', 'GoLM', 'YoLM', 'BoLM', 'MoLM', 'CoLM', 'WoLM',
    'LGyoLM', 'DGyoLM', 'LRoLM', 'LGoLM', 'LYoLM', 'LBoLM', 'LMoLM', 'LCoLM',
    'KoR', 'RoR', 'GoR', 'YoR', 'BoR', 'MoR', 'CoR', 'WoR',
    'LGyoR', 'DGyoR', 'LRoR', 'LGoR', 'LYoR', 'LBoR', 'LMoR', 'LCoR',
    'KoLR', 'RoLR', 'GoLR', 'YoLR', 'BoLR', 'MoLR', 'CoLR', 'WoLR',
    'LGyoLR', 'DGyoLR', 'LRoLR', 'LGoLR', 'LYoLR', 'LBoLR', 'LMoLR', 'LCoLR',
    'KoY', 'RoY', 'GoY', 'YoY', 'BoY', 'MoY', 'CoY', 'WoY',
    'LGyoY', 'DGyoY', 'LRoY', 'LGoY', 'LYoY', 'LBoY', 'LMoY', 'LCoY',
    'KoLY', 'RoLY', 'GoLY', 'YoLY', 'BoLY', 'MoLY', 'CoLY', 'WoLY',
    'LGyoLY', 'DGyoLY', 'LRoLY', 'LGoLY', 'LYoLY', 'LBoLY', 'LMoLY', 'LCoLY',
]

