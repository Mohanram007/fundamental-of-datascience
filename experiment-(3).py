import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Snake initial position and properties
block_size = 20
snake_speed = 15
font_style = pygame.font.SysFont(None, 50)

# Function to draw snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, BLACK, [x[0], x[1], snake_block, snake_block])

# Function to display message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [WIDTH/4, HEIGHT/4])

# Main function
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of snake
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    # Initial change in position
    x1_change = 0
    y1_change = 0

    # Initial snake length
    snake_list = []
    length_of_snake = 1

    # Initial position of food
    foodx = round(random.randrange(0, WIDTH - block_size) / 20.0) * 20
    foody = round(random.randrange(0, HEIGHT - block_size) / 20.0) * 20

    # Game loop
    while not game_over:
        while game_close == True:
            win.fill(WHITE)
            message("You lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Update snake position
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        win.fill(WHITE)
        pygame.draw.rect(win, RED, [foodx, foody, block_size, block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Snake collides with itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw snake
        draw_snake(block_size, snake_list)

        # Update display
        pygame.display.update()

        # Snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - block_size) / 20.0) * 20
            foody = round(random.randrange(0, HEIGHT - block_size) / 20.0) * 20
            length_of_snake += 1

        # Set snake speed
        clock.tick(snake_speed)

    # Quit pygame
    pygame.quit()
    quit()

# Start the game
gameLoop()
