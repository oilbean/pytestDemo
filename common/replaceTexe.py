"""
1.替换yaml文档中的数据

"""
import json
from string import Template

class Replace:
    def __int__(self):
        pass

    def yaml_replace(self,data,newdata,**kwargs):
        """
        :param data: yaml数据
        :param newdata: 需要替换的动态数据
        :param kwargs: 其他参数
        :return:
        """
        dic={}
        tempplate = Template(data)

        if len(kwargs)==0:
            realData = tempplate.safe_substitute(newdata)
        else:
            for key in kwargs:
                dic[key] == kwargs[key]
            realData = tempplate.safe_substitute(dic)

        return json.loads(realData)


