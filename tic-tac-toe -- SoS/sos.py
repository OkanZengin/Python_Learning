# we added some libraries
import time

import pygame
import pygame as pg
import sys
from pygame.locals import *

# we initialized global variables
SO = 'S'  # this variable is for drawing S and O on to the board.
size = int(input("Please enter size of the board:  "))
row = 0
col = 0
indexrow = 0
indexcol = 0
countp_1 = 0
countp_2 = 0
turn = "Player 1"
previous_p_1 = 0
previous_p_2 = 0
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
screen = pg.display.set_mode((width, height + 100), 0,
                             32)  # this function determines width and height of the game window
pg.display.set_caption("Tic Tac Toe")  # title of the game window

# loading the images
opening = pg.image.load('tic tac opening.png')
s_img = pg.image.load('s.png')
o_img = pg.image.load('o.png')
s_button = pg.image.load('s_button.png').convert_alpha()
o_button = pg.image.load('o_button.png').convert_alpha()
reset_button = pg.image.load('reset_button.png').convert_alpha()

# resizing images
s_img = pg.transform.scale(s_img, (width / size, width / size))
o_img = pg.transform.scale(o_img, (width / size, width / size))
s_button = pg.transform.scale(s_button, (50, 50))
o_button = pg.transform.scale(o_button, (50, 50))
reset_button = pg.transform.scale(reset_button, (120, 50))
opening = pg.transform.scale(opening, (width, height + 100))


