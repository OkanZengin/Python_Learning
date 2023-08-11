 # we added some libraries
import time
import pygame as pg
import sys
from pygame.locals import *

# we initialized global variables
XO = 'x'  # this variable is for drawing X and O on to the board.
size = int(input("Please enter size of the board:  "))
row = 0
col = 0
countx = 0
counto = 0
winner = None
width = 500
height = 500
white = (255, 255, 255)
line_color = (10, 10, 10)  # width, height, color of the board and colors of the line on the board.
end_list = []  # we used this list to determine whether game is over or not

TTT = [[None for x in range(size)] for y in range(size)]

# initializing pygame window
pg.init()  # this function safely initializes all imported pygame modules
fps = 30  # this variable determines how fast the game will be
CLOCK = pg.time.Clock()  # this function delays loading of the game opening picture and game board.
screen = pg.display.set_mode((width, height + 100), 0, 32)  # this function determines width and height of the game window
pg.display.set_caption("Tic Tac Toe")  # title of the game window

# loading the images
opening = pg.image.load('tic tac opening.png')
x_img = pg.image.load('x.png')
o_img = pg.image.load('o.png')

# resizing images
x_img = pg.transform.scale(x_img, (width / size, width / size))
o_img = pg.transform.scale(o_img, (width / size, width / size))
opening = pg.transform.scale(opening, (width, height + 100))


def game_opening():
    global winner,countx, counto
    winner = None
    countx = 0
    counto = 0
    screen.blit(opening, (0, 0))  # This function transfers the image of the opening to the app window
    pg.display.update()  # this function updates screen events.
    time.sleep(1)  # before opening game board opening image stays on screen for a second
    screen.fill(white)  # to draw black lines we need white background

    # Drawing vertical lines
    for i in range(1, size):
        pg.draw.line(screen, line_color, (width / size * i, 0), (width / size * i, height), 4)
    for t in range(1, size):
        pg.draw.line(screen, line_color, (0, height / size * t), (width, height / size * t), 4)
    draw_status()  # we need this function in this function because we need the status of the sub text


def draw_status():  # this function control's the subtext and game progress
    global winner, XO, counto, countx
    if winner is None:
        message = "X = " + str(countx) + "  O = " + str(counto) + "|||" + XO.upper() + "'s Turn"
        countx = 0
        counto = 0
    elif winner == "X":
        message = "X = " + str(countx) + "  O = " + str(counto) + " ||| X won. Game will restart in 3 seconds"
        winner = False
    elif winner == "O":
        message = "X = " + str(countx) + "  O = " + str(counto) + " ||| O won. Game will restart in 3 seconds"
        winner = False
    elif winner == "draw":
        message = "X = " + str(countx) + "  O = " + str(counto) + " ||| Game is Draw. Game will restart in 3 seconds"
        winner = False

    font = pg.font.Font(None, 25)  # this function arranges the font of the subtext
    text = font.render(message, True, (255, 255, 255))  # this function arranges subtext's contents and color.

    # copy the rendered message onto the board
    screen.fill((0, 0, 0), (0, 500, 600, 100))
    text_rect = text.get_rect(center=(width / 2, 550))
    screen.blit(text, text_rect)
    pg.display.update()


