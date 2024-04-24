import pygame
import sys
##Initialize pygame
pygame.init()

# Constants for the board
BOARD_SIZE = 8
CELL_SIZE = 60
WINDOW_SIZE = CELL_SIZE * BOARD_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
LINE_WIDTH = 3  # Width of the lines for the cell outlines

# Set up the display
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("IE 616 Game")

def draw_board():
    colors = [BLUE, ORANGE, PURPLE]
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            color = colors[(row + col) % 3]
            pygame.draw.rect(window, color, (x, y, CELL_SIZE, CELL_SIZE), LINE_WIDTH)

def draw_piece(x, y, color):
    radius = int(CELL_SIZE * 0.4)
    pygame.draw.circle(window, color, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), radius)

def main():
    board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    running = True
    click_count = 0  # Track the number of clicks
    player_turn = 0  # 0 for player 1 (white), 1 for player 2 (black)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                if board[row][col] == 0:  # Place a piece only if the cell is empty
                    board[row][col] = 1 if player_turn == 0 else 2
                    click_count += 1
                    if click_count % 3 == 0:  # Change turn after every 3 clicks
                        player_turn = 1 - player_turn

        window.fill(WHITE)  # Fill the background with white
        draw_board()
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] == 1:
                    draw_piece(col, row, PURPLE)
                elif board[row][col] == 2:
                    draw_piece(col, row, ORANGE)

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


## Start with taking the input of board dimensions.
## Make a menu / sound on off.

## Implement rulesets to the game!!!

## Both player needs to put its first piece to upper-right or lower-left corner.

## New piece should be placed on the board near any same-coloured-piece on the board (diagonals are allowed)
## 3 consecutive plays per each round.

## If a player can't place a piece on the board, the other player wins the game.
## If the board is full, who has the turn loses the game.
