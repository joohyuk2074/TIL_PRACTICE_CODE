import requests
import time
import random
from selenium import webdriver
from bs4 import BeautifulSoup

# # 다운받은 webdriver의 경로를 지정
# executable_path='/Users/joohyuk/Documents/JAVAWORKSPACE/study/TIL_PRACTICE_CODE/python-algorithm/venv/lib/python3.10/site-packages/selenium/webdriver'
# driver = webdriver.Firefox(executable_path = executable_path)
# time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
# naver login page로 이동
# driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.link)
# print(soup.link.attrs)
# print(soup.link["href"])


print(soup)
result = soup.find("link", attrs={"type": "image/x-icon"})
print(result)
