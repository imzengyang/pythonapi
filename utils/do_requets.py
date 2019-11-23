
import requests

class DORequests():

    def __init__(self,method,url):
        self.method = method
        self.url = url


    def do_requst(self,data=None):
        if self.method == "get":
            return requests.get(self.url,params=data)
        elif self.method == "post":
            return requests.post(self.url,data=data)