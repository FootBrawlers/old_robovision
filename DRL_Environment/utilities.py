import cv2
import numpy as np

def show_squad(squad, img):
    for player in squad:
        print(player)
        print(player.x)
        print(player.y)
        player.draw_player(img)
    
    return img

# def get_other_players(player_no, player_list):
# 	if(type == 'our'):


# 	elif(type == 'enemy'):


def render(img):
    cv2.imshow("image",img)
    cv2.waitKey(100000) & 0xFF == ord('q')




