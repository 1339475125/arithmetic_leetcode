

from abc import ABCMeta, abstractmethod


class Toy(metaclass=ABCMeta):
    """
    玩具
    """
    def __init__(self, name):
        self._name = name
        self.__components = []
    
    def getName(self):
        return self._name

    def addComponent(self, component, count=1, unit="个"):
        self.__components.append([component, count, unit])
        print("%s增加了%d %s%s" % (self._name, count, unit,component))

    @abstractmethod
    def feature(self):
        pass


class Car(Toy):
    """
    小车
    """
    def feature(self):
        print("我是 %s, 我可以快速蹦跑....." % self._name)


class Manor(Toy):
    """
    庄园
    """
    def feature(self):
        print("我是 %s, 我可供观赏， 也可用来游玩" % self._name)


class ToyBuilder:
    def buildCar(self):
        car = Car("迷你小车")
        print("正在构建%s ...."% car.getName())
        car.addComponent("轮子", 4)
        car.addComponent("车身", 1)
        car.addComponent("发动机", 1)
        car.addComponent("方向盘", 1)
        return car

    def buildManor(self):
        manor = Manor("庄园")
        print("正在构建%s ...."% manor.getName())
        manor.addComponent("轮子", 4)
        manor.addComponent("车身", 1)
        manor.addComponent("发动机", 1)
        manor.addComponent("方向盘", 1)
        return manor


def testBuilder():
    builder = ToyBuilder()
    car = builder.buildCar()
    car.feature()
    print()
    manor = builder.buildManor()
    manor.feature()


testBuilder()

