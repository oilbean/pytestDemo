'''
配置环境
1。 pip install allure-pytest
2. 下载commandline压缩包 解压到目录 E：//
3。配置环境变量到 E
'''
import os
import time

import pytest


def report():
    """
    1.如何保存多份测试报告-----保存不同的文件夹
    2。如何展示最新一份测试报告 -----根据时间排序
    :return:
    """

    #报告根据时间保存，可查看历史报告
    nowTime = str(time.strftime("%Y-%m-%d-%H-%M-%S",time.gmtime()))
    allure_result = f"./allure-result/{nowTime}"

    #执行用例，将用例数据保存在allure-result文件夹中
    pytest.main(['-vs','.\\testCase\\popupget.py','--alluredir',allure_result])

    #根据allure-result文件夹中的数据生产report报告
    os.system(f"allure generate {allure_result} -o ./result/{nowTime} ----")

if __name__ == '__main__':
    report()