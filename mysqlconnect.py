import time
import pymysql
import json
import traceback
import requests
from selenium.webdriver import Chrome, ChromeOptions

#conn = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="cov", charset="utf8")

option = ChromeOptions()
option.add_argument("--headless")  # 隐藏游览器
option.add_argument("--no--sandbox")
browser = Chrome(options=option, executable_path="chromedriver-dev.exe")