
"""
 根据返回结果，获取返回信息

"""
import json

import jsonpath as jsonpath

def get_text(res,key):
    if res is not None:
        try:

            text = json.loads(res.text)
            value = jsonpath.jsonpath(text,'$..{0}'.format(key))

            if value:
                if len(value) == 1:
                    return value[0]
                else:
                    return value

        except Exception as e:
            return e
    else:
        return None