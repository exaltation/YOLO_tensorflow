import math
import numpy

class Passenger(object):
    def __init__(self, _id, x, y, w, h, max_age):
        self._id = _id
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.tracks = []
        self.age = 0
        self.max_age = max_age
        self.done = False
        self.near_radius = 250

    def updateCoords(self, nx, ny):
        self.tracks.append([nx,ny])
        self.age = 0

    def bday(self):
        self.age += 1
        if self.age > self.max_age:
            self.done = True

    def timedOut(self):
        return self.done

    def wasGoingIn(self, inLine, outLine):
        if len(self.tracks) < 5:
            return False
        if abs(self.tracks[-1][1] - inLine) < abs(self.tracks[-1][1] - outLine):
            return True
        return False

    def wasGoingOut(self, inLine, outLine):
        if len(self.tracks) < 5:
            return False
        if abs(self.tracks[-1][1] - inLine) > abs(self.tracks[-1][1] - outLine):
            return True
        return False

    def near(self, _passenger):
        if self.mod(_passenger) < 0.7 * min(self.w, self.h) and self.w - _passenger.w < self.near_radius and self.h - _passenger.h < self.near_radius:
            return True
        return False

    def mod(self, _passenger):
        dist = (self.x - _passenger.x)*(self.x - _passenger.x) + (self.y - _passenger.y)*(self.y - _passenger.y)
        return math.sqrt(dist)
