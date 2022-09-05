"""
xx:公有变量，所有对象都可以访问；

_xx:单前置下划线，私有化属性和方法，for 包名 import * 禁止导入，类对象和子类可以访问，使用对象._变量名调用；

__xx:双前置下划线，避免与子类中的属性命名冲突，无法在外部直接访问，应使用对象._类名__变量名调用；

__xx__:双前后下划线，用于定义类的魔法属性/模法方法，例如：__init__,__str__等，无法直接调用；

xx_:单后置下划线，用于避免与python关键字的冲突。
"""

class Register:
    """
    报到登记
    """

    def register(self, name):
        print("活动中心： %s 同学报道成功！" % name) 
    


class Payment:
    """
    缴费中心
    """

    def pay(self, name, money):
        print("缴费中心： 收到%s 同学%s元付款，缴费成功" % (name, money))


class DormitoryManagementCenter:
    """
    生活中心（宿舍管理中心）
    """

    def provideLivingGoods(self, name):
        print("生活中心 %s 同学的生活用品已发放" % name)


class Dormitory:
    """
    宿舍
    """

    def meetRoommate(self, name):
        print("宿舍： 大家好，我是刚来的%s同学，是你们的舍友，请多关照" % name )


class Volunteer:
    """
    迎新志愿者
    """

    def __init__(self, name):
        self.__name = name
        self.__register = Register()
        self.__payment = Payment()
        self.__lifeCenter = DormitoryManagementCenter()
        self.__dormintory = Dormitory()

    def welcomeFreshmen(self, name):
        print("你好， %s同学，我是新生报奥的志愿者%s,我将带你挖成整个报道流程" %(name, self.__name))
        self.__register.register(name)
        self.__payment.pay(name, 10000)
        self.__lifeCenter.provideLivingGoods(name)
        self.__dormintory.meetRoommate(name)



def testRegister():
    volunteer = Volunteer("Frank")
    volunteer.welcomeFreshmen("Tony")
     

# testRegister()
"""
压缩文件示例
"""

from os import path
import logging
from zipapp import ZipAppError


class ZIPModel:

    def compress(self, srcFilePath, dstFilePath):
        print("ZIP 模块正在进行 %s 文件的压缩....." % srcFilePath)
        print("文件压缩成功，已保存在%s" % dstFilePath)

    def decompress(self, srcFilePath, dstFilePath):
        print("ZIP 模块正在进行 %s 文件的解压缩....." % srcFilePath)
        print("文件解压缩成功，已保存在%s" % dstFilePath)


class ZModel:

    def compress(self, srcFilePath, dstFilePath):
        print("7Z 模块正在进行 %s 文件的压缩....." % srcFilePath)
        print("文件压缩成功，已保存在%s" % dstFilePath)

    def decompress(self, srcFilePath, dstFilePath):
        print("7Z 模块正在进行 %s 文件的解压缩....." % srcFilePath)
        print("文件解压缩成功，已保存在%s" % dstFilePath)

class RARModel:

    def compress(self, srcFilePath, dstFilePath):
        print("RAR 模块正在进行 %s 文件的压缩....." % srcFilePath)
        print("文件压缩成功，已保存在%s" % dstFilePath)

    def decompress(self, srcFilePath, dstFilePath):
        print("RAR 模块正在进行 %s 文件的解压缩....." % srcFilePath)
        print("文件解压缩成功，已保存在%s" % dstFilePath)


class CompressionFacade:
    """
    压缩系统的外观类
    """

    def __init__(self):
        self.__zipModel = ZIPModel()
        self.__rarModel = RARModel()
        self.__zModel = ZModel()

    def compress(self, srcFilePath, dstFilePath, type):
        """
        根据路径不同的压缩类型，压缩成不同的格式
        """
        extName = "." + type
        fullName = dstFilePath + extName
        if (type.lower() == "zip"):
            self.__zipModel.compress(srcFilePath, fullName)
        elif (type.lower() == "rar"):
            self.__rarModel.compress(srcFilePath, fullName)
        elif (type.lower() == "7z"):
            self.__zModel.compress(srcFilePath, fullName)
        else:
            logging.error("not support this format: " + str(type))
            return False
        return True
    
    def decompress(self, srcFilePath, dstFilePath):
        """
        根据路径不同的后缀名，解压缩成不同的格式
        """
        baseName = path.basename(srcFilePath)
        extName = baseName.split(".")[1]
        if (extName.lower() == "zip"):
            self.__zipModel.decompress(srcFilePath, dstFilePath)
        elif (extName.lower() == "rar"):
            self.__rarModel.decompress(srcFilePath, dstFilePath)
        elif (extName.lower() == "7z"):
            self.__zModel.decompress(srcFilePath, dstFilePath)
        else:
            logging.error("not support this format: " + str(type))
            return False
        return True


