import math

class pendulum:
    def __init__(self, chopx=0, chopy=0, choplen=100, ballx=0, bally=0, ballsize=0, ballmass=100):
        self.chop = {"x": chopx, "y": chopy, "len": choplen}
        self.ball = {"x": ballx, "y": bally, "size": ballsize, "mass": ballmass}

    def addAngle(self, angle):
        self.ball["x"] -= (math.sin(angle) * self.chop["len"])
        self.ball["y"] -= (math.cos(angle) * self.chop["len"])

p = pendulum()
p.addAngle(360)
print(vars(p))
