from ddt import ddt,file_data
import unittest
import requests
"""
yaml data

注意： 注意参数位置 以及参数名
"""


@ddt
class TestTopics(unittest.TestCase):

    @file_data('../data/topics.yaml')
    def test_index_page(self,page,tab,limit,mdrender):
        value={
            "page": page,
            "tab": tab,
            "limit": limit,
            "mdrender": mdrender
        }
        print(value)
        r = requests.get(url='http://39.107.96.138:3000/api/v1/topics',params=value)
        print(r.request.url)
        result_data = r.json()
        self.assertEqual(limit,len(result_data['data']),f"返回的数据长度应为{limit}")
        for d in result_data["data"]:
            self.assertEqual(tab,d['tab'],f"返回数据中的每一个对象tab值都应该为{tab}")


if __name__ == '__main__':
    unittest.main(verbosity=2)