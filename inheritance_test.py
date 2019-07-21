from class_inheritance import Car, ElectricCar

def testCarName():
    c = Car("Tesla")
    assert c.name == "Tesla"

def main():
    testCarName()

main()