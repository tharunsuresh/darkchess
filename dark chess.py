# Tharun's first ever project, developed circa 2015
# Implements a variant of Chinese Chess that I invented in high school using pygame
# See the official handbook PDF for game play rules 
# See the /meta/anacondapackages.txt file for the python environment 

# TO-DO LIST
# 1. Change logic structure from dictionary-based to something more robust
# 2. Recognize game states so it can end game when checkmate/recognize lucky wins

import pygame
import random
import sys
from pygame.locals import *

pygame.init()
MAX_PIXEL_X = 780
MAX_PIXEL_Y = 460
screen = pygame.display.set_mode((MAX_PIXEL_X, MAX_PIXEL_Y))
pygame.display.set_caption('Dark Resistance')

BLACK = (0, 0, 0)
BGCOLOR = (179, 0, 0)
# inside board color is (254,235,206)
BOARDXY = (0, 0)

clock = pygame.time.Clock()
FPS = 30

gamefont = pygame.font.SysFont("abril fatface", 30)


def newgame():
    global BOARDGRID, HIDDEN_PIECE, TURN, BOARD, SELECTION, SELECTION_IMG, CANNON_CAPTURE

    BOARD = pygame.image.load('Images/empty_board.png')
    HIDDEN_PIECE = pygame.image.load('Images/hidden_piece.png')
    SELECTION_IMG = pygame.image.load('Images/selection.png')

    screen.fill(BGCOLOR)
    screen.blit(BOARD, (BOARDXY))

    GRID = PIXELX = PIXELY = 0
    GRID_POS = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4],
                [3, 1], [3, 2], [3, 3], [3, 4], [4, 1], [4, 2], [4, 3], [4, 4],
                [5, 1], [5, 2], [5, 3], [5, 4], [6, 1], [6, 2], [6, 3], [6, 4],
                [7, 1], [7, 2], [7, 3], [7, 4], [8, 1], [8, 2], [8, 3], [8, 4]]

    BOARDGRID = {
        'RP1': ['RED', 'PAWN', GRID, PIXELX, PIXELY, pygame.image.load('Images/red_pawn.png')],
        'RP2': ['RED', 'PAWN', GRID, PIXELX, PIXELY, pygame.image.load('Images/red_pawn.png')],
        'RP3': ['RED', 'PAWN', GRID, PIXELX, PIXELY, pygame.image.load('Images/red_pawn.png')],
        'RP4': ['RED', 'PAWN', GRID, PIXELX, PIXELY, pygame.image.load('Images/red_pawn.png')],
        'RP5': ['RED', 'PAWN', GRID, PIXELX, PIXELY, pygame.image.load('Images/red_pawn.png')],
        'RC1': ['RED', 'CANNON', GRID, PIXELX, PIXELY, pygame.image.load('Images/red_cannon.png')],
        'RC2': ['RED', 'CANNON', GRID, PIXELX, PIXELY, pygame.image.load('Images/red_cannon.png')],
        'RR1': ['RED', 'ROOK', GRID, PIXELX, PIXELY, pygame.image.load('Images/red_rook.png')],
        'RH1': ['RED', 'HORSE', GRID, PIXELX, PIXELY, pygame.image.load('Images/red_horse.png')],
        'RE1': ['RED', 'ELEPHANT', GRID, PIXELX, PIXELY, pygame.image.load('Images/red_elephant.png')],
        'RG1': ['RED', 'GUARDIAN', GRID, PIXELX, PIXELY, pygame.image.load('Images/red_guardian.png')],
        'RK': ['RED', 'KING', GRID, PIXELX, PIXELY, pygame.image.load('Images/red_king.png')],
        'RG2': ['RED', 'GUARDIAN', GRID, PIXELX, PIXELY, pygame.image.load('Images/red_guardian.png')],
        'RE2': ['RED', 'ELEPHANT', GRID, PIXELX, PIXELY, pygame.image.load('Images/red_elephant.png')],
        'RH2': ['RED', 'HORSE', GRID, PIXELX, PIXELY, pygame.image.load('Images/red_horse.png')],
        'RR2': ['RED', 'ROOK', GRID, PIXELX, PIXELY, pygame.image.load('Images/red_rook.png')],
        'BP1': ['BLACK', 'PAWN', GRID, PIXELX, PIXELY, pygame.image.load('Images/black_pawn.png')],
        'BP2': ['BLACK', 'PAWN', GRID, PIXELX, PIXELY, pygame.image.load('Images/black_pawn.png')],
        'BP3': ['BLACK', 'PAWN', GRID, PIXELX, PIXELY, pygame.image.load('Images/black_pawn.png')],
        'BP4': ['BLACK', 'PAWN', GRID, PIXELX, PIXELY, pygame.image.load('Images/black_pawn.png')],
        'BP5': ['BLACK', 'PAWN', GRID, PIXELX, PIXELY, pygame.image.load('Images/black_pawn.png')],
        'BC1': ['BLACK', 'CANNON', GRID, PIXELX, PIXELY, pygame.image.load('Images/black_cannon.png')],
        'BC2': ['BLACK', 'CANNON', GRID, PIXELX, PIXELY, pygame.image.load('Images/black_cannon.png')],
        'BR1': ['BLACK', 'ROOK', GRID, PIXELX, PIXELY, pygame.image.load('Images/black_rook.png')],
        'BH1': ['BLACK', 'HORSE', GRID, PIXELX, PIXELY, pygame.image.load('Images/black_horse.png')],
        'BE1': ['BLACK', 'ELEPHANT', GRID, PIXELX, PIXELY, pygame.image.load('Images/black_elephant.png')],
        'BG1': ['BLACK', 'GUARDIAN', GRID, PIXELX, PIXELY, pygame.image.load('Images/black_guardian.png')],
        'BK': ['BLACK', 'KING', GRID, PIXELX, PIXELY, pygame.image.load('Images/black_king.png')],
        'BG2': ['BLACK', 'GUARDIAN', GRID, PIXELX, PIXELY, pygame.image.load('Images/black_guardian.png')],
        'BE2': ['BLACK', 'ELEPHANT', GRID, PIXELX, PIXELY, pygame.image.load('Images/black_elephant.png')],
        'BH2': ['BLACK', 'HORSE', GRID, PIXELX, PIXELY, pygame.image.load('Images/black_horse.png')],
        'BR2': ['BLACK', 'ROOK', GRID, PIXELX, PIXELY, pygame.image.load('Images/black_rook.png')],
    }

    for i in BOARDGRID:
        BOARDGRID[i][2] = GRID_POS.pop(GRID_POS.index(random.choice(GRID_POS)))
        BOARDGRID[i][3] = 77.5 + (BOARDGRID[i][2][0] - 1) * 80
        BOARDGRID[i][4] = 77.5 + (BOARDGRID[i][2][1] - 1) * 80
        BOARDGRID[i].append(0)  # [i][6] 0 if piece is to be hidden, 1 to show the piece

    TURN = 0
    SELECTION = None
    CANNON_CAPTURE = False


