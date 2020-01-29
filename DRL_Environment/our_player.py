import cv2
import numpy as np
from PIL import Image
ENV_SIZE_X = 640
ENV_SIZE_Y = 497

class our_player:
    def __init__(self, x=10, y=20, player_no=1):
        self.x = x
        self.y = y
        self.player_no = player_no
    
    def __str__(self):
        return f" Our Player No. {self.player_no}"

    def draw_player(self, img):
        cv2.circle(img, (self.x, self.y), 2, (0,0,255), 2)

    def action(self, choice, others):
        if(choice == 0):
            # Stay stationary
            self.move(x_mov=0, y_mov=0, others=others)
        elif(choice == 1):
            # Move x front
            self.move(x_mov=1, y_mov=0, others=others)
        elif(choice == 2):
            # Move y front
            self.move(x_mov=0,y_mov=1, others=others)
        elif(choice == 3):
            self.move(x_mov=-1,y_mov=0, others=others)
        elif(choice == 4):
            self.move(x_mov=0,y_mov=-1, others=others)
        elif(choice == 3):
            # Move diagonally
            self.move(x_mov=1,y_mov=1, others=others)

    def can_move(self, x_mov=0, y_mov=0):
        if(self.x + x_mov > ENV_SIZE_X):
            return False
        elif(self.y + y_mov > ENV_SIZE_Y):
            return False
        else:
            return True

    def move(self, x_mov, y_mov, others):
        if(self.can_move(x_mov, y_mov)):
            if(self.check_collision(x_mov, y_mov, others)):
                self.x += x_mov
                self.y += y_mov
            else:
                self.x -= 10
                self.y -= 10
        else:
            self.x -= 1
            self.y -= 1


    def check_collision(self, x_mov, y_mov, others):
        check_x = self.x + x_mov
        check_y = self.y + y_mov
        for player in others:
            if(player.x == check_x and player.y == check_y):
                return False
        else:
            return True

def create_our_squad():
    p1 = our_player(x=63, y=49, player_no=1)
    p2 = our_player(x=64, y=49, player_no=2)
    p3 = our_player(x=120, y=120, player_no=3)
    p4 = our_player(x=380, y=110, player_no=4)
    p5 = our_player(x=10, y=120, player_no=5)
    p6 = our_player(x=550, y=420, player_no=6)

    squad = [p1, p2, p3, p4, p5, p6]
    return squad
