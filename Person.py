class Passenger(object):
    def __init__(self, _id, x, y, max_age):
        self._id = _id
        self.x = x
        self.y = y
        self.tracks = []
        self.age = 0
        self.max_age = max_age
        self.done = False
        self.near_radius = 300

    def updateCoords(self, nx, ny):
        self.tracks.append([nx,ny])
        self.age = 0
        # self.x = nx
        # self.y = ny

    def bday(self):
        self.age += 1
        if self.age > self.max_age:
            self.done = True

    def timedOut(self):
        return self.done

    def wasGoingIn(self, inLine, outLine):
        if len(self.tracks) < 3:
            return False
        if self.y - self.tracks[-1][1] < 0 and abs(self.y - inLine) < abs(self.y - outLine):
            return True
        return False

    def wasGoingOut(self, inLine, outLine):
        if len(self.tracks) < 3:
            return False
        if self.y - self.tracks[-1][1] > 0 and abs(self.y - inLine) > abs(self.y - outLine):
            return True
        return False

    def near(self, x, y):
        if abs(x - self.x) < self.near_radius and abs(y - self.y) < self.near_radius:
            return True
        return False