def refresh_pieces_hiddenorshown():
    for i in BOARDGRID:
        if BOARDGRID[i][6] == 0:  # if piece is hidden or revealed
            screen.blit(HIDDEN_PIECE, (BOARDGRID[i][3], BOARDGRID[i][4]))
        elif BOARDGRID[i][6] == 1:
            screen.blit(BOARDGRID[i][5], (BOARDGRID[i][3], BOARDGRID[i][4]))
    if SELECTION != None:
        screen.blit(SELECTION_IMG, (SELECTION[3] - 7.5, SELECTION[4] - 7.5))


def check_hierarchy(OFFENSE, NOTOFFENSE):
    if OFFENSE != None and NOTOFFENSE == None:
        return True
    elif NOTOFFENSE == False:
        return False
    elif OFFENSE[1] == 'ROOK':
        if NOTOFFENSE[1] == 'ROOK' or NOTOFFENSE[1] == 'PAWN' or NOTOFFENSE[1] == 'CANNON':
            return True
        else:
            return False
    elif OFFENSE[1] == 'HORSE':
        if NOTOFFENSE[1] == 'HORSE' or NOTOFFENSE[1] == 'ROOK' or NOTOFFENSE[1] == 'PAWN' or NOTOFFENSE[1] == 'CANNON':
            return True
        else:
            return False
    elif OFFENSE[1] == 'ELEPHANT':
        if NOTOFFENSE[1] == 'ELEPHANT' or NOTOFFENSE[1] == 'HORSE' or NOTOFFENSE[1] == 'ROOK' or NOTOFFENSE[
            1] == 'PAWN' or NOTOFFENSE[1] == 'CANNON':
            return True
        else:
            return False
    elif OFFENSE[1] == 'GUARDIAN' or ATTACKER[1] == 'CANNON':
        if NOTOFFENSE[1] == 'GUARDIAN' or NOTOFFENSE[1] == 'ELEPHANT' or NOTOFFENSE[1] == 'HORSE' or NOTOFFENSE[
            1] == 'ROOK' or NOTOFFENSE[1] == 'PAWN' or NOTOFFENSE[1] == 'CANNON':
            return True
        else:
            return False
    elif OFFENSE[1] == 'KING':
        if NOTOFFENSE[1] == 'GUARDIAN' or NOTOFFENSE[1] == 'ELEPHANT' or NOTOFFENSE[1] == 'HORSE' or NOTOFFENSE[
            1] == 'ROOK' or NOTOFFENSE[1] == 'CANNON':
            return True
        else:
            return False
    elif OFFENSE[1] == 'PAWN':
        if NOTOFFENSE[1] == 'PAWN' or NOTOFFENSE[1] == 'KING':
            return True
        else:
            return False


