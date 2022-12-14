from abc import ABCMeta, abstractmethod


class ReceiveParcel(metaclass=ABCMeta):
    """
    接受包裹的抽象类
    """

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def receive(self, parcelContent):
        pass


class TonyReception(ReceiveParcel):
    """
    tony 接受
    """

    def __init__(self, name, phoneNum):
        super().__init__(name)
        self.__phoneNum = phoneNum

    def getPhoneNum(self):
        return self.__phoneNum

    def receive(self, parcelContent):
        print("货物主人： %s, 手机号： %s" % (self.getName(), self.getPhoneNum()))
        print("接收到一个包裹， 包裹内容: %s" % parcelContent)
    

class WendyReception(ReceiveParcel):
    """
    wendy代收
    """

    def __init__(self, name, receiver: TonyReception):
        super().__init__(name)
        self.__receiver = receiver

    def receive(self, parcelContent):
        print("我是%s 的朋友，我来帮他代收快递" % (self.__receiver.getName()))
        if self.__receiver is not None:
            self.__receiver.receive(parcelContent)
        print("代收人： %s" % self.getName())
    


def testReceiveParcel():
    tony = TonyReception("Tony", "18512345678")
    print("Tony接收")
    tony.receive("雪地靴")
    print()


    print("wendy 代收")
    wendy = WendyReception("wendy", tony)
    wendy.receive("雪地靴")



# ##########  抽象类代码 ##########

class Subject(metaclass=ABCMeta):
    """
    主题类
    """
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name
    
    @abstractmethod
    def request(self, content = ""):
        pass


class RealSubject(Subject):
    """
    真实主题类
    """

    def request(self, content):
        print("RealSubject todo something...")


class ProxySubject(Subject):
    """
    代理主题类
    """
    def __init__(self, name, subject: RealSubject):
        super().__init__(name)
        self._realsubject = subject

    def request(self, content = ''):
        self.preRequest()
        if self._realsubject is not  None:
            self._realsubject.request(content)
        self.afterRequest()

    def preRequest(self):
        print("preRequest")

    def afterRequest(self):
        print("afterRequest")




if __name__ == "__main__":
    testReceiveParcel()