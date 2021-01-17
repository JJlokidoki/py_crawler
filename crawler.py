# 1. get from input ip address
# 2. analyze raw html for the presence of forms
# 3. analize other response code (301, 500, 403) 

from lxml import etree
import requests
import wfuzz
import sys
import os

FORMS_DICT = {'get_form': [], 
              'post_form': []}

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class FuzzDirs():
    def __init__(self, ip_add, wl, ext):
        self.ip_add = ip_add
        self.wl = wl
        self.ext = ext

    def get_list(self):
        res = []
        for i in self.fuzz_dirs():
            res.append(i)
        return res

    def fuzz_dirs(self):
        wf_sess = wfuzz.FuzzSession(url = f"{self.ip_add}FUZZ")
        # wf_sess.get_payload(self.wl)
        for req in wf_sess.fuzz(hc=[404], payloads=[("file", dict(fn=self.wl))]):
            yield req.url

class SearchForms():
    def __init__(self, urls):
        self.urls = urls

    def request_to(self):
        for i in self.urls:
            data = requests.get(i)
            yield data.raw
    
    def report():
        pass


def __test():
    print(os.getcwd())

if __name__ == "__main__":
    print(bcolors.HEADER+"**** Wfuzz report will be create in currebt dirrectory ****"+bcolors.ENDC)

    ip_add = "http://127.0.0.1:4444/"
    wordlist = "/home/nickl/py_crawler/test_wl.txt"
    extension = {'regular': ['php', 'html', 'js'],
                 'advanced': ['php', 'html', 'js', 'py'],
                 'extremely': ['php', 'html', 'js', 'py']}
    
    dirs_l = FuzzDirs(ip_add, wordlist, extension['regular']).get_list()
    print(dirs_l)