def capture():
    global TURN, SELECTION, ATTACKER, DEFENDER

    if DEFENDER != None:
        ATTACKER[2] = DEFENDER[2]
        BOARDGRID.pop(list(BOARDGRID.keys())[list(BOARDGRID.values()).index(DEFENDER)])
        ATTACKER[3] = 77.5 + (ATTACKER[2][0] - 1) * 80
        ATTACKER[4] = 77.5 + (ATTACKER[2][1] - 1) * 80
        TURN += 1
        SELECTION = None


def regular_move():
    global SELECTION, TURN, ATTACKER, DEFENDER

    if event.key == K_LEFT or event.key == K_a:
        for i in BOARDGRID:
            if BOARDGRID[i][2] == [SELECTION[2][0] - 1, SELECTION[2][1]]:  # if piece to the left
                if BOARDGRID[i][0] != ATTACKER[0] and BOARDGRID[i][
                    6] == 1:  # checks if enemy and that piece has been revealed already
                    DEFENDER = BOARDGRID[i]
                elif BOARDGRID[i][0] == ATTACKER[0] or BOARDGRID[i][6] == 0:
                    DEFENDER = False
        if check_hierarchy(ATTACKER, DEFENDER):
            capture()
            if DEFENDER == None:
                if ATTACKER[2][0] > 1:
                    ATTACKER[2][0] = ATTACKER[2][0] - 1
                    ATTACKER[3] = 77.5 + (ATTACKER[2][0] - 1) * 80
                    TURN += 1
                    SELECTION = None
    elif event.key == K_UP or event.key == K_w:
        for i in BOARDGRID:
            if BOARDGRID[i][2] == [SELECTION[2][0], SELECTION[2][1] - 1]:
                if BOARDGRID[i][0] != ATTACKER[0] and BOARDGRID[i][6] == 1:
                    DEFENDER = BOARDGRID[i]
                elif BOARDGRID[i][0] == ATTACKER[0] or BOARDGRID[i][6] == 0:
                    DEFENDER = False
        if check_hierarchy(ATTACKER, DEFENDER):
            capture()
            if DEFENDER == None:  # moves up
                if ATTACKER[2][1] > 1:
                    ATTACKER[2][1] = ATTACKER[2][1] - 1
                    ATTACKER[4] = 77.5 + (ATTACKER[2][1] - 1) * 80
                    TURN += 1
                    SELECTION = None
    elif event.key == K_RIGHT or event.key == K_d:
        for i in BOARDGRID:
            if BOARDGRID[i][2] == [SELECTION[2][0] + 1, SELECTION[2][1]]:  # if piece to the left
                if BOARDGRID[i][0] != ATTACKER[0] and BOARDGRID[i][6]:
                    # checks if enemy and that piece has been revealed already
                    DEFENDER = BOARDGRID[i]
                elif BOARDGRID[i][0] == ATTACKER[0] or BOARDGRID[i][6] == 0:
                    DEFENDER = False
        if check_hierarchy(ATTACKER, DEFENDER):
            capture()
            if DEFENDER == None:  # moves left
                if ATTACKER[2][0] < 8:
                    ATTACKER[2][0] = ATTACKER[2][0] + 1
                    ATTACKER[3] = 77.5 + (ATTACKER[2][0] - 1) * 80
                    TURN += 1
                    SELECTION = None
    elif event.key == K_DOWN or event.key == K_s:
        for i in BOARDGRID:
            if BOARDGRID[i][2] == [SELECTION[2][0], SELECTION[2][1] + 1]:
                if BOARDGRID[i][0] != ATTACKER[0] and BOARDGRID[i][6] == 1:
                    DEFENDER = BOARDGRID[i]
                elif BOARDGRID[i][0] == ATTACKER[0] or BOARDGRID[i][6] == 0:
                    DEFENDER = False
        if check_hierarchy(ATTACKER, DEFENDER):
            capture()
            if DEFENDER == None:  # moves up
                if ATTACKER[2][1] < 4:
                    ATTACKER[2][1] = ATTACKER[2][1] + 1
                    ATTACKER[4] = 77.5 + (ATTACKER[2][1] - 1) * 80
                    TURN += 1
                    SELECTION = None


