#python3
from alien import Alien

class GameManager:
	def __init__(self, app):
		self.app = app
		self.n_babies = 0
		self.babies = []
		self.score = 0
		self.baby_to_pick = False
		self.time_to_next_baby = 7000
	
	def get_babies(self):
		return self.babies

	def deliver_baby(self, baby):
		self.babies.pop(baby)
		self.n_babies -= 1
		self.score += 1

	def receive_baby(self):
		baby = Alien(len(self.n_babies))
		self.babies.append(baby)
		self.n_babies += 1

	def update(time):
		if(time > self.time_to_next_baby and not self.baby_to_pick):
			
			self.deliver_baby()
		
		for i in self.babies:
			if i.life == 0:
				return 0


