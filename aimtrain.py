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
display.fill((200,200,200))
font = pygame.font.Font('font/Pixeltype.ttf', 50)
bigfont = pygame.font.Font('font/Pixeltype.ttf', 150)
score = 0
shrinkRate = None
gameactive = False

# Button class
class Button():

    # Initialize class
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    # draw button method
    def draw(self, display, outline = None):
        if outline:
            pygame.draw.rect(display, self.color, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            text = font.render(self.text, 1, (0,0,0))
            display.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    # Mouse position
    def hover(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

# Update window
def window():
    display.fill((0,0,0))
    easybutton.draw(display, (255,255,255))
    hardbutton.draw(display, (255,255,255))
    main_surf = bigfont.render('MAIN MENU', False, (64,64,64))
    main_rect = main_surf.get_rect(center = (600,100))
    display.blit(main_surf, main_rect)

# Create buttons
easybutton = Button((32,32,32), 500, 250, 250, 100, 'Easy')
hardbutton = Button((32,32,32), 500, 500, 250, 100, 'Hard') 

def easymode():
    global shrinkRate
    shrinkRate = 0.08

def hardmode():
    global shrinkRate
    shrinkRate = 0.15

# Main Menu Function
def main():
    global gameactive, score
    score = 0
    loop = True

    while loop:
        window()
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if easybutton.hover(pos):
                    easymode()
                    loop = False
                    gameactive = True

                elif hardbutton.hover(pos):
                    hardmode()
                    loop = False
                    gameactive = True

            if event.type == pygame.MOUSEMOTION:
                if easybutton.hover(pos):
                    easybutton.color = (32,32,32)
                else:
                    easybutton.color = (64,64,64)
            
            if event.type == pygame.MOUSEMOTION:
                if hardbutton.hover(pos):
                    hardbutton.color = (32,32,32)
                else:
                    hardbutton.color = (64,64,64)
            
main()

# Score function
def display_score():
    score_surf = font.render(f'Score: {score}', False, (75,75,75))
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
    score_surf = font.render(f'Score: {score}', False, (200,64,64))
    score_rect = score_surf.get_rect(center = (600,400))
    display.blit(score_surf, score_rect)
    over_surf = bigfont.render('GAME OVER', False, (200,64,64))
    over_rect = over_surf.get_rect(center = (600,300))
    display.blit(over_surf, over_rect)
    restart_surf = font.render('Tap anywhere to continue', False, (200,64,64))
    restart_rect = restart_surf.get_rect(center = (600,500))
    display.blit(restart_surf, restart_rect)

    click = pygame.mouse.get_pressed()
    if click[0] == 1:
        display.fill(black)
        main()


# Set Frame Rate
clock = pygame.time.Clock()

# First circle
circles.append(Circle(random.randint(20, width - 20), random.randint(20, height - 20), random.randint(22,25), random.choice(colors)))

# Game loop
while gameactive:
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
        currentCircle.circleWidth -= shrinkRate
        display.fill(black) # reset screen
        display_score() # display score

    # Draw Shrinking Cirles onto screen
        for i in range(len(circles)):
            circles[i].drawCircle()

    # Shrink next circle
    if len(circles) > 1:
        if frameRate % 1 == 0:
            circles[1].circleWidth -= 0.10

    # End game
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