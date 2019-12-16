
import requests
from utils.log import log
import  sys


class DORequests():

    def __init__(self,method,url):
        self.method = method
        self.url = url

    def do_requst(self,data=None):
        if self.method == "get":
            try:
                log.info(f"发送GET请求,请求的路径为{self.url},请求参数{data}")
                r = requests.get(self.url, params=data)
                result_data = r.json()
                log.info(f"服务器响应结果{result_data}")
                return r
            except Exception as e:
                log.error(f"服务器发生异常，请检查错误信息: {e}")


        elif self.method == "post":
            log.info(f"发送POST请求,请求的路径为{self.url},请求参数{data}")
            return requests.post(self.url,data=data)