def cannon_capture():
    global SELECTION, ATTACKER, DEFENDER

    if event.key == K_LEFT or event.key == K_a:
        for i in BOARDGRID:
            if BOARDGRID[i][2] == [SELECTION[2][0] - 2, SELECTION[2][1]]:  # if there is a piece 2 to the left
                for j in BOARDGRID:
                    if BOARDGRID[j][2] == [SELECTION[2][0] - 1, SELECTION[2][1]]:  # if there is a piece in the middle
                        if BOARDGRID[i][0] != ATTACKER[0] and BOARDGRID[i][6]:
                            # checks if enemy and that piece has been revealed already
                            DEFENDER = BOARDGRID[i]
        if check_hierarchy(ATTACKER, DEFENDER):
            capture()
    elif event.key == K_UP or event.key == K_w:
        for i in BOARDGRID:
            if BOARDGRID[i][2] == [SELECTION[2][0], SELECTION[2][1] - 2]:
                for j in BOARDGRID:
                    if BOARDGRID[j][2] == [SELECTION[2][0], SELECTION[2][1] - 1]:  # if there is a piece in the middle
                        if BOARDGRID[i][0] != ATTACKER[0] and BOARDGRID[i][
                            6]:  # checks if enemy and that piece has been revealed already
                            DEFENDER = BOARDGRID[i]
        if check_hierarchy(ATTACKER, DEFENDER):
            capture()
    elif event.key == K_RIGHT or event.key == K_d:
        for i in BOARDGRID:
            if BOARDGRID[i][2] == [SELECTION[2][0] + 2, SELECTION[2][1]]:
                for j in BOARDGRID:
                    if BOARDGRID[j][2] == [SELECTION[2][0] + 1, SELECTION[2][1]]:  # if there is a piece in the middle
                        if BOARDGRID[i][0] != ATTACKER[0] and BOARDGRID[i][
                            6] == 1:  # checks if enemy and that piece has been revealed already
                            DEFENDER = BOARDGRID[i]
        if check_hierarchy(ATTACKER, DEFENDER):
            capture()
    elif event.key == K_DOWN or event.key == K_s:
        for i in BOARDGRID:
            if BOARDGRID[i][2] == [SELECTION[2][0], SELECTION[2][1] + 2]:
                for j in BOARDGRID:
                    if BOARDGRID[j][2] == [SELECTION[2][0], SELECTION[2][1] + 1]:  # if there is a piece in the middle
                        if BOARDGRID[i][0] != ATTACKER[0] and BOARDGRID[i][6]:
                            # checks if enemy and that piece has been revealed already
                            DEFENDER = BOARDGRID[i]
        if check_hierarchy(ATTACKER, DEFENDER):
            capture()


