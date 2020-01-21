import requests
from bs4 import BeautifulSoup

def station() :
    url = 'https://search.naver.com/search.naver?query='
    station = ''

    # #사용자에게 입력받은 값으로 역 설정
    while 1:
        num = input("정왕역 = 1 / 오이도역 = 2")
        if num == "1" :
            station = "정왕역막차"
            break
        elif num == "2" :
            station = "수인선오이도역막차"
            break
        else :
            print("잘못 입력했어요. 다시 입력하세요.")

    url += station
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    if station == '정왕역막차' :
        table_div = soup.find_all("tbody")

        table_4_body = table_div[5]
        table_su_body = table_div[7]

        tr_4_sta = table_4_body.find_all("p")
        tr_su_sta = table_su_body.find_all("p")

        text_4_sta = []
        for item in tr_4_sta :
            text_4_sta += item

        text_su_sta = []
        for item in tr_su_sta :
            text_su_sta += item

        print("정왕역 막차 정보입니다!")
        print("종 착 역  / 평 일 /  주말 및 공휴일")
        print("당고개행 :", text_4_sta[5], text_4_sta[6])
        print("사 당 행 :", text_4_sta[13], text_4_sta[14])
        print("금 정 행 :", text_4_sta[17], text_4_sta[18])
        print("오이도행 :", text_su_sta[11], text_su_sta[12])
        print("본 정보는 네이버 검색 결과를 바탕으로 제공됩니다.")
    elif station == '수인선오이도역막차' :
        table_div = soup.find_all("tr", {"class" : "last"})
        table_tr = table_div[1]

        text_su_sta = []
        for item in table_tr :
            if item != " " :
                text_su_sta += item

        text_sta = []
        for item in text_su_sta :
            text_sta += item

        print("오이도역(수인선) 막차 정보입니다!")
        print("종 착 역  / 평 일 /  주말 및 공휴일")
        print("인 천 행 :", text_sta[1], text_sta[2])
        print("본 정보는 네이버 검색 결과를 바탕으로 제공됩니다.")

