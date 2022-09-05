from abc import ABCMeta, abstractmethod
from msilib.schema import Component


class ComputerComponent(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def showInfo(self, indent=""):
        pass

    def isComposite(self):
        return False
    
    def startup(self, indent=""):
        print("%s%s 即将结束工作..." % (indent, self._name))

    def shutdown(self, indent=""):
        print("%s%s 即将结束工作..." % (indent, self._name))

    
class CPU(ComputerComponent):
    """
    中央处理器
    """

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print("%sCPU:%s, 可以进行高速计算" % (indent, self._name))

    
class MemoryCard(ComputerComponent):
    """
    内存条
    """

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print("%s内存:%s, 可以缓存数据，读写速度快" % (indent, self._name))


class HardDisk(ComputerComponent):
    """
    硬盘
    """

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print("%s硬盘:%s, 可以永久存储数据，容量大" % (indent, self._name))



class GraphicsCard(ComputerComponent):
    """
    显卡
    """

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print("%s显卡:%s, 可以告诉计算和处理图形图像" % (indent, self._name))


class Battery(ComputerComponent):
    """
    电源
    """

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print("%s电源:%s, 可以持续给主板和外接配件供电" % (indent, self._name))


class Fan(ComputerComponent):
    """
    风扇
    """

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print("%s风扇:%s, 辅助cpu散热" % (indent, self._name))



class Displayer(ComputerComponent):
    """
    显示器
    """

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print("%s显示器:%s, 负责内容的显示" % (indent, self._name))


class ComputerComposite(ComputerComponent):
    """
    配件组合器
    """
    def __init__(self, name):
        super().__init__(name)
        self._components = []
    
    def showInfo(self, indent=""):
        print("%s, 由以下部件组成：" % (self._name))
        indent += "\t"
        for element in self._components:
            element.showInfo(indent)

    def isComposite(self):
        return True
    
    def addComponent(self, component):
        self._components.append(component)

    def removeComponent(self, component):
        self._components.remove(component)
    
    def startup(self, indent=""):
        super().startup(indent)
        indent += "\t"
        for element in self._components:
            element.startup(indent)
    
    def shutdown(self, indent):
        super().shutdown(indent)
        indent += "\t"
        for element in self._components:
            element.shutdown(indent)


class Mainboard(ComputerComposite):
    """
    主板
    """
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print(indent + "主板", end="")
        super().showInfo(indent)


class ComputerCase(ComputerComposite):
    """
    机箱
    """

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print(indent + "机箱", end="")
        super().showInfo(indent)


class Computer(ComputerComposite):
    """
    电脑
    """

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print(indent + "电脑", end="")
        super().showInfo(indent)


def testComputer():
    mainBoard = Mainboard("GIGABYTE Z170M M-ATX")
    mainBoard.addComponent(CPU("INtel"))
    mainBoard.addComponent(MemoryCard("Kingston"))
    mainBoard.addComponent(HardDisk("Kingston V300"))
    mainBoard.addComponent(GraphicsCard("Colorful iGame 750"))

    computerCase = ComputerCase("SAMA MATX")
    computerCase.addComponent(mainBoard)
    computerCase.addComponent(Battery("Antec VP 450P"))
    computerCase.addComponent(Fan("DEEPCOOL 120T"))

    computer = Computer("Tony DIY 电脑")
    computer.addComponent(computerCase)
    computer.addComponent(Displayer("AOC"))

    computer.showInfo("")
    print("\n 开机过程: ")
    computer.startup("")
    print("\n 关机过程: ")
    computer.shutdown("")



testComputer()