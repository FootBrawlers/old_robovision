import cv2

video_path = '''E:\\Aditya\\AI_DL_ML\\Robo_Soccer\\Robo_vision\\data\\clipped_videos\\Video_1.mp4'''
save_path = '''data\\clipped_images'''

def extract_frames_persec(video_path, save_path):
	try:
		cap = cv2.VideoCapture(video_path)
		fps = cap.get(cv2.CAP_PROP_FPS)
		index = 0
		counter = 0
		ret = 1
		while(ret):    
			ret, frame = cap.read()
			if(ret == 1):
				if((counter % fps == 0)):		
					cv2.imwrite("Video_1_frame%d.jpg" % index, frame) 
					index += 1
					counter += 1
				else:
					counter += 1
			else:
				print("Error while reading the frame")
	except:
		print("Could not read the Video")


if __name__ == "__main__":
    extract_frames_persec(video_path, save_path)