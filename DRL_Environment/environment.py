import cv2
import numpy as np
from PIL import Image

ENV_SIZE_X = 640
ENV_SIZE_Y = 497

def create_environment_setup(ENV_SIZE_X = 640, ENV_SIZE_Y = 497):
    env = np.zeros((ENV_SIZE_Y, ENV_SIZE_X, 3), dtype=np.uint8)    
    img = Image.fromarray(env, "RGB")
    img = np.array(img)
    center_half_x = ENV_SIZE_X // 2
    center_half_y = ENV_SIZE_Y // 2
    cv2.line(img, (center_half_x, 0), (center_half_x, ENV_SIZE_Y), color = (255,255,255), thickness=3)
    return img

# def draw_goal_lines(img, ENV_SIZE_X, ENV_SIZE_Y):



class our_player:
    def __init__(self, x = 10, y = 20, player_no = 1):
        self.x = x
        self.y = y
        self.player_no = player_no
    
    def __str__(self):
        return f" Our Player No. {self.player_no}"

    def draw_player(self, img):
        cv2.circle(img, (self.x, self.y), 2, (0,0,255), 2)

    # def action(self):

class enemy_player:
    def __init__(self, x = 410, y = 420, player_no = 1):
        self.x = x
        self.y = y
        self.player_no = player_no
    
    def __str__(self):
        return f" Enemy Player No. {self.player_no}"

    def draw_player(self, img):
        cv2.circle(img, (self.x, self.y), 2, (255,0,0), 2)

# def draw_player(img, player):
#     cv2.circle(img, (player.x, player.y), 2, (0,0,255), 2)

img = create_environment_setup()

def create_our_squad():
    p1 = our_player()
    p2 = our_player(x=30, y=30, player_no=2)
    p3 = our_player(x=150, y=70, player_no=3)
    p4 = our_player(x=380, y=110, player_no=4)
    p5 = our_player(x=10, y=120, player_no=5)
    p6 = our_player(x=550, y=420, player_no=6)

    squad = [p1, p2, p3, p4, p5, p6]
    return squad

our_squad = create_our_squad()

# def create_

def create_enemey_squad():
    e1 = enemy_player(x=480, y=420, player_no=1)
    e2 = enemy_player(x=560, y=320, player_no=2)
    e3 = enemy_player(x=580, y=120, player_no=3)
    e4 = enemy_player(x=620, y=320, player_no=4)
    e5 = enemy_player(x=330, y=380, player_no=5)
    e6 = enemy_player(x=310, y=220, player_no=6)

    enemy_squad = [e1, e2, e3, e4, e5, e6]
    return enemy_squad

def show_squad(squad):
    for player in squad:
        print(player)
        print(player.x)
        print(player.y)
        player.draw_player(img)
    
    return img

enemy_squad = create_enemey_squad()

# def create_oppoenets():

img = show_squad(our_squad)
img = show_squad(enemy_squad)

# print(p1)
# print(p1.x)
# print(p1.y)
# p1.draw_player(img)

cv2.imshow("image",img)
cv2.waitKey(100000) & 0xFF == ord('q')
    