import pygame
import random

# Initialize the game
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Define the snake's initial position and size
snake_block_size = 20
snake_speed = 15
snake_list = []
snake_length = 1

# Define the food's position and size
food_block_size = 20
food_x = round(random.randrange(0, window_width - food_block_size) / 20) * 20
food_y = round(random.randrange(0, window_height - food_block_size) / 20) * 20

# Define the snake's movement
snake_x = window_width / 2
snake_y = window_height / 2
snake_x_change = 0
snake_y_change = 0

# Define the score
score = 0

# Define the font for the score display
font_style = pygame.font.SysFont(None, 50)

# Function to display the score on the screen
def show_score(score):
    score_text = font_style.render("Score: " + str(score), True, white)
    window.blit(score_text, [10, 10])

# Function to draw the snake on the screen
def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block_size, snake_block_size])

# Main game loop
game_over = False
game_quit = False

while not game_quit:
    while game_over == True:
        # Display game over message and options to play again or quit
        window.fill(black)
        game_over_text = font_style.render("Game Over", True, red)
        window.blit(game_over_text, [window_width / 2 - 100, window_height / 2 - 50])
        show_score(score)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
                game_over = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_quit = True
                    game_over = False
                if event.key == pygame.K_r:
                    game_quit = False
                    game_over = False
                    # Reset the game variables
                    snake_x = window_width / 2
                    snake_y = window_height / 2
                    snake_x_change = 0
                    snake_y_change = 0
                    snake_list = []
                    snake_length = 1
                    score = 0
                    food_x = round(random.randrange(0, window_width - food_block_size) / 20) * 20
                    food_y = round(random.randrange(0, window_height - food_block_size) / 20) * 20

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_block_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_block_size
                snake_x_change = 0

    # Update the snake's position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for collisions with the walls
    if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
        game_over = True

    # Check for collisions with the food
    if snake_x == food_x and snake_y == food_y:
        score += 1
        food_x = round(random.randrange(0, window_width - food_block_size) / 20) * 20
        food_y = round(random.randrange(0, window_height - food_block_size) / 20) * 20
        snake_length += 1

    # Update the game window
    window.fill(black)
    pygame.draw.rect(window, white, [food_x, food_y, food_block_size, food_block_size])
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True

    draw_snake(snake_block_size, snake_list)
    show_score(score)
    pygame.display.update()

    # Set the game speed
    pygame.time.Clock().tick(snake_speed)

# Quit the game
pygame.quit()