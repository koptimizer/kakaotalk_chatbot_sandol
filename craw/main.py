import game
import station
import wheather

def noFunc():
    print("구현이 안됬어요 ㅜ")

def funcText():
    print("-----------기능-----------")
    print("학식 식단표 : 학식, ㅎㅅ")
    print("인근역 막차 : 막차, ㅁㅊ")
    print("셔틀 시간표 : 셔틀, ㅅㅌ")
    print("정왕역 날씨 : 날씨, ㄴㅆ")
    print("학사 공지 : 공지, ㄱㅈ")
    print("게임전적검색 : 게임, ㄱㅇ")
    print("ㄴ 현재 지원되는 게임 : 롤, 메이플, 배그")
    print("산돌이 끄기 : 산바, ㅅㅂ")

def start() :
    print("-------산돌이 v0.1-------")
    print("기능 소개는 기능, ㄱㄴ을 입력하세요.")
    inp = ''
    while 1 :
        inp = input()
        if inp == '기능' or inp == 'ㄱㄴ':
            funcText()
        elif inp == '학식' or inp == 'ㅎㅅ':
            noFunc()
        elif inp == '막차' or inp == 'ㅁㅊ':
            station.station()
        elif inp == '셔틀' or inp == 'ㅅㅌ':
            noFunc()
        elif inp == '날씨' or inp == 'ㄴㅆ':
            wheather.wheather()
        elif inp == '공지' or inp == 'ㄱㅈ':
            noFunc()
        elif inp == '게임' or inp == 'ㄱㅇ':
            inp2 = input("롤? 메이플? 옵치? 배그?")
            if inp2 == "롤" or inp2 == "ㄹ" :
                game.lol()
            elif inp2 == "메이플" or inp2 == "ㅁㅇㅍ" or inp2 == "메이플스토리" :
                game.maple()
            elif inp2 == "오버워치" or inp2 == "옵치" or inp2 == "ㅇㅊ" or inp2 == "ㅇㅂㅇㅊ":
                game.overwatch()
            elif inp2 == "배그" or inp2 == "ㅂㄱ" :
                game.pubg()
            else :
                print("무슨 게임 말하는 거에요??")
        elif inp == '산바' or inp == 'ㅅㅂ':
            print("이용해줘서 감사해요!")
            break
        else :
            print("무슨 말인지 모르겠어요!")

start()