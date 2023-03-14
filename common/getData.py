
# -*- coding：utf-8 -*-
'''
获取 yaml 文件的数据
并做部分处理
'''

import logging
import yaml

log = logging.getLogger(__name__)

def getYamlData(path):
    """
    :param path: 传入文件地址
    :return: 返回yaml数据，数据类型根据yaml文件数据返回list，dict，string等type
    """

    with open(path,encoding="utf-8") as f:

        data = yaml.load(f.read(),Loader=yaml.SafeLoader)
        log.info(f"获取文件:{path}中测试数据:{data}")
    return data

def writeYamlData(path,data):
    """
    可以将数据反向写入yaml文件yaml.dump()
    :param path:
    :param data:
    :return:
    """

    with open(path,"w") as f:
        yaml.dump(data,f,encoding="utf-8",allow_unicode=True)

