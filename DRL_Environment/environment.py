import cv2
import numpy as np
from PIL import Image
from enemy_player import enemy_player, create_enemy_squad
from environment_setup import create_environment_setup
from our_player import our_player, create_our_squad
from utilities import show_squad, render

envir = create_environment_setup()
# render(envir)

our_squad = create_our_squad()
envir = show_squad(our_squad, envir)
# render(envir)

enemy_squad = create_enemy_squad()
envir = show_squad(enemy_squad, envir)
render(envir)

# print(squad)


