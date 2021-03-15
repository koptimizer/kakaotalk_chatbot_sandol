import json
import requests
import re
from datetime import datetime, timedelta, timezone
from bs4 import BeautifulSoup

def weather(location) :
    result = ''
    aria = location
    try :

        url = 'https://search.naver.com/search.naver?query='
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

        if today_com.split(',')[0] == '눈' or today_com.split(',')[0] == '비' or today_com.split(',')[0] == '흐림' :
            today_rain_box = soup.find_all("span", {"class" : "rainfall"})
            today_rain_det = []
            for item in today_rain_box:
                today_rain_det += item
            today_rayorrain = today_rain_det[0]
            today_rayorrain_value = str(today_rain_det[1]).split(">")[2].split("<")[0]

        else :
            today_ray_box = soup.find_all("span", {"class" : "indicator"})
            today_ray_det = []
            for item in today_ray_box:
                today_ray_det += item
            today_rayorrain = today_ray_det[0]
            today_rayorrain_value = str(today_ray_det[1]).split(">")[2].split("<")[0]
            today_rayorrain_value += " "+str(today_ray_det[1]).split(">")[3].split("<")[0]

        #먼지박스
        today_dust_box = soup.find_all("dl", {"class" : "indicator"})
        today_dust_det = []
        for item in today_dust_box:
            today_dust_det += item

        today_sdust = str(re.sub('<.+?>',' ',str(today_dust_det[3]),0).strip())
        today_gdust = str(re.sub('<.+?>',' ',str(today_dust_det[7]),0).strip())
        today_oz = str(re.sub('<.+?>',' ',str(today_dust_det[11]),0).strip())

        result += (datetime.now(timezone.utc) + timedelta(hours=9)).strftime("%Y-%m-%d %H:%M:%S \n")
        result += aria + "의 날씨입니다.\n"
        result += "금일 평균기온 : " + str(today_temp) +"˚c\n"
        result += "금일 최고기온 : " + str(today_max_temp) +"˚c\n"
        result += "금일 최저기온 : " + str(today_min_temp) +"˚c\n"
        result += "현재 " + str(today_com.replace("˚","˚c")) + '\n\n'
        result += str(today_rayorrain) + ": " + str(today_rayorrain_value) + '\n'
        result += "미세먼지 : " + str(today_sdust) + '\n'
        result += "초미세먼지 : " + str(today_gdust) + '\n'
        result += "오존 : " + str(today_oz) + '\n\n'
        result += "본 정보는 네이버 검색 결과를 바탕으로 제공됩니다."
    except :
        result += "지역을 찾을 수 없거나 동일한 지역명이 여러개 존재해요!\n"
        result += "ex)부평동 -> 부산부평동 or 부평구부평동"

    return result
    
def lambda_handler(event, context):

    # 메시지 내용은 request의 ['body']에 들어 있음
    request_body = json.loads(event['body'])
    params = request_body['action']['params']
    location = params['location']
    answer = weather(str(location))

    result = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer
                    }
                }
            ]
        }
    }

    return {
        'statusCode':200,
        'body': json.dumps(result),
        'headers': {
            'Access-Control-Allow-Origin': '*',
        }
    }
