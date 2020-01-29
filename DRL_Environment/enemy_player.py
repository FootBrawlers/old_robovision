import cv2
import numpy as np
from PIL import Image

class enemy_player:
    def __init__(self, x = 410, y = 420, player_no = 1):
        self.x = x
        self.y = y
        self.player_no = player_no
    
    def __str__(self):
        return f" Enemy Player No. {self.player_no}"

    def draw_player(self, img):
        cv2.circle(img, (self.x, self.y), 2, (255,0,0), 2)


def create_enemy_squad():
    e1 = enemy_player(x=480, y=420, player_no=1)
    e2 = enemy_player(x=560, y=320, player_no=2)
    e3 = enemy_player(x=580, y=120, player_no=3)
    e4 = enemy_player(x=620, y=320, player_no=4)
    e5 = enemy_player(x=330, y=380, player_no=5)
    e6 = enemy_player(x=310, y=220, player_no=6)

    enemy_squad = [e1, e2, e3, e4, e5, e6]
    return enemy_squad
