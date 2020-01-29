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

