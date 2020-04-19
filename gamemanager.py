#python3
from alien import Alien

class GameManager:
	def __init__(self, app):
		self.app = app
		self.n_babies = 0
		self.babies = []
		self.score = 0
		self.baby_to_pick = False
		self.time_to_next_baby = 20
	
	def get_babies(self):
		return self.babies

	def deliver_baby(self, baby):
		self.babies[baby.tag] = None
		self.score += 1

	def receive_baby(self):
		baby = Alien(self.n_babies)
		self.babies.append(baby)
		self.n_babies += 1

	def update(self, time):
		self.time_to_next_baby -= time

		if self.time_to_next_baby <= 0:
			self.receive_baby()
			self.time_to_next_baby  = 30

		for i in self.babies:
			if (i != None):
				if round(i.life/4,0) == 25:
					return 0
			
				i.update(time)
			
		return 1
			


