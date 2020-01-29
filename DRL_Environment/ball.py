class ball:
	def __init__(self, size, x, y):
		self.size = size
		self.x = x 
		self.y = y

	def __str__(self):
		return f"Ball is at location {self.x,self.y}"

	def draw_ball(self, img):
		cv2.circle(img, (self.x, self.y), 2, (0,255,255), 2)

	



