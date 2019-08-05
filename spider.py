import requests
import re
import random
from fake_useragent import UserAgent
from urllib import parse, request
import http.cookiejar

# UserAgent使用方法
# from fake_useragent import UserAgent

# httpbin.org测试网站

# url = 'http://www.baidu.com'
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'Germey'
# }
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# # add_header方法也行
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))

# 代理
# 伪装ip
# proxy_  hander = request.ProxyHandler({
#     代理端口号
#     'http': 'http://127.0.0.1:9743'
# })
# opener = request.build_opener(proxy_hander)
# response = opener.open('网站地址（外网等）')
# print(response.read())

# cookie
# 保存cookie
# filename = "cookie.txt"
# 两种保存格式
# 1：
#   cookie = http.cookiejar.MozillaCookieJar(filename)
# 2：
#   cookie = http.cookiejar.LWPCookieJar(filename)
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# cookie.save(ignore_expires=True, ignore_discard=True)

# 读取cookie
# cookie = http.cookiejar.MozillaCookieJar()
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# print(response.read().decode('utf-8'))