def cannon_move():
    global SELECTION, ATTACKER, DEFENDER, TURN

    if event.key == K_LEFT or event.key == K_a:
        for i in BOARDGRID:
            if BOARDGRID[i][2] == [SELECTION[2][0] - 1, SELECTION[2][1]]:  # if piece to the left
                if BOARDGRID[i][0] != ATTACKER[0] and BOARDGRID[i][6]:
                    # checks if enemy and that piece has been revealed already
                    DEFENDER = BOARDGRID[i]
                elif BOARDGRID[i][0] == ATTACKER[0] or BOARDGRID[i][6] == 0:
                    DEFENDER = False
        if check_hierarchy(ATTACKER, DEFENDER):
            if DEFENDER == None:
                if ATTACKER[2][0] > 1:
                    ATTACKER[2][0] = ATTACKER[2][0] - 1
                    ATTACKER[3] = 77.5 + (ATTACKER[2][0] - 1) * 80
                    TURN += 1
                    SELECTION = None
    elif event.key == K_UP or event.key == K_w:
        for i in BOARDGRID:
            if BOARDGRID[i][2] == [SELECTION[2][0], SELECTION[2][1] - 1]:
                if BOARDGRID[i][0] != ATTACKER[0] and BOARDGRID[i][6] == 1:
                    DEFENDER = BOARDGRID[i]
                elif BOARDGRID[i][0] == ATTACKER[0] or BOARDGRID[i][6] == 0:
                    DEFENDER = False
        if check_hierarchy(ATTACKER, DEFENDER):
            if DEFENDER == None:  # moves up
                if ATTACKER[2][1] > 1:
                    ATTACKER[2][1] = ATTACKER[2][1] - 1
                    ATTACKER[4] = 77.5 + (ATTACKER[2][1] - 1) * 80
                    TURN += 1
                    SELECTION = None
    elif event.key == K_RIGHT or event.key == K_d:
        for i in BOARDGRID:
            if BOARDGRID[i][2] == [SELECTION[2][0] + 1, SELECTION[2][1]]:  # if piece to the left
                if BOARDGRID[i][0] != ATTACKER[0] and BOARDGRID[i][6]:
                    # checks if enemy and that piece has been revealed already
                    DEFENDER = BOARDGRID[i]
                elif BOARDGRID[i][0] == ATTACKER[0] or BOARDGRID[i][6] == 0:
                    DEFENDER = False
        if check_hierarchy(ATTACKER, DEFENDER):
            if DEFENDER == None:  # moves left
                if ATTACKER[2][0] < 8:
                    ATTACKER[2][0] = ATTACKER[2][0] + 1
                    ATTACKER[3] = 77.5 + (ATTACKER[2][0] - 1) * 80
                    TURN += 1
                    SELECTION = None
    elif event.key == K_DOWN or event.key == K_s:
        for i in BOARDGRID:
            if BOARDGRID[i][2] == [SELECTION[2][0], SELECTION[2][1] + 1]:
                if BOARDGRID[i][0] != ATTACKER[0] and BOARDGRID[i][6] == 1:
                    DEFENDER = BOARDGRID[i]
                elif BOARDGRID[i][0] == ATTACKER[0] or BOARDGRID[i][6] == 0:
                    DEFENDER = False
        if check_hierarchy(ATTACKER, DEFENDER):
            if DEFENDER == None:  # moves up
                if ATTACKER[2][1] < 4:
                    ATTACKER[2][1] = ATTACKER[2][1] + 1
                    ATTACKER[4] = 77.5 + (ATTACKER[2][1] - 1) * 80
                    TURN += 1
                    SELECTION = None


