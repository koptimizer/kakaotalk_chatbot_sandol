import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup

def wheather() :
    try :
        url = 'https://search.naver.com/search.naver?query='
        aria = ''

        # #사용자에게 입력받은 값으로 역 설정
        aria = input("어떤 지역 날씨를 보여드릴까요?")
        aria = aria.replace("날씨", "")
        url += (aria+"날씨")

        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')

        #지역정보
        aria_det_box = soup.find_all("span", {"class" : "btn_select"})
        aria_det_det = []
        for item in aria_det_box :
            aria_det_det += item
        aria_det = str(aria_det_det[0]).split(">")[1].split("<")[0]

        #기온박스
        today_temp_box = soup.find_all("span", {"class" : "todaytemp"})
        today_temp_det = []
        for item in today_temp_box :
            today_temp_det += item
        today_max_temp = str(today_temp_det[2])
        today_min_temp = str(today_temp_det[1])
        today_temp = str(today_temp_det[0])

        #코멘트박스
        today_com_box = soup.find_all("p", {"class" : "cast_txt"})
        today_com_det = []
        for item in today_com_box :
            today_com_det += item
        today_com = str(today_com_det[0])

        #자외선박스
        today_ray_box = soup.find_all("span", {"class" : "lv1"})
        today_ray_det = []
        for item in today_ray_box:
            today_ray_det += item
        today_ray = str(today_ray_det[1]).strip()

        #먼지박스
        today_dust_box = soup.find_all("dl", {"class" : "indicator"})
        today_dust_det = []
        for item in today_dust_box:
            today_dust_det += item

        today_sdust = str(re.sub('<.+?>','',str(today_dust_det[3]),0).strip())
        today_gdust = str(re.sub('<.+?>','',str(today_dust_det[7]),0).strip())
        today_oz = str(re.sub('<.+?>','',str(today_dust_det[11]),0).strip())

        print(datetime.today().strftime("%Y%m%d"))
        print(aria_det, "의 날씨입니다.")
        print("금일 평균기온 :", today_temp+"˚c")
        print("금일 최고기온 :", today_max_temp+"˚c")
        print("금일 최저기온 :", today_min_temp+"˚c")
        print("오늘은", today_com.replace("˚","˚c"))
        print("")
        print("자외선 :", today_ray)
        print("미세먼지 :", today_sdust)
        print("초미세먼지 :", today_gdust)
        print("오존 :", today_oz)
        print("본 정보는 네이버 검색 결과를 바탕으로 제공됩니다.")
    except :
        print("지역을 찾을 수 없거나 동일한 지역명이 여러개 존재해요!")
        print("ex)부평동 -> 부산부평동 or 부평구부평동")