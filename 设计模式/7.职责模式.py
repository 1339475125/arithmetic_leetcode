from  abc import ABCMeta, abstractmethod

class Person:
    """
    请假申请人
    """

    def __init__(self, name:str, dayoff: int, reason: str):
        self.__name = name
        self.__dayoff = dayoff
        self.__reason = reason
        self.__leader: Manager = None
    
    def getName(self):
        return self.__name

    def getDayoff(self):
        return self.__dayoff

    def getReason(self):
        return self.__reason

    def setLeader(self, leader:str):
        self.__leader = leader

    def request(self):
        print("%s 申请请假 %d 天，请假理由： %s" % (self.__name, self.__dayoff, self.__reason))
        if self.__leader:
            self.__leader.handleRequest(self)


class Manager(metaclass=ABCMeta):
    """
        公司管理人员
    """

    def __init__(self, name, title):
        self.__name = name
        self.__title = title
        self._nextHandler: Manager = None

    def getName(self):
        return self.__name

    def getTitle(self):
        self.__title

    def setNextHandler(self, nextHandler):
        self._nextHandler = nextHandler

    @abstractmethod
    def handleRequest(self, person):
        pass


class Supervisor(Manager):
    """
    主管
    """

    def __init__(self, name, title):
        super().__init__(name, title)

    def handleRequest(self, person:Person):
        if person.getDayoff() <= 2:
            print("同意%s 请假， 签字人： %s(%s)" % (person.getName(), self.getName(), self.getTitle()))
        if self._nextHandler is not None:
            self._nextHandler.handleRequest(person)


class DepartmentManager(Manager):
    """
    部门总监
    """
    def __init__(self, name, title):
        super().__init__(name, title)

    def handleRequest(self, person: Person):
        if person.getDayoff() > 2 and person.getDayoff() <= 5:
            print("同意%s 请假， 签字人： %s(%s)" % (person.getName(), self.getName(), self.getTitle()))

        if self._nextHandler is not None:
            self._nextHandler.handleRequest(person)


class CEO(Manager):
    """
    CEO
    """
    def __init__(self, name, title):
        super().__init__(name, title)
    
    def handleRequest(self, person: Person):
        if person.getDayoff() > 5 and person.getDayoff() <= 22:
            print("同意%s 请假， 签字人： %s(%s)" % (person.getName(), self.getName(), self.getTitle()))

        if self._nextHandler is not None:
            self._nextHandler.handleRequest(person)


class Administrator(Manager):

    def __init__(self, name, title):
        super().__init__(name, title)
    
    def handleRequest(self, person: Person):
        print("%s 的请假申请已审核， 情况属实，处理人: %s(%s)\n" % (person.getName(), self.getName(), self.getTitle()))

    
def testAskForleave():
    directLeader = Supervisor("Eren", "客户端研发经理")
    departmentLeader = DepartmentManager("Eric", "技术研发中心总监")
    ceo = CEO("Halen", "啊公司CEO")
    administrator = Administrator("nina", "行政中心总监")

    directLeader.setNextHandler(departmentLeader)
    departmentLeader.setNextHandler(ceo)
    ceo.setNextHandler(administrator)

    sunny = Person("Sunny", 1, "canjia dahui")
    sunny.setLeader(directLeader)
    sunny.request()

    tony = Person("Tony", 5, "家里及时")
    tony.setLeader(directLeader)
    tony.request()

    pony = Person("Pony", 15, "chuguo shengzao")
    pony.setLeader(directLeader)
    pony.request()




if __name__ == "__main__":
    testAskForleave()



