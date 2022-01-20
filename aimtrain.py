# Imports
import pygame
import math 
import random

# initialize
pygame.init()
pygame.display.set_caption('Aim trainer')
width = 1200
height = 800
display = pygame.display.set_mode((width, height))
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
score = 0

# Score function
def display_score():
    score_surf = test_font.render(f'Score: {score}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (600,50))
    display.blit(score_surf, score_rect)
    return score

# Colors
black = (0,0,0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
pink = (255, 0 , 127)
white = (255, 255, 255)
orange = (255, 130, 0)
colors = [red, green, blue, yellow, pink, white, orange]

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

# End Game function
def endGame():
    display.fill(black)
    score_surf = test_font.render(f'Score: {score}', False, (200,64,64))
    score_rect = score_surf.get_rect(center = (600,400))
    display.blit(score_surf, score_rect)

# Set Frame Rate
clock = pygame.time.Clock()

# First circle
circles.append(Circle(random.randint(20, width - 20), random.randint(20, height - 20), random.randint(22,25), random.choice(colors)))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Set current circle as first circle in array
    currentCircle = circles[0]

    display_score()

    # Add Circles and draw every second
    frameRate += 1
    if frameRate % 200 == 0:
        circles.append(Circle(random.randint(20, width - 20), random.randint(20, height - 20), random.randint(22,25), random.choice(colors)))

    # Shrink function
    if frameRate % 1 == 0:
        currentCircle.circleWidth -= 0.10
        display.fill(black) # reset screen
        display_score() # display score

    # Draw Shrinking Cirles onto screen
        for i in range(len(circles)):
            circles[i].drawCircle()

    # Shrink next circle
    if len(circles) > 1:
        if frameRate % 1 == 0:
            circles[1].circleWidth -= 0.10


    if currentCircle.circleWidth < 4:
        endGame()

    # Mouse detection 
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    click = pygame.mouse.get_pressed()

    sqx = (x - currentCircle.cx) **2
    sqy = (y - currentCircle.cy) **2
    circleWidth = currentCircle.circleWidth

    # Detect and draw circles
    if math.sqrt(sqx + sqy) < circleWidth and click[0] == 1:
        display.fill(black) # reset screen
        circles.append(Circle(random.randint(20, width - 20), random.randint(20, height - 20), random.randint(22,25), random.choice(colors)))

        # Delete and reset current circle
        del circles[0]
        currentCircle = circles[0]

        # Add and display score
        score  = score + 1
        score = display_score()

    pygame.display.update()
    clock.tick(60)