# Imports
from hashlib import blake2b
import pygame
import math 
import random

# initialize
pygame.init()
pygame.display.set_caption('Aim trainer')
width = 1200
height = 800
screen = display = pygame.display.set_mode((width, height))
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
score = 0

# Score function
def display_score():
    score_surf = test_font.render(f'Score: {score}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (600,50))
    screen.blit(score_surf, score_rect)
    return score

# Colors
black = (0,0,0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (85, 206, 255)
colors = [red, green, blue]

# Set Frame Rate
clock = pygame.time.Clock()

cx = random.randint(20, width - 20)
cy = random.randint(20, height - 20)
circleWidth = random.randint(14,20)
pygame.draw.circle(display, random.choice(colors), (cx, cy), circleWidth)

# Easy loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    click = pygame.mouse.get_pressed()

    sqx = (x - cx) **2
    sqy = (y -cy) **2

    if math.sqrt(sqx + sqy) < circleWidth and click[0] == 1:
        display.fill(black) # reset screen
        cx = random.randint(20, width - 20)
        cy = random.randint(20, height - 20)
        circleWidth = random.randint(14,20)
        pygame.draw.circle(display, random.choice(colors), (cx, cy), circleWidth)
        score  = score + 1
        score = display_score()

    pygame.display.update()
    clock.tick(60)