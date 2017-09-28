class Passenger(object):
    def __init__(self, _id, x, y, max_age):
        self._id = _id
        self.x = x
        self.y = y
        self.lastX = False
        self.lastY = False
        self.age = 0
        self.max_age = max_age
        self.done = False

    def updateCoords(self, nx, ny):
        self.age = 0
        self.lastX = nx
        self.lastY = ny

    def bday(self):
        self.age += 1
        if self.age > self.max_age:
            self.done = True

    def timedOut(self):
        return self.done

    def wasGoingIn(self):
        if self.y - self.lastY > 0:
            return False
        return True
