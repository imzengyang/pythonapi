import unittest
from testcases.test_topic4 import TestIndexPage
from testcases.test_topic2 import TestTopics
from BeautifulReport import  BeautifulReport

def get_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    # 使用加载器从 TestClass中去取数据
    tests1 = loader.loadTestsFromTestCase(TestIndexPage)
    tests2 = loader.loadTestsFromTestCase(TestTopics)
    # suite.addTest(TestIndexPage('test_index_page'))
    suite.addTests(tests1)
    suite.addTests(tests2)
    return suite


def get_test_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    # TODO loadTestsFromModule
    # tests = loader.loadTestsFromModule("testcases")
    tests = loader.discover('testcases',"test_**.py")
    suite.addTests(tests)
    return suite

if __name__ == '__main__':
    # with open('./log.txt',mode='w',encoding='utf8') as f:
    #     runner = unittest.TextTestRunner(stream=f,verbosity=2)
    #     # suite = get_suite()
    #     suite = get_test_suite()
    #     runner.run(suite)
    suite = get_test_suite()
    result = BeautifulReport(suite)
    result.report("APITesting",filename="apiReport2",log_path='./apiRunning.log',theme="theme_candy")