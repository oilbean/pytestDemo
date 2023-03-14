"""
一些随机数据 生成方法
"""
import random
import time


def goodsname():
    nowtime = str(time.strftime("%Y-%m-%d-%H:%M:%S",time.gmtime()))
    goodsname = "实物商品-自动化创建-"+nowtime

    return goodsname

def goodsNo():

    numbers = "P"+str(random.randint(10000,99999))

    return numbers