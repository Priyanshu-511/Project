import pygame
import random
import os

# Initialize Pygame
pygame.init()
# Screen dimensions and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Snake settings
SNAKE_BLOCK = 20
SNAKE_SPEED = 15

# Fonts
FONT_STYLE = pygame.font.SysFont("bahnschrift", 25)
SCORE_FONT = pygame.font.SysFont("comicsansms", 35)

# High scores file
HIGH_SCORES_FILE = "high_scores.txt"
TOP_SCORES_COUNT = 5

# Initialize display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Nokia Snake Game')
path = 'project2/Snake/snake_finale.mp3'
print(os.path.exists(path))  # Check if the file exists

if os.path.exists(path):
    pygame.mixer.music.load(path)
else:
    print("File not found at:", path) # Replace with your music file path
pygame.mixer.music.play(-1)  # Loop the music indefinitely


def save_high_score(score, player_name):
    """Saves the high score to the file."""
    high_scores = load_high_scores()
    high_scores.append((score, player_name))
    high_scores.sort(reverse=True, key=lambda x: x[0])  # Sort by score in descending order
    high_scores = high_scores[:TOP_SCORES_COUNT]  # Keep only the top scores
    with open(HIGH_SCORES_FILE, 'w') as file:
        for score, name in high_scores:
            file.write(f"{score},{name}\n")


def load_high_scores():
    """Loads the high scores from the file."""
    if not os.path.exists(HIGH_SCORES_FILE):
        return []
    with open(HIGH_SCORES_FILE, 'r') as file:
        lines = file.readlines()
        return [(int(line.split(',')[0]), line.split(',')[1].strip()) for line in lines]


def display_score(score):
    """Displays the current score."""
    value = SCORE_FONT.render(f"Score: {score}", True, BLUE)
    screen.blit(value, [0, 0])


def draw_snake(snake_block, snake_list):
    """Draws the snake."""
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    """Displays a message on the screen."""
    mesg = FONT_STYLE.render(msg, True, color)
    screen.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])


def game_loop():
    """Main game loop."""
    game_over = False
    game_close = False

    x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    x_change, y_change = 0, 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
    food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK

    clock = pygame.time.Clock()
    score = 0

    while not game_over:
        while game_close:
            screen.fill(WHITE)
            message("You Lost! Press C-Play Again or Q-Quit", RED)
            display_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()  # Restart the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True  # Set game_over to True when window is closed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change, y_change = -SNAKE_BLOCK, 0
                elif event.key == pygame.K_RIGHT:
                    x_change, y_change = SNAKE_BLOCK, 0
                elif event.key == pygame.K_UP:
                    x_change, y_change = 0, -SNAKE_BLOCK
                elif event.key == pygame.K_DOWN:
                    x_change, y_change = 0, SNAKE_BLOCK

        # Snake boundary collision check
        if x >= SCREEN_WIDTH or x < 0 or y >= SCREEN_HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check for self-collision
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_list)
        display_score(score)
        pygame.display.update()

        # Snake eating food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
            food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
            length_of_snake += 1
            score += 10

        clock.tick(SNAKE_SPEED)

    pygame.quit()  # Properly close Pygame
    quit()  # Exit the program

if __name__ == "__main__":
    game_loop()
