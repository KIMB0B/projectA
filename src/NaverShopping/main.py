import json

import requests
import urllib


def getProductsInNaverShopping(product):
    product = urllib.parse.quote(product)

    url = "https://openapi.naver.com/v1/search/shop?query=" + product

    request = urllib.request.Request(url)
    request.add_header('X-Naver-Client-Id', "PX031VWN0_YzL72Xfqmz")
    request.add_header('X-Naver-Client-Secret', "pm0chqWUPi")

    response = urllib.request.urlopen(request).read().decode('utf-8')
    return response
