import requests
from bs4 import BeautifulSoup
import re

def notice() :
    url = 'http://www.kpu.ac.kr/front/boardlist.do?currentPage=1&menuGubun=1&siteGubun=14&bbsConfigFK=1&searchField=ALL' \
          '&searchValue=&searchLowItem=ALL'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    title_box = soup.find_all("span" , { "class" : "text" })

    titles_box = []
    for item in title_box :
        titles_box += item

    # 학사 공지 1페이지 전체 제목 리스트
    titles = []
    for item in range(len(titles_box)) :
        titles.append(titles_box[item].replace("\r", "").replace("\n", "").replace("\t", ""))

    dates = []
    for item in range(len(title_box)) :
        dates.append(str(soup.select("body > form:nth-child(1) > div > div.bbs.list.mt15.bt1 > table > tbody > "
                                     "tr:nth-child("+str(item+1)+") > td:nth-child(5)")[0]).split(">")[1].split("<")[0])

    #1페이지 전체 출력...
    print("학사공지 1페이지 자료입니다.")
    for item in range(len(titles)):
        print(dates[item], ":", titles[item])
    print("자세한 사항은 학사공지를 참조하세요!")
    print("본 정보는 한국산업기술대학교 홈페이지를 바탕으로 제공됩니다.")