def check_win():  # this function checks if the XXX or OOO happened in any column or row or diagonally.  If there are, function draws a line on it
    global TTT, winner, size, countx, counto

    for a in range(0, size):
        for b in range(0, size - 2):
            if (TTT[a][b] == TTT[a][b + 1] == TTT[a][b + 2]) and (TTT[a][b] is not None and TTT[a][b] == 'x'):
                pg.draw.line(screen, (250, 0, 0), (b * (width / size), a * height / size + height / (size * 2)),
                             ((b + 3) * (width / size), (a * (height / size) + height / (size * 2))), 2)
                countx += 1
            elif (TTT[a][b] == TTT[a][b + 1] == TTT[a][b + 2]) and (TTT[a][b] is not None and TTT[a][b] == 'o'):
                pg.draw.line(screen, (0, 0, 250), (b * (width / size), a * height / size + height / (size * 2)),
                             ((b + 3) * (width / size), (a * (height / size) + height / (size * 2))), 2)
                counto += 1
    for a in range(0, size - 2):
        for b in range(0, size):
            if (TTT[a][b] == TTT[a + 1][b] == TTT[a + 2][b]) and (TTT[a][b] is not None and TTT[a][b] == 'x'):
                pg.draw.line(screen, (250, 0, 0), ((b * (width / size) + (width / (size * 2))), (a * height / size)),
                             (((b * (width / size)) + width / (size * 2)), ((a + 3) * (height / size))), 2)
                countx += 1
            elif (TTT[a][b] == TTT[a + 1][b] == TTT[a + 2][b]) and (TTT[a][b] is not None and TTT[a][b] == 'o'):
                pg.draw.line(screen, (0, 0, 250), ((b * (width / size) + (width / (size * 2))), (a * height / size)),
                             (((b * (width / size)) + width / (size * 2)), ((a + 3) * (height / size))), 2)
                counto += 1

    for a in range(0, size - 2):
        for b in range(0, size - 2):
            if (TTT[a][b] == TTT[a + 1][b + 1] == TTT[a + 2][b + 2]) and (TTT[a][b] is not None and TTT[a][b] == 'x'):
                pg.draw.line(screen, (250, 0, 0), ((b * width / size), (a * height / size)),
                             (((b + 3) * width / size), ((a + 3) * height / size)), 2)
                countx += 1

            elif (TTT[a][b] == TTT[a + 1][b + 1] == TTT[a + 2][b + 2]) and (TTT[a][b] is not None and TTT[a][b] == 'o'):
                pg.draw.line(screen, (0, 0, 250), ((b * width / size), (a * height / size)),
                             (((b + 3) * width / size), ((a + 3) * height / size)), 2)
                counto += 1

    for a in range(0, size - 2):
        for b in range(2, size):
            if (TTT[a][b] == TTT[a + 1][b - 1] == TTT[a + 2][b - 2]) and (TTT[a][b] is not None and TTT[a][b] == 'x'):
                pg.draw.line(screen, (250, 0, 0), (((b - 2) * width / size), ((a + 3) * height / size)),
                             (((b + 1) * width / size), (a * height / size)), 4)
                countx += 1

            elif (TTT[a][b] == TTT[a + 1][b - 1] == TTT[a + 2][b - 2]) and (TTT[a][b] is not None and TTT[a][b] == 'o'):
                pg.draw.line(screen, (0, 0, 250), (((b - 2) * width / size), ((a + 3) * height / size)),
                             (((b + 1) * width / size), (a * height / size)), 4)
                counto += 1


def check_none():  # This functions checks whether all the squares are filled or not
    global TTT, winner
    winner = None
    for a in range(0, size):
        for b in range(0, size):
            if TTT[a][b] is not None:
                end_list.append(TTT[a][b])
    if len(end_list) == ((size * size) * (size * size + 1)) / 2:
        if countx > counto:
            winner = "X"
        elif counto > countx:
            winner = "O"
        else:
            winner = "draw"


def drawXO():  # This function draws 'x' or 'o' on selected square
    global TTT, XO, row, col
    x, y = pg.mouse.get_pos()
    if x < 500 and y < 500:
        posx = (width / size) * (row - 1)
        posy = (height / size) * (col - 1)

        TTT[row - 1][col - 1] = XO
        if XO == 'x':
            screen.blit(x_img, (posy, posx))
            XO = 'o'
        else:
            screen.blit(o_img, (posy, posx))
            XO = 'x'
        pg.display.update()


def userClick():
    x, y = pg.mouse.get_pos()
    global width, height, row, col
    if x < 500 and y < 500:
        for k in range(0, size):
            if (k * width) / size < x < ((k + 1) * width) / size:
                col = k + 1
        for t in range(0, size):
            if (t * height) / size < y < ((t + 1) * height) / size:
                row = t + 1

    if TTT[row - 1][col - 1] is None:
        global XO
        # This part draws 'x' or 'o' on the board, checks if there is a winning, checks is the board full and changes subtext.
        drawXO()
        check_win()
        check_none()
        draw_status()


def reset_game():  # after the board is full this function resets the game
    global TTT, winner, XO, end_list, counto, countx
    time.sleep(3)
    XO = 'x'
    game_opening()
    winner = None
    TTT = [[None for x in range(size)] for y in range(size)]
    countx = 0
    counto = 0
    end_list = []


game_opening()

# run the game loop forever
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # the user clicked; place an X or O
            userClick()
            if winner is False:
                reset_game()

    pg.display.update()
    CLOCK.tick(fps)
