
import os

def get_rootPath():
    """
    :return: str 当前项目的绝对路径
    """
    return os.path.dirname(os.path.dirname( os.path.abspath(__file__)))
    # pass

if __name__ == '__main__':
    get_rootPath()