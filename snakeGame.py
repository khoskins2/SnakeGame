import pygame
import time
import random

pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#Display
displayWidth = 600
displayHeight = 400
display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Snake Game')

#Clock
clock = pygame.time.Clock()

snakeBlock = 10
snakeSpeed = 15

font_style = pygame.font.SysFont(None, 50)

snake_list = []

#Functions
def snake(snakeBlock, snakeSpeed):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snakeBlock, snakeBlock])

def message(msg, color):
    message = font_style.render(msg, False, color)
    display.blit(msg, [displayWidth/6, displayHeight/3])

def gameLoop():
    gameOver = False
    gameClose = False

    #Initial x and y position of snake head
    x1 = displayWidth / 2
    y1 = displayHeight / 2

    #x and y coords for each movement
    x1Change = 0
    y1Change = 0

    snakeLength = 1

    #Random coords for fruit pieces
    foodx = round(random.randrange(0, displayWidth - snakeBlock) / 10.0) * 10.0
    foody = round(random.randrange(0, displayHeight - snakeBlock) / 10.0) * 10.0

    while not gameOver:
        while gameClose == True:
            display.fill(black)
            message("You lost. Press (Q)uit or (P)lay Again", red)
            snake(snakeBlock, snake_list)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_p:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1Change = -snakeBlock
                    y1Change = 0
                elif event.key == pygame.K_RIGHT:
                    x1Change = snakeBlock
                    y1Change = 0
                elif event.key == pygame.K_UP:
                    x1Change = 0
                    y1Change = -snakeBlock
                elif event.key == pygame.K_DOWN:
                    x1Change = 0
                    y1Change = snakeBlock
        
        if x1 >= displayWidth or x1 < 0 or y1 >= displayHeight or y1 < 0:
            gameClose = True
        x1 += x1Change
        y1 += y1Change
        display.fill(black)
        pygame.draw.rect(display, green, [foodx, foody, snakeBlock, snakeBlock])
        snakeHead = []
        snakeHead.append(x1)
        snakeHead.append(y1)
        snake_list.append(snakeHead)
        if len(snake_list) > snakeLength:
            del snake_list[0]
        
        for x in snake_list[:-1]:
            if x == snakeHead:
                gameClose = True

        snake(snakeBlock, snake_list)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, displayWidth - snakeBlock) / 10.0) * 10.0
            foody = round(random.randrange(0, displayHeight - snakeBlock) / 10.0) * 10.0
            snakeLength += 1

        clock.tick(snakeSpeed)

    pygame.quit()
    quit()

gameLoop()

        