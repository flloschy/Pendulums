import pygame, math
from Modules.pendulum import pendulum
from Modules.simulation import Simulation


Sim = Simulation()
Pen = pendulum(ballx=50, bally=50, chopx=500, chopy=500)
while True:
    Pen.addAngle(10)
    pygame.draw.line(Sim.WIN, (255, 255, 255), (Pen.ball["x"], Pen.ball["y"]), (Pen.chop["x"], Pen.chop["y"]), width=3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()