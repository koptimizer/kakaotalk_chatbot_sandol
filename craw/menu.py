import requests
from bs4 import BeautifulSoup
import time
import re

def menu() :
    try :
        url = 'http://localhost:8080/crawling/main.jsp'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        lunBox = soup.find_all("tr")[1]
        dinBox = soup.find_all("tr")[2]

        lunTd = str(lunBox).replace("\t", "").replace("\r", "").replace("</td>", "").replace("\n", "").replace("amp;",
                "").replace("<tr>", "").replace("<tr>","").replace("</tr>", "").split("<td>")
        if lunTd[0] == "" :
            lunTd.remove("")

        dinTd = str(dinBox).replace("\t", "").replace("\r", "").replace("</td>", "").replace("\n", "").replace("amp;",
                "").replace("<tr>", "").replace("<tr>","").replace("</tr>", "").split("<td>")
        if dinTd[0] == "":
            dinTd.remove("")

        #월 = 0 ~ 일 = 6
        today = time.localtime().tm_wday


        if today == 5 or today == 6 :
            print("토요일과 일요일은 운영하지 않아요~!")
        else :
            try :
                lun = lunTd[today].split(",")
            except :
                lun = "점심 식단이 없습니다."

            try :
                din = dinTd[today].split(",")
            except :
                din = "저녁 식단이 없습니다."

            print("- 웰스프레시 점심메뉴 -")
            for item in lun :
                print(item)
            print()
            print("- 웰스프레시 저녁메뉴 -")
            for item in din:
                print(item)
            print("본 정보는 한국산업기술대학교 홈페이지 정보를 바탕으로 제공됩니다.")
    except :
        print("금일 학식정보가 업로드 되지 않았어요.")
