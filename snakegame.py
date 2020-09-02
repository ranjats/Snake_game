import pygame
import time
import random

# initialize the pygame windows

pygame.init()
clock = pygame.time.Clock()

# Declare the color for user and snake

orangecolor =(255, 123, 7)
blackcolor =(0, 0, 0)
redcolor = (213, 50, 80)
greencolor =(0, 255, 0)
bluecolor =(50, 153, 213)


#Display windows width and height

display_width = 600
display_height = 400

dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Ranjat Srivastava First Game')
snake_block = 10
snake_speed = 10
snake_list = []

# define thr snake structure and position


def snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, orangecolor,[x[0],x[1],snake_block,snake_block])


# Main Function

def snakegame():
    game_over =False
    game_end =False
# co-ordinate the snake
    x1 = display_width / 2
    y1 = display_height / 2
# When Snake move
    x1_change = 0
    y1_change = 0
# Define the snake length
    snake_list = []
    Length_of_snake = 1
# the co-ordinate of the food element
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0)*10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0)* 10.0

    while not game_over:
        while game_end ==True:

            dis.fill(greencolor)
            font_style =pygame.font.SysFont("comicsansms", 20)
            mesg = font_style.render("Sorry Ranjat You Lost the Game!play again? press P", True, blackcolor)
            dis.blit(mesg, [display_width / 6, display_height / 3])

            score = Length_of_snake - 1
            score_font = pygame.font.SysFont("comicsansms", 35)
            value = score_font.render("Your score "+ str(score), True, blackcolor)
            dis.blit(value, [display_width / 3, display_height / 5])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        snakegame()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_end = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over == True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_end = True
# updated the co-ordinate with the changed position
        x1 += x1_change
        y1 += y1_change
        dis.fill(bluecolor)
        pygame.draw.rect(dis, greencolor, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        # if size of snake is greater than width it will stop the game
        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_end =True
        snake(snake_block, snake_list)
        # Whwn snake hits itself , game will ends
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0)*10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()


snakegame()




