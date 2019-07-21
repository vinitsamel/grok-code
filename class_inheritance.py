from enum import Enum, unique

@unique
class FuelType(Enum):
    GAS = 0
    HYBRID = 1
    ELECTRIC = 2
    HYDROGEN = 3

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)

class Car:
    def __init__(self, name, zerotosixty = None, fuel = 0):
        self.name = name
        self.zerotosixty = zerotosixty
        self.fuel = fuel

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def zerotosixty(self):
        return self._zerotosixty

    @zerotosixty.setter
    def zerotosixty(self, ztos):
        self._zerotosixty = ztos

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, fuel):
        if FuelType.has_value(fuel):
            self._fuel = fuel
        else:
            raise ValueError

    def __str__(self):
        return self.name + " : " + str(self.zerotosixty) +  " : " + str(self.fuel)

class ElectricCar(Car):
    def __init__(self, name, zerotosixty=None):
        super().__init__(name, zerotosixty, 2)

class SingletonOK:
    _instance = None

    def __init__(self, value=None):
        if Singleton._instance is not None:
            raise Exception("Cannot instantiate a Singleton. Call GetInstance instead")
        else:
            self.value = value
            Singleton._instance = self

    @classmethod
    def getInstance(cls):
        if Singleton._instance is None:
            Singleton("Singleton")
        return Singleton._instance

class Singleton:
    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if Singleton._instance is None:
            Singleton._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return Singleton._instance

def main():
    c1 = Car("Tesla", 3.0, 2)
    print (c1)

    c2 = ElectricCar("M3")
    c2.zerotosixty = 1.9
    print (c2)

    #c3 = Singleton.getInstance()
   # print (c3.value)

    c4 = Singleton()
    print (c4.value)

main()



