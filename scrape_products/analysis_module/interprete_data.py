import json
import sys
from os import path
from scrapy.selector import Selector
from scrapy.http import HtmlResponse, TextResponse, JsonRequest
import requests

def ReadVprokJson(file_path = path.join(path.dirname(sys.path[0]), "vprok.json")):
    if not path.isfile(file_path):
        raise FileNotFoundError("the vprok.json file doesn't exist")
    with open(file_path, encoding='ascii') as f:
        data = json.load(f)
    print(data)

def TestSelector():
    response = requests.request(method='GET', url='https://www.vprok.ru/product/market-perekrestok-yabloki-zelenye-fasovannye-1-5-kg-up--1177093')
    print(response)
    return 'hi' #response.xpath('@ui-id-1').get()

if __name__ == "__main__" :
    answer = TestSelector()
    print(answer)