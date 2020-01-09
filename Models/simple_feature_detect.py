import cv2
import matplotlib.pyplot as plt
import numpy as np

def read_image_rgb(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    if img is None:
        print("Not found the image")
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def read_image_bgr(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    if img is None:
        print("Not found the image")
    return img

def read_image_grayscale(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Not found the image")
    return img


to_detect_robo = read_image_grayscale(r'E:\Aditya\AI_DL_ML\Robo_Soccer\Robo_vision\Sample_data\to_detect.jpg')
robo_image = read_image_grayscale(r'E:\Aditya\AI_DL_ML\Robo_Soccer\Robo_vision\Sample_data\Video_1_frame280.jpg')

plt.imshow(robo_image[...,::-1])
plt.show()

w, h = to_detect_robo.shape[::-1]

for i in range(25):
    res = cv2.matchTemplate(robo_image, to_detect_robo, cv2.TM_CCOEFF)

    # threshold = 0.2
    # loc = np.where( res >= threshold)
    # for pt in zip(*loc[::-1]):
    #     cv2.rectangle(robo_image, pt, (pt[0] + w, pt[1] + h), 255, 2)


    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(robo_image, top_left, bottom_right, (0,0,255), 4)
    
    plt.imshow(res[...,::-1])
    plt.show()

    plt.imshow(robo_image[...,::-1])
    plt.show()

    cv2.rectangle(robo_image, top_left, bottom_right, (0,0,255), cv2.FILLED)

    plt.imshow(robo_image[...,::-1])
    plt.show()


