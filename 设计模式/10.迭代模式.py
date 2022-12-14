


class Customer:
    """
    客户
    """

    def __init__(self, name):
        self.__name = name
        self.__num = 0
        self.__clinics = None

    def getName(self):
        return self.__name
    
    def register(self, system):
        system.pushCustomer(self)


    def setNum(self, num):
        self.__num = num

    def getNum(self):
        return self.__num

    def setClinic(self, clinic):
        self.__clinics = clinic

    def getClinic(self):
        return self.__clinics


class NumeralIterator:
    """
    迭代器
    """

    def __init__(self, data):
        self.__data = data
        self.__curIdx = -1

    def next(self):
        if self.__curIdx < len(self.__data) - 1:
            self.__curIdx += 1
            return True
        else:
            return False
    
    def current(self):
        return self.__data[self.__curIdx] if self.__curIdx < len(self.__data) and self.__curIdx >= 0 else None


class NumeralSystem:
    """
    排号系统
    """
    __clinics = ("1号诊室", "2号诊室", "3号诊室")

    def __init__(self, name):
        self.__customers = []
        self.__curNum = 0
        self.__name = name

    def pushCustomer(self, customer:Customer):
        customer.setNum(self.__curNum + 1)
        click = NumeralSystem.__clinics[self.__curNum % len(NumeralSystem.__clinics)]
        customer.setClinic(click)
        self.__curNum += 1
        self.__customers.append(customer)
        print("%s 您好， 您已经在%s成功挂号，序号是： %04d， 清耐心等待" % (customer.getName(), self.__name, customer.getNum()))

    def getIterator(self):
        return NumeralIterator(self.__customers)


def testHospital():
    numeralSyatem = NumeralSystem("挂号台")
    lily = Customer("Lily")
    lily.register(numeralSyatem)
    pony = Customer("pony")
    pony.register(numeralSyatem)
    nick = Customer("nick")
    nick.register(numeralSyatem)
    tony = Customer("tony")
    tony.register(numeralSyatem)

    print()

    iterators = numeralSyatem.getIterator()
    while iterators.next():
        customer = iterators.current()
        print("下一位客人%4d %s 请到 %s就诊" % (customer.getNum(), customer.getName(), customer.getClinic())) 



testHospital()





