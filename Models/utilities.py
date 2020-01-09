import cv2

def read_image(img_path):
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

def read_grayscale(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Not found the image")
    return img