class Button():
    def __init__(self, x, y, image, scale):
        width_img = image.get_width()
        height_img = image.get_height()
        self.image = pygame.transform.scale(image, (int(width_img * scale), int(height_img * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


s_button = Button(50, 550, s_button,0.8)
o_button = Button(450, 550, o_button,0.8)
reset_button = Button(350,575,reset_button,0.8)


def buttons():
    global SO, winner
    if s_button.draw(screen):
        SO = "S"
    if o_button.draw(screen):
        SO = "O"
    if reset_button.draw(screen):
        winner = "reset"
        draw_status()
        reset_game()


def game_opening():
    global winner, countp_1, countp_2
    winner = None
    countp_1 = 0
    countp_2 = 0
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
    buttons()


def draw_status():  # this function control's the subtext and game progress
    global winner, countp_1, countp_2, previous_p_1, previous_p_2, SO
    if winner is None:
        message = "Player 1 = " + str(countp_1) + "  Player 2 = " + str(countp_2) + "|||" + turn + "'s Turn"
        message2 = ""
    elif winner == "Player 1":
        message = "Player 1 = " + str(previous_p_1) + "  Player 2 = " + str(previous_p_2)
        message2 = "Player 1 won. Game will restart in 3 seconds"
        winner = False
    elif winner == "Player 2":
        message = "Player 1 = " + str(previous_p_1) + "  Player 2 = " + str(previous_p_2)
        message2 = "Player 2 won. Game will restart in 3 seconds"
        winner = False
    elif winner == "draw":
        message = "Player 1 = " + str(countp_1) + "  Player 2 = " + str(countp_2)
        message2 = " Game is Draw. Game will restart in 3 seconds"
        winner = False
    elif winner == "reset":
        message = "Oyun yeniden başlatılıyor."
        message2= ""
        winner = False

    font = pg.font.Font(None, 25)  # this function arranges the font of the subtext
    texta = font.render(message, True, (255, 255, 255))  # this function arranges subtext's contents and color.
    textb = font.render(message2, True, (255, 255, 255))
    # copy the rendered message onto the board
    screen.fill((0, 0, 0), (0, 500, 600, 100))
    texta_rect = texta.get_rect(center=(width / 2, 550))
    textb_rect = textb.get_rect(center=(width / 2, 570))
    screen.blit(texta, texta_rect)
    screen.blit(textb, textb_rect)
    pg.display.update()


def check_win_h():
    global TTT, winner, size, countp_1, countp_2, indexrow, indexcol, turn
    if turn == "Player 1":
        for a in range(0, size):
            for b in range(0, size - 2):
                if a == indexrow and b == indexcol or a == indexrow and b+1 == indexcol or a == indexrow and b+2 == indexcol:
                    if (TTT[a][b] == TTT[a][b + 2]) and (TTT[a][b] != TTT[a][b + 1]) and (
                            TTT[a][b] and TTT[a][b + 1] is not None and TTT[a][b] == 'S'):
                        pg.draw.line(screen, (250, 0, 0),
                                     (b * (width / size), a * height / size + height / (size * 2)),
                                     ((b + 3) * (width / size), (a * (height / size) + height / (size * 2))), 2)
                        countp_1 += 1
    elif turn == "Player 2":
        for a in range(0, size):
            for b in range(0, size - 2):
                if a == indexrow and b == indexcol or a == indexrow and b+1 == indexcol or a == indexrow and b+2 == indexcol:
                    if (TTT[a][b] == TTT[a][b + 2]) and (TTT[a][b] != TTT[a][b + 1]) and (
                            TTT[a][b] and TTT[a][b + 1] is not None and TTT[a][b] == 'S'):
                        pg.draw.line(screen, (0, 0, 250), (b * (width / size), a * height / size + height / (size * 2)),
                                     ((b + 3) * (width / size), (a * (height / size) + height / (size * 2))), 2)
                        countp_2 += 1


def check_win_v():
    global TTT, winner, size, countp_1, countp_2, indexrow, indexcol, turn
    if turn == "Player 1":
        for a in range(0, size - 2):
            for b in range(0, size):
                if a == indexrow and b == indexcol or a+1 == indexrow and b == indexcol or a+2 == indexrow and b == indexcol:
                    if (TTT[a][b] == TTT[a + 2][b]) and (TTT[a][b] != TTT[a + 1][b]) and (
                            TTT[a][b] and TTT[a + 1][b] is not None and TTT[a][b] == 'S'):
                        pg.draw.line(screen, (250, 0, 0), ((b * (width / size) + (width / (size * 2))), (a * height / size)),
                                     (((b * (width / size)) + width / (size * 2)), ((a + 3) * (height / size))), 2)
                        countp_1 += 1
    elif turn == "Player 2":
        for a in range(0, size - 2):
            for b in range(0, size):
                if a == indexrow and b == indexcol or a+1 == indexrow and b == indexcol or a+2 == indexrow and b == indexcol:
                    if (TTT[a][b] == TTT[a + 2][b]) and (TTT[a][b] != TTT[a + 1][b]) and (
                            TTT[a][b] and TTT[a + 1][b] is not None and TTT[a][b] == 'S'):
                        pg.draw.line(screen, (0, 0, 250), ((b * (width / size) + (width / (size * 2))), (a * height / size)),
                                     (((b * (width / size)) + width / (size * 2)), ((a + 3) * (height / size))), 2)
                        countp_2 += 1


def check_win_rd():
    global TTT, winner, size, countp_1, countp_2, indexrow, indexcol, turn
    if turn == "Player 1":
        for a in range(0, size - 2):
            for b in range(0, size - 2):
                if a == indexrow and b == indexcol or a+1 == indexrow and b + 1 == indexcol or a+2 == indexrow and b + 2 == indexcol:
                    if (TTT[a][b] == TTT[a + 2][b + 2]) and (TTT[a][b] != TTT[a + 1][b + 1]) and (
                            TTT[a][b] and TTT[a + 1][b + 1] is not None and TTT[a][b] == 'S'):
                        pg.draw.line(screen, (250, 0, 0), ((b * width / size), (a * height / size)),
                                     (((b + 3) * width / size), ((a + 3) * height / size)), 2)
                        countp_1 += 1
    elif turn == "Player 2":
        for a in range(0, size - 2):
            for b in range(0, size - 2):
                if a == indexrow and b == indexcol or a+1 == indexrow and b + 1 == indexcol or a+2 == indexrow and b + 2 == indexcol:
                    if (TTT[a][b] == TTT[a + 2][b + 2]) and (TTT[a][b] != TTT[a + 1][b + 1]) and (
                            TTT[a][b] and TTT[a + 1][b + 1] is not None and TTT[a][b] == 'S'):
                        pg.draw.line(screen, (0, 0, 250), ((b * width / size), (a * height / size)),
                                     (((b + 3) * width / size), ((a + 3) * height / size)), 2)
                        countp_2 += 1


def check_win_ld():
    global TTT, winner, size, countp_1, countp_2, indexrow, indexcol, turn
    if turn == "Player 1":
        for a in range(0, size - 2):
            for b in range(2, size):
                if a == indexrow and b == indexcol or a+1 == indexrow and b - 1 == indexcol or a+2 == indexrow and b - 2 == indexcol:
                    if (TTT[a][b] == TTT[a + 2][b - 2]) and (TTT[a][b] != TTT[a + 1][b - 1]) and (
                            TTT[a][b] and TTT[a + 1][b - 1] is not None and TTT[a][b] == 'S'):
                        pg.draw.line(screen, (250, 0, 0), (((b - 2) * width / size), ((a + 3) * height / size)),
                                     (((b + 1) * width / size), (a * height / size)), 4)
                        countp_1 += 1
    elif turn == "Player 2":
        for a in range(0, size - 2):
            for b in range(2, size):
                if a == indexrow and b == indexcol or a+1 == indexrow and b - 1 == indexcol or a+2 == indexrow and b - 2 == indexcol:
                    if (TTT[a][b] == TTT[a + 2][b - 2]) and (TTT[a][b] != TTT[a + 1][b - 1]) and (
                            TTT[a][b] and TTT[a + 1][b - 1] is not None and TTT[a][b] == 'S'):
                        pg.draw.line(screen, (0, 0, 250), (((b - 2) * width / size), ((a + 3) * height / size)),
                                     (((b + 1) * width / size), (a * height / size)), 4)
                        countp_2 += 1


def check_none():  # This functions checks whether all the squares are filled or not
    global TTT, winner, turn, countp_1, previous_p_1, countp_2, previous_p_2
    winner = None
    if turn == "Player 1":
        if countp_1 > previous_p_1:
            previous_p_1 += 1
            for a in range(0, size):
                if countp_1 > previous_p_1:
                    previous_p_1 +=1
                elif countp_1 == previous_p_1:
                    break
        else:
            turn = "Player 2"
    elif turn == "Player 2":
        if countp_2 > previous_p_2:
            previous_p_2 += 1
            for a in range(0, size):
                if countp_2 > previous_p_2:
                    previous_p_2 +=1
                elif countp_2 == previous_p_2:
                    break
        else:
            turn = "Player 1"
    for a in range(0, size):
        for b in range(0, size):
            if TTT[a][b] is not None:
                end_list.append(TTT[a][b])
    if len(end_list) == ((size * size) * (size * size + 1)) / 2:
        if countp_1 > countp_2:
            winner = "Player 1"
        elif countp_2 > countp_1:
            winner = "Player 2"
        else:
            winner = "draw"


def drawXO():  # This function draws 'x' or 'o' on selected square
    global TTT, SO, row, col, turn, countp_1, previous_p_1, countp_2, previous_p_2
    x, y = pg.mouse.get_pos()
    if x < 500 and y < 500:
        posx = (width / size) * (row - 1)
        posy = (height / size) * (col - 1)
        TTT[row - 1][col - 1] = SO
        if SO == "S":
            screen.blit(s_img, (posy, posx))
        elif SO == "O":
            screen.blit(o_img, (posy, posx))
        pg.display.update()
        buttons()

def userClick():
    x, y = pg.mouse.get_pos()
    global width, height, row, col, indexrow, indexcol
    if x < 500 and y < 500:
        for k in range(0, size):
            if (k * width) / size < x < ((k + 1) * width) / size:
                col = k + 1
                indexcol = k
        for t in range(0, size):
            if (t * height) / size < y < ((t + 1) * height) / size:
                row = t + 1
                indexrow = t

    if TTT[row - 1][col - 1] is None:
        global SO, turn
        drawXO()
        check_win_v()
        check_win_h()
        check_win_rd()
        check_win_ld()
        check_none()
        draw_status()
        buttons()


def reset_game():  # after the board is full this function resets the game
    global TTT, winner, SO, end_list, countp_1, countp_2, turn,previous_p_1,previous_p_2
    time.sleep(3)
    SO = 'S'
    turn = "Player 1"

    game_opening()
    winner = None
    TTT = [[None for x in range(size)] for y in range(size)]
    countp_1 = 0
    previous_p_1 = 0
    countp_2 = 0
    previous_p_2 = 0
    end_list = []


game_opening()

# run the game loop forever
while True:
    for event in pg.event.get():
        buttons()
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
