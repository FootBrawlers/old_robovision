import cv2

video_path = '''data\\Videos\\Clipped Videos\\2015_VID_1_3.mp4'''
save_path = '''data\\pictures\\2015_VID_1_3'''

def extract_frames(video_path, save_path):
    try:
        cap = cv2.VideoCapture(video_path)
        index = 0
        ret = 1
        while(ret):    
            ret, frame = cap.read()
            if(ret == 1):
                cv2.imwrite("2015_VID_1_3_frame%d.jpg" % index, frame) 
                index += 1
            else:
                print("Error while reading the frame")
    except:
        print("Could not read the Video")


if __name__ == "__main__":
    extract_frames(video_path, save_path)