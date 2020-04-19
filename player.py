#python3
import sprites

class Player:
	def __init__(self):
		self.sprite = sprites.Player()
		self.target = (250, 250)
		self.top = 250
		self.left = 250
		self.item = ""
		self.baby = 0
		self.deliver = False

	def move(self):
		ydiff = self.target[0] - self.top - 20
		xdiff = self.target[1] - self.left - 20
		yspeed = 0
		xspeed = 0

		if ydiff>0 and ydiff > 1:
			yspeed=3
		elif ydiff<0 and ydiff < -1:
			yspeed=-3
		
		if xdiff>0 and xdiff > 1:
			xspeed=3
		elif xdiff<0 and xdiff < -1:
			xspeed=-3

		self.sprite.rect = self.sprite.rect.move(yspeed, xspeed)
		self.top += yspeed
		self.left += xspeed