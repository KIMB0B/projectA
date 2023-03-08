import json

import requests
import urllib
import config


def getProductsInNaverShopping(product):
    product = urllib.parse.quote(product)

    url = "https://openapi.naver.com/v1/search/shop?query=" + product

    request = urllib.request.Request(url)
    request.add_header('X-Naver-Client-Id', config.naver_shopping_api_id)
    request.add_header('X-Naver-Client-Secret', config.naver_shopping_api_key)

    response = urllib.request.urlopen(request).read().decode('utf-8')
    return response
