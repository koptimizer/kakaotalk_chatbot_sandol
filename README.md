
<img src = "https://github.com/KGJsGit/sandol_bot/blob/master/%EC%82%B0%EB%8F%8C%EC%9D%B4jpeg.jpg?raw=true">

## 🤖 한국산업기술대학교 챗봇 산돌이
```
안녕하세요! 한국산업기술대학교 챗봇 산돌이입니다!
교내외 학식메뉴, 셔틀시간표, 학교 날씨, 인근역 막차 시간표 등 다양한 정보를 제공합니다!
```
- 개발 및 디자인 : 16' IT경영학과 고광종
  - Github = https://github.com/KGJsGit
  - Email = rhkswhdwkd@naver.com // ilovecoding@kakao.com
- 카카오톡 친구추가 URL : http://pf.kakao.com/_pRxlZxb/chat
- Since 20.01.03
<img src = "https://github.com/KGJsGit/kakaotalk_chatbot_sandol/blob/master/%EC%BA%A1%EC%B2%981.JPG?raw=true">
<img src = "https://github.com/KGJsGit/kakaotalk_chatbot_sandol/blob/master/%EC%BA%A1%EC%B2%98.JPG?raw=true">
<br/>

## 📃 작동 방식
1. 매일 00:00 : 필요정보 크롤링(학식식단, 막차시간, 정왕역날씨, 학사공지)후, 파싱해서 서버 DB에 업로드(python, mySql)<br/>
  ㄴ 외부식당메뉴는 각 식당 사장님들이 산돌이에게 직접 메뉴 업로드(사장님들의 고유ID 식별)

2. 사용자 발화시, kakao openbuilder에서 의도를 캐치하고 해당 skil을 통해 DB에 업로드된 내용을 파싱해서 response

3. 사용자 발화 의도를 캐치하지 못하면, 도움말 바로가기 버튼을 생성해줌으로서 사용자 편의성 고려
<br/>


## 🔎 구현 상황(20.03.09)
- [x] 셔틀 시간표 조회(img)
- [x] 금일 학식 및 외부 식당 식단 조회
    - [x] 썬푸드 학식
    - [x] E동 식당
    - [ ] TIP 한식당 (사장님이 허락안해주셔서 보류중)
    - [x] 세미콘
    - [x] 미가
- [x] 요일별 인근역(정왕역, 오이도역) 막차 시간 조회
- [ ] 인근정류장 및 전철역의 실시간 상황 조회
- [x] 금일 정왕동 날씨 조회
- [x] 학교 시설물 및 장소 조회
    - [x] 공부 및 스터디장소
    - [x] 휴게장소
    - [x] 큐브 위치
- [ ] 학교 공지 조회 
    - [x] 학사공지 
- [ ] 게임 정보 조회
    - [x] LoL 인게임 전적 및 티어조회
    - [x] MapleStory 인게임 캐릭터 정보 및 룩 조회
- [ ] 후원 및 건의
    - [x] 산돌이 건의
    - [x] 후원 등록
<br/>

## 🔧 이슈 사항(20.05.13)
- 크롤링해야하는 대부분의 정보(셔틀, 교내학식 등)가 flash기반으로 웹에 표현되서 해당 정보는 크롤링이 아예 안됨.
  - 셔틀은 어짜피 자주 바뀌는 항목이 아니니 내가 수동으로 입력
  - 학식은 일주일 단위로 식단표가 나오니 1주일에 한번씩 수동으로 개인 홈페이지에 올리고 크롤링.
- 외부 식당끼리의 메뉴 조회 금지 및 식단 수정기능 필요
  - 외부식당 사장님이 '학식조회' 관련 발화을 하면 고유 ID를 식별해서 타 외부 식당을 제외하고 출력하도록 함
  - 위의 기능을 조금 수정해서 메뉴수정의 기능 추가
- 기존에 사용하던 AWS EC2의 서버비용 문제 및 자원성능
  - 연구실 서버로 스킬서버 이전 예정
  - 연구실 서버가 아직 없어서 미뤄짐... EC2 다시 파서 스킬올려놔야할듯...ㅠ
  - 우선 수동으로 업데이트
<br/>
