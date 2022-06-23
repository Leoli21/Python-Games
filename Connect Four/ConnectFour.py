import numpy as np
import pygame
import sys
import math

ROWS = 6
COLS = 7

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def create_board():
    board = np.zeros((ROWS,COLS))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    if board[ROWS-1][col] == 0:
        return True
    return False

def get_next_open_row(board, col):
    for rows in range(ROWS):
        if board[rows][col] == 0:
            return rows

def print_board(board):
   print(np.flipud(board))

def winning_move(board, piece):
    #Check horizontal locations for win
    for col in range(COLS-3):
        for row in range(ROWS):
            if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                return True

    #Check vertical locations for win
    for row in range(ROWS-3):
        for col in range(COLS):
            if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                return True

    #Check positive slope diagonals
    for row in range(ROWS-3):
        for col in range(COLS-3):
            if board[row][col] == piece and board[row + 1][col+1] == piece and board[row + 2][col+2] == piece and board[row + 3][col+3] == piece:
                return True
    #Check negative slope diagonal
    for row in range(3, ROWS):
        for col in range(COLS-3):
            if board[row][col] == piece and board[row - 1][col+1] == piece and board[row - 2][col+2] == piece and board[row- 3][col+3] == piece:
                return True

def draw_board(board):
    for col in range(COLS):
        for row in range(ROWS):
            pygame.draw.rect(screen, BLUE, (col*SQUARESIZE, row * SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(col*SQUARESIZE+SQUARESIZE/2), int(row * SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    for col in range(COLS):
        for row in range(ROWS):
            # Player 1 Occupy
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (int(col * SQUARESIZE + SQUARESIZE / 2), screenHeight - int(row * SQUARESIZE + SQUARESIZE / 2)), RADIUS)

            # Player 2 Occupy
            elif board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW, (int(col * SQUARESIZE + SQUARESIZE / 2), screenHeight - int(row * SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    pygame.display.update()



board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 -5)

screenWidth = COLS * SQUARESIZE
screenHeight = (ROWS + 1) * SQUARESIZE

size = (screenWidth, screenHeight)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
font = pygame.font.SysFont("monospace", 75)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, screenWidth, SQUARESIZE))
            xpos = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (xpos, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (xpos, int(SQUARESIZE / 2)), RADIUS)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, screenWidth, SQUARESIZE))
            #print(event.pos)
            #Player 1 Turn
            if turn == 0:
                xpos = event.pos[0]
                column = int(math.floor(xpos/SQUARESIZE))

                if is_valid_location(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, 1)

                    if winning_move(board, 1):
                        win_label = font.render("Player 1 Wins!", 1, RED)
                        screen.blit(win_label, (40, 10))
                        game_over = True
            #Player 2 Turn
            else:
                xpos = event.pos[0]
                column = int(math.floor(xpos / SQUARESIZE))

                if is_valid_location(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, 2)

                    if winning_move(board, 2):
                        win_label = font.render("Player 2 Wins!", 1, YELLOW)
                        screen.blit(win_label, (40, 10))
                        game_over = True

            print_board(board)
            draw_board(board)
            turn += 1
            turn %= 2

            if game_over:
                pygame.time.wait(3000)

