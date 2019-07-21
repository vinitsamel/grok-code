class RGCMath:

    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    def add(self):
        return self.x + self.y

    def mul(self):
        return self.x * self.y

    def __str__(self):
        return str(self.x) + " : " + str(self.y)

#def main():
    #m = RGCMath(1,2)
   # m.x = 2
    #print(m)
    #assert 4 == m.add()

#main()

