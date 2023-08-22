
import pygame
import sys

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
LINE_COLOR = (23, 85, 85)

# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
CELL_SIZE = 100

# Initialize screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()

# Variables
player_turn = 'X'
board = [['' for x in range(3)] for y in range(3)]

# Load and scale background image
background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load and scale circle play piece image (O)
o_image = pygame.image.load('o_image.png')
o_image = pygame.transform.scale(o_image, (CELL_SIZE, CELL_SIZE))

# Load and scale the bacon image for the "X" play piece
x_image_path = 'bacon_x_without_checkerboard.png'  # Path to the bacon image
x_image = pygame.image.load(x_image_path)
x_image = pygame.transform.scale(x_image, (CELL_SIZE, CELL_SIZE))

# Draw board function
def draw_board():
    for row in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE * row), (SCREEN_WIDTH, CELL_SIZE * row), 5)
        pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE * row, 0), (CELL_SIZE * row, SCREEN_HEIGHT), 5)

    # Draw board content
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'O':
                screen.blit(o_image, (col * CELL_SIZE, row * CELL_SIZE))

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row, col = x // CELL_SIZE, y // CELL_SIZE
            if board[col][row] == '':
                board[col][row] = 'O' if player_turn == 'O' else 'X'
                player_turn = 'O' if player_turn == 'X' else 'X'

    # Draw everything
    screen.blit(background_image, (0, 0))
    draw_board()
    pygame.display.flip()
    clock.tick(60)
