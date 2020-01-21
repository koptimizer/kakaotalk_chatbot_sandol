# OP.GG에서 소환사명을 입력받아 인게임 전적을 파싱하는 크롤러
import requests
from bs4 import BeautifulSoup
import re

def lol() :
	params = input("소환사 명 : ")
	url = 'https://www.op.gg/summoner/userName='
	target_url = url+params
	html = requests.get(target_url).text

	soup = BeautifulSoup(html, 'html.parser')

	#소환사명
	name = params

	try :
		#소환사 여부
		non_summoner = str(soup.find_all("h2", {"class" : "Title"})[0]).split(">")[1].split("<")[0]
		print(non_summoner)
	except :
		try :
			# 언랭 판별
			isUnranked = str(soup.find_all("div", {"class": "TierRank unranked"})[0]).split(">")[1].split("<")[0].strip()
			print(name, "소환사님 정보입니다.")
			print("Tier :", "Unranked")
			print("본 정보는 op.gg의 검색결과를 바탕으로 제공됩니다!")
		except :
			try :
				# 솔로랭크
				solo_tier = str(soup.find_all("div", {"class": "TierRank"})[0]).split(">")[1].split("<")[0].strip()
				solo_point = str(soup.find_all("span", {"class": "LeaguePoints"})[0]).split(">")[1].split("<")[0].strip().replace(" ", "")
				solo_wins = str(soup.find_all("span", {"class": "wins"})[0]).split(">")[1].split("<")[0].strip()
				solo_lose = str(soup.find_all("span", {"class": "losses"})[0]).split(">")[1].split("<")[0].strip()
				solo_rate = str(soup.find_all("span", {"class": "winratio"})[0]).split(">")[1].split("<")[0].strip()

				print(name, "소환사님 정보입니다.")
				print("-----솔로랭크-----")
				print('Tier :', solo_tier, solo_point)
				print('Win & Lose :', solo_wins, solo_lose)
				print('Raiting :', solo_rate, "\n")
			except:
				print("-----솔로랭크-----")
				print("Tier :", "Unranked")
			try :
				# 자유랭크
				free_tier = str(soup.find_all("div", {"class": "sub-tier__rank-tier"})[0]).split(">")[1].split("<")[0].strip()
				free_point = str(soup.find_all("div", {"class": "sub-tier__league-point"})[0]).split(">")[1].split("<")[0].strip()
				free_wins_lose = str(soup.find_all("span", {"class": "sub-tier__gray-text"})[0]).split(">")[1].split("<")[0].split("/")[
					1].strip()
				free_rate = str(soup.find_all("div", {"class": "sub-tier__gray-text"})[0]).split(">")[1].split("<")[0].strip().replace("승률", "Win Ratio")

				print("-----자유랭크-----")
				print('Tier :', free_tier, free_point)
				print('Win & Lose :', free_wins_lose)
				print('Raiting :', free_rate)
				print("본 정보는 op.gg의 검색결과를 바탕으로 제공됩니다!")
			except:
				print("-----자유랭크-----")
				print("Tier :", "Unranked")

def maple() :
	try :
		params = input("캐릭터 명 : ")
		url = 'https://maple.gg/u/'
		target_url = url + params
		html = requests.get(target_url).text

		soup = BeautifulSoup(html, 'html.parser')

		#레벨,직업,인기도
		user_mainInfo_box = soup.find_all("li", {"class":"user-summary-item"})
		#순위
		user_subInfo_box = soup.find_all("div", {"class":"col-lg-2 col-md-4 col-sm-4 col-6 mt-3"})
		#기타 기록 -> 필요 없을 듯해서 미구현
		#user_rankInfo_box = soup.find_all("div", {"class":"col-lg-3 col-6 mt-3 px-1"})

		name = params
		level = str(re.sub('<.+?>', '', str(user_mainInfo_box[0]), 0).strip())
		userClass = str(re.sub('<.+?>', '', str(user_mainInfo_box[1]), 0).strip())
		population = str(re.sub('<.+?>', '', str(user_mainInfo_box[2]), 0).strip()).replace("인기도","").strip()
		rank_all = str(re.sub('<.+?>', '', str(user_subInfo_box[0]), 0).strip()).replace("위","").strip()
		rank_world = str(re.sub('<.+?>', '', str(user_subInfo_box[1]), 0).strip()).replace("위","").strip().replace("\n","")
		rank_class_all = str(re.sub('<.+?>', '', str(user_subInfo_box[2]), 0).strip()).replace("위","").strip().replace("\n","")
		rank_class_world = str(re.sub('<.+?>', '', str(user_subInfo_box[3]), 0).strip()).replace("위","").strip().replace("\n","")
		guild = str(soup.find_all("div", {"class": "col-lg-2 col-md-4 col-sm-4 col-12 mt-3"})[0]).split(">")[4].split("<")[0]

		#미구현 항목(무릉, 시드, 유니온{유니온이 고렙 아니면 .gg에서 적용 안됨})
		#rank_murung = user_rankInfo_box.find_all("div", {"class" : "text-secondary"})
		#rank_seed = user_rankInfo_box.find_all("div", {"class" : "mb-3"})
		#union = user_rankInfo_box.find_all("div", {"class" : "mb-3"})
		#union_level = user_rankInfo_box.find_all("div", {"class" : "mb-3"})

		print("닉네임 :", name)
		print("레벨 :", level)
		print("직업 :", userClass)
		print("인기도 :", population)
		print("길드 :", guild)
		#print("유니온 :", union, union_level)
		#print("무릉 최고기록 :", rank_murung)
		#print("더 시드 최고기록 :", rank_seed)
		print(rank_all+"위")
		print(rank_world+"위")
		print(rank_class_world+"위")
		print(rank_class_all+"위")
		print("본 정보는 메이플.gg의 검색 결과를 바탕으로 제공됩니다.")
	except :
		print("캐릭터를 찾을 수 없어요...")