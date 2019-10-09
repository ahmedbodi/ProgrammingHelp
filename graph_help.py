import turtle
import math

def calculateNext(trajectory, velocity, angle):
    x = velocity * math.cos(angle) * trajectory
    y = velocity * math.sin(angle) * trajectory - 0.5 * (9.8) * trajectory **2
    return x, y


trajectory = 0
velocity = 100
angle = 40

x, y = calculateNext(trajectory, velocity, angle)
while y > 0:
    trajectory += 0.1
    x, y = calculateNext(trajectory, velocity, angle)
    print("Trajectory: %s, Velocity: %s, Angle: %s, X: %s, Y: %s" % (
        trajectory, velocity, angle, x, y
    ))
