
import pytest

from common import getData,getResultText
from common.re import request


class TestCase():

    @classmethod
    def setup(cls):
        pass

    data = getData.getYamlData("../caseData/pop/popup.yaml")

    @pytest.mark.parametrize('case',data)
    def test_case01(self,case):

        method = case['http']['method']
        url = case['http']['path']
        data = case['data']

        result = request().request(url=url,method=method,data=data)

        popupType = getResultText(result,"popupType")

        expected = case['expected']['popupType']

        assert popupType == expected

