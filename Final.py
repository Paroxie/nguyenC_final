import pygame 
import random


pygame.init()


# Display (test background)
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Final Project")

Pink = (255, 182, 193)
Blue = (173, 216, 230)
White = (255, 255, 255)


class sparkles:
    def __init__(self, x, y, size): 
        self.x = x
        self.y = y
        self.size = size
        self.alpha = random.randint(100, 255)  #
        self.alpha_direction = random.choice([-1, 1])  # Fade in or out
        self.max_alpha = 255
        self.min_alpha = 50

    def update(self):