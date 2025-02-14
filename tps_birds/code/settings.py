import pygame
import sys, time
from random import randint, choice

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
SCREEN_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
FRAMERATE = 120
ANIMATION_SPEED = 1

pygame.mixer.init()


BACKGROUNDS = {
    'stage 1':"../graphics/backgrounds/1",
    'stage 2':"../graphics/backgrounds/2",
    'stage 3': "../graphics/landscapes/Bg1/Repeated"
}
EFFECTS = {
    'poof': '../graphics/deadSprite'
}

BIRDS = {
    'bird1': "../graphics/birds/Bird01",
    'bird2': "../graphics/birds//Bird02",
    'bird3': "../graphics/birds//Bird03",
    'bird4': "../graphics/birds//Bird04",
    'bird5': "../graphics/birds//Bird05",
    'bird6': "../graphics/birds//Bird06",
    'bird7': "../graphics/birds//Bird07",
    'bird8': "../graphics/birds//Bird08",
    'bird9': "../graphics/birds//Bird09"
}

OBSTACLES = {
    'ob1' : "../graphics/backgrounds/Obstacle1",
    'ob2' : "../graphics/backgrounds/Obstacle2"
}


SOUNDS = {
			'jump': pygame.mixer.Sound("../audio/jump.wav"),
			'music': pygame.mixer.Sound("../audio/music.wav")
		}