def game_play():
    global TURN, PLAYER_1, PLAYER_2, ATTACKER, DEFENDER, SELECTION, CANNON_CAPTURE

    ATTACKER = DEFENDER = None

    if event.type == MOUSEBUTTONDOWN:
        mousexy = pygame.mouse.get_pos()
        for i in BOARDGRID:
            if mousexy[0] in range(int(BOARDGRID[i][3]), int(BOARDGRID[i][3] + 65)) and mousexy[1] in range(
                    int(BOARDGRID[i][4]), int(BOARDGRID[i][4] + 65)):
                if BOARDGRID[i][6] == 0:  # revealing the piece, consumes a turn
                    BOARDGRID[i][6] = 1
                    TURN += 1
                    if TURN == 1:
                        PLAYER_1 = BOARDGRID[i][0]
                        if PLAYER_1 == 'BLACK':
                            PLAYER_2 = 'RED'
                        elif PLAYER_1 == 'RED':
                            PLAYER_2 = 'BLACK'
                elif BOARDGRID[i][6] == 1 and SELECTION is None:  # selecting and using it for movement
                    if (TURN % 2 == 1 and BOARDGRID[i][0] == PLAYER_2) or (
                            TURN % 2 == 0 and BOARDGRID[i][0] == PLAYER_1):
                        SELECTION = BOARDGRID[i]
                elif BOARDGRID[i][6] == 1 and SELECTION is not None:  # deselecting
                    SELECTION = None
    if event.type == KEYDOWN:
        ATTACKER = SELECTION
        if SELECTION is None:
            pass
        elif SELECTION[1] != 'CANNON':
            regular_move()
            CANNON_CAPTURE = False
        elif SELECTION[1] == 'CANNON':
            if event.key == K_c:
                CANNON_CAPTURE = True
            else:
                if CANNON_CAPTURE:
                    cannon_capture()
                    CANNON_CAPTURE = False
                else:
                    cannon_move()


def turn_display():
    if TURN > 0:
        PLAYER_1_TEXT = gamefont.render(PLAYER_1 + '\'S TURN', 0, BLACK)
        PLAYER_2_TEXT = gamefont.render(PLAYER_2 + '\'S TURN', 0, BLACK)
        if TURN % 2 == 0:
            screen.blit(PLAYER_1_TEXT, (5, MAX_PIXEL_Y - 30))
        elif TURN % 2 == 1:
            screen.blit(PLAYER_2_TEXT, (5, MAX_PIXEL_Y - 30))


def check_if_quit():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()


def refresh():
    clock.tick(FPS)
    pygame.display.update()
    screen.fill(BLACK)
    screen.fill(BGCOLOR)
    screen.blit(BOARD, BOARDXY)


newgame()
while True:
    refresh_pieces_hiddenorshown()
    for event in pygame.event.get():
        check_if_quit()
        game_play()
    turn_display()
    refresh()
