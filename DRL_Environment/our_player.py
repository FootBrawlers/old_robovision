import cv2
import numpy as np
from PIL import Image

class our_player:
    def __init__(self, x = 10, y = 20, player_no = 1):
        self.x = x
        self.y = y
        self.player_no = player_no
    
    def __str__(self):
        return f" Our Player No. {self.player_no}"

    def draw_player(self, img):
        cv2.circle(img, (self.x, self.y), 2, (0,0,255), 2)

    def action(self, choice):
        if(choice == 0):
            # Stay stationary
            self.move(x=0,y=0)
        elif(choice == 1):
            # Move x front
            self.move(x=1,y=0)
        elif(choice == 2):
            # Move y front
            self.move(x=0,y=1)
        elif(choice == 3):
            self.move(x=-1,y=0)
        elif(choice == 4):
            self.move(x=0,y=-1)
        elif(choice == 3):
            # Move diagonally
            self.move(x=1,y=1)

    def move(self, x_mov, y_mov):
        if(can_move(x_mov, y_mov)):
            self.x += x_mov
            self.y += y_mov
        else:
            self.x -= 1
            self.y -= 1

    def can_move(self, x_mov=0, y_mov=0):
        if(self.x + x_mov > ENV_SIZE_X):
            return False
        elif(self.y + y_mov > ENV_SIZE_Y):
            return False
        else:
            return True


def create_our_squad():
    p1 = our_player()
    p2 = our_player(x=30, y=30, player_no=2)
    p3 = our_player(x=150, y=70, player_no=3)
    p4 = our_player(x=380, y=110, player_no=4)
    p5 = our_player(x=10, y=120, player_no=5)
    p6 = our_player(x=550, y=420, player_no=6)

    squad = [p1, p2, p3, p4, p5, p6]
    return squad
