import  unittest
import requests
from ddt import  ddt,data

"""
data 使用方法
"""
prama_data1 = {
            "page":1,
            "tab":"share",
            "limit":1,
            "mdrender":"fasle"
        }
prama_data2 = {
            "page": 1,
            "tab": "share",
            "limit": 1,
            "mdrender": "true"
        }
prama_data3 = {
            "page": 1,
            "tab": "ask",
            "limit": 5,
            "mdrender": "true"
        }
prama_data4 = {
            "page": 1,
            "tab": "ask",
            "limit": 5,
            "mdrender": "false"
            }

@ddt
class TestTopics(unittest.TestCase):

    @data(prama_data1,prama_data2,prama_data3)
    def test_index_page(self,value):
        print("value==",value)
        r = requests.get(url='http://39.107.96.138:3000/api/v1/topics',params=value)
        print(r.request.url)
        result_data = r.json()
        self.assertEqual(value["limit"],len(result_data['data']),f"返回的数据长度应为{value['limit']}")
        for d in result_data["data"]:
            self.assertEqual(value['tab'],d['tab'],f"返回数据中的每一个对象tab值都应该为{d['tab']}")



if __name__ == '__main__':
    unittest.main(verbosity=2)