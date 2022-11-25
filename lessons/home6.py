class Hero:
    def __init__(self, fly=0, power=0,speed=0,ads=0):
        self.__fly=fly
        self.__power=power
        self.__speed=speed
        self.__ads=ads
    def setfly(self, fly):
        self.__fly = fly

    def getfly(self):
        return self.__fly

    def setpower(self, power):
        self.__power = power

    def getpower(self):
        return self.__power

    def setspeed(self, speed):
        self.__speed = speed

    def getspeed(self):
        return self.__speed

    def setads(self, ads):
        self.__ads = ads

    def getads(self):
        return self.__ads

hero=Hero()
hero.setspeed(24)
hero.setfly(43)
hero.setpower(23)
hero.setads(12)
print(f"скорость {hero.getspeed()}\n"
      f"сила {hero.getpower()}\n"
      f"летучесть {hero.getfly()}\n"
      f"супер сила {hero.getads()}")