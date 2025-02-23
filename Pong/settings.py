import pygame


WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
SIZE = {"paddle": (40, 100), "ball": (30,30), 'obstacle': (40, 70)}
SPEED = {"player": 700, "opponent": 450, "ball": 450}

POS = {"player": (WINDOW_WIDTH -50, WINDOW_HEIGHT/2), 
        "opponent": (50, WINDOW_HEIGHT/2)}

COLORS = {
        "paddle": "#ffffff",
        "ball": "#f3d55b",
        "bg": "#26b99a",
        "bg detail": "#81ccab",
        "obs": "#143D60",
}
