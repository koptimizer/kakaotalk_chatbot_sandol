from selenium import webdriver
import time

browser = webdriver.Chrome("./chromedriver")
# let the browser wait for some time.
time.sleep(3)
# navigate to the Web URL
browser.get("http://www.kpu.ac.kr/front/boardlist.do?bbsConfigFK=1&siteGubun=14&menuGubun=1#")
print(browser)
