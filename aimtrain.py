# Imports
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

circles = []
currentCircle = None
frameRate = 0

class Circle:
    def __init__(self, cx, cy, circleWidth, color) :

        self.cx = cx
        self.cy = cy
        self.circleWidth = circleWidth
        self.color = color

    def drawCircle(self):
        pygame.draw.circle(display, self.color, (self.cx, self.cy), self.circleWidth)



# Set Frame Rate
clock = pygame.time.Clock()

# First circle
circles.append(Circle(random.randint(20, width - 20), random.randint(20, height - 20), random.randint(14,20), random.choice(colors)))

# Easy loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Add Circles and draw every second
    frameRate += 1
    if frameRate% 60 == 0:
        circles.append(Circle(random.randint(20, width - 20), random.randint(20, height - 20), random.randint(14,20), random.choice(colors)))
    for i in range(len(circles)):
        circles[i].drawCircle()

    # Set current circle as first circle in array
    currentCircle = circles[0]

    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    click = pygame.mouse.get_pressed()

    sqx = (x - currentCircle.cx) **2
    sqy = (y - currentCircle.cy) **2
    circleWidth = currentCircle.circleWidth

    # Detect and draw circles
    if math.sqrt(sqx + sqy) < circleWidth and click[0] == 1:
        display.fill(black) # reset screen
        del circles[0]
        score  = score + 1
        score = display_score()

    pygame.display.update()
    clock.tick(60)