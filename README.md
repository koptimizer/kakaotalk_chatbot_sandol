<img src = "https://github.com/koptimizer/kakaotalk_chatbot_sandol/blob/master/pics/sandol.jpg">

## 🤖 한국산업기술대학교 챗봇 산돌이
```
안녕하세요! 한국산업기술대학교 챗봇 산돌이입니다!
교내외 학식메뉴, 셔틀시간표, 학교 날씨, 인근역 막차 시간표 등 다양한 정보를 제공합니다!
```
- Develope & Design = 고광종
- Github = https://github.com/koptimizer
- Email = rhkswhdwkd@naver.com // ilovecoding@kakao.com
- 카카오톡 친구추가 URL : http://pf.kakao.com/_pRxlZxb/chat
- Since 20.01.03
<img src = 'https://github.com/koptimizer/kakaotalk_chatbot_sandol/blob/master/pics/cap.jpg'>
<br/>

## "카톡 챗봇으로 알찬 정보 " (본교 학보 490호 6면)
<img src = "https://github.com/koptimizer/kakaotalk_chatbot_sandol/blob/master/pics/news.jpg" height = "500px">
<br/>

## "우리 대학의 빛나는 주역" (본교 학보 509호 5면)
<img src = "https://github.com/koptimizer/kakaotalk_chatbot_sandol/blob/master/pics/news2.jpg" height = "500px">
<br/>

## 📃 작동 방식
1. 학식/외부식당의 경우 각 식당 사장님들의 고유 카카오 아이디 식별을 통해 메뉴를 업로드 받음.

2. 사용자 발화시, kakao openbuilder에서 의도를 캐치하고 해당 AWS lambda로 구현된 skil을 통해 해당 내용을 파싱해서 response

3. 사용자 발화 의도를 캐치하지 못하면, 도움말 바로가기 버튼을 생성해줌으로서 사용자 편의성 고려

4. 산돌이 관련 질문은 Issue에 남겨주세요!
<br/>

## 🔎 구현 상황(21.03.29)
- [x] 셔틀 시간표 조회(img)
- [x] 금일 학식 및 외부 식당 식단 조회
    - [x] 썬푸드 학식
    - [x] E동 식당
    - [x] TIP 한식당
    - [x] 세미콘
    - [x] 미가
- [x] 요일별 인근역(정왕역, 오이도역) 막차 시간 조회
- [ ] 인근정류장 및 전철역의 실시간 상황 조회
- [x] 금일 정왕동 날씨 조회
- [x] 학교 시설물 및 장소 조회
    - [x] 공부 및 스터디장소
    - [x] 휴게장소
    - [x] 큐브 위치
- [x] 학교 내선번호 안내
- [x] 대학로 먹거리 추천
- [x] 학교 공지 조회
    - [x] 학사공지 
- [ ] 게임 정보 조회 (적용 검토중)
    - [x] LoL 인게임 전적 및 티어조회
    - [x] MapleStory 인게임 캐릭터 정보 및 룩 조회
- [x] 후원 및 건의
    - [x] 산돌이 건의
    - [x] 후원 등록
<br/>

## 🔧 산돌팀21
- 21.03.02 이후 산돌이의 관리 및 지속가능한 서비스 구현을 위해서 산돌팀21을 만들어 활동하고 있습니다.
  - [**고광종**](https://github.com/koptimizer) - <rhkswhdwkd@naver.com>
    산돌팀21 총괄 및 경영
  - [**박준하**](https://github.com/Cycrypto) - <jh01love@naver.com>
    산돌이 스킬 및 로직파트 메인개발
  - [**이지호**](https://github.com/DPS0340) - <optional.int@kakao.com>
    산돌이 데브옵스 및 보조개발, 웹 서비스 플랫폼 검토
  - [**허민**](https://github.com/hhhminme) - <huhmn0409@naver.com>
    경영지원 및 프론트엔드 개발
- 산돌팀21 체제 전환 이후, Github action을 이용한 CI/CD 파이프라인으로 스킬들을 관리하고 있습니다.
  - [관련 Repository 바로가기](https://github.com/hhhminme/kpu_sandol_team)
<br/>

## 🎓 챗봇강좌문의
- rhkswhdwkd@naver.com
