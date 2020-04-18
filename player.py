#python3
import sprites

class Player:
    def __init__(self):
        self.sprite = sprites.Player()
        self.target = (0, 0)
        self.top = 0
        self.left = 0

    def move(self):
        ydiff = self.target[0] - self.top
        xdiff = self.target[1] - self.left
        yspeed = 0
        xspeed = 0

        if ydiff>0 and ydiff > 1:
            yspeed=2
        elif ydiff<0 and ydiff < -1:
            yspeed=-2
        
        if xdiff>0 and xdiff > 1:
            xspeed=2
        elif xdiff<0 and xdiff < -1:
            xspeed=-2

        self.sprite.rect = self.sprite.rect.move(yspeed, xspeed)
        self.top += yspeed
        self.left += xspeed