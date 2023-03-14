'''
封装 requests 函数 ，并做部分处理
'''

import logging
import requests

log = logging.getLogger(__name__)
class request():

    def __int__(self):
        pass

    def get(self,url,params="",headers=""):

        result = requests.get(url,params=params,headers=headers)

        log.info(f"[GET请求]：{url},请求头：{headers},请求参数：{params}\n 请求结果：{result.text}")

        return result

    def post(self,url,data="",headers=""):

        result = requests.post(url,data=data,headers=headers)

        log.info(f"[POST请求]：{url},请求头：{headers},请求参数：{data}\n 请求结果：{result.text}")

        return result

    def post_json(self, url, data="", headers=""):
        result = requests.post(url, json=data, headers=headers)

        log.info(f"[POST请求]：{url},请求头：{headers},请求参数：{data}\n 请求结果：{result.text}")

        return result

    def request(self,method,url,data,headers=""):

        if method =="GET":
            return self.get(url,params=data,headers=headers)
        elif method == "POST":
            return self.post(url,data=data,headers=headers)
        elif method == "POST_JSON":
            return self.post_json(url,data=data,headers=headers)
        else:
            log.error("请求类型无效")
            raise TypeError("请求类型无效")

