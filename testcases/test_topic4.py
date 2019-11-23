import unittest
from ddt import ddt,data
from utils.do_excel import DOExcel
from utils.do_requets import DORequests
from utils.common import get_rootPath
import os
"""
DDT 从Excel中读取数据
"""

root_path = get_rootPath()
excel_path = os.path.join(root_path,'data/topicdata.xlsx')

doExcel = DOExcel(excel_path,'indextopic')
all_data = doExcel.read_excel()

"""
[(1, 'get', 'http://39.107.96.138:3000/api/v1//topics', '{"page": 1, "tab": "Job.", "limit": 1, "mdrander": "false"}', None, None, None), (2, 'get', 'http://39.107.96.138:3000/api/v1//topics', '{"page": 1, "tab": "Good.", "limit": 1, "mdrander": "false"}', None, None, None)]
"""



@ddt
class TestIndexPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass


    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass




    @data(*all_data)
    def test_index_page(self,data):
        # print(data)
        re = DORequests(method=data[1],url=data[2])
        r = re.do_requst(eval(data[3]))
        print(r.request.url)
        """
        TODO fix this bug
        http://39.107.96.138:3000/api/v1/topics?page=1&tab=Ask.&limit=1&mdrander=false
        """
        print(r.json())

    @unittest.skip("Skip")
    def test_topics(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
