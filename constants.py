"""
    constants.py
    Hack & Hustle Academy Sampler
    Authored by Gurtej Singh
    Created on July 7, 2017
    Python Version 3.6
"""

import pygame.constants

# config.json keys

SOUND_KITS = "soundKits"
MODE = "mode"

# Sound Kit Options
ROLAND_TR_808 = "rolandTR808"

# For Sample Mode
SAMPLE_MODE = "SAMPLE"
ROOT_PATH = "rootPath"
KEY_SAMPLES = "keySamples"

# Key: Keyboard Input Character, 
# Value: Pygame Constants Numbers
PYGAME_CONST_FOR_CHAR = {
    " " : pygame.K_SPACE,
    "," : pygame.K_COMMA,
    "[" : pygame.K_LEFTBRACKET,
    "]" : pygame.K_RIGHTBRACKET,
    "a" : pygame.K_a,
    "b" : pygame.K_b,
    "c" : pygame.K_c,
    "d" : pygame.K_d,
    "e" : pygame.K_e,
    "f" : pygame.K_f,
    "g" : pygame.K_g,
    "h" : pygame.K_h,
    "i" : pygame.K_i,
    "j" : pygame.K_j,
    "k" : pygame.K_k,
    "l" : pygame.K_l,
    "m" : pygame.K_m,
    "n" : pygame.K_n,
    "o" : pygame.K_o,
    "p" : pygame.K_p,
    "q" : pygame.K_q,
    "r" : pygame.K_r,
    "s" : pygame.K_s,
    "t" : pygame.K_t,
    "u" : pygame.K_u,
    "v" : pygame.K_v,
    "w" : pygame.K_w,
    "x" : pygame.K_x,
    "y" : pygame.K_y,
    "z" : pygame.K_z
}