#Python 300
# #001
# print('Hello')
# #002
# print("Mary's cosmetics")
# #003
# print('신씨가 소리질렀다. "도둑이야".')
# #004
# print('"C:\Windows"')
# #005
# print("안녕하세요.\n만나서\t\t반갑습니다.")
# #\n:줄바꿈, \t : 탭
# #006
# print ("오늘은", "일요일")
# #오늘은 일요일
# #007
# print('naver','kakao','sk','samsung',sep = ';')
# #008
# print('naver','kakao','sk','samsung',sep = '/')
# #009
# print("first",end = " ");print("second")
# #010
# print(5/3)

# #011
# 삼성전자 = 50000
# 평가금액 = 삼성전자 * 10
# print(평가금액)
# #012
# 시가총액 = '298조'
# 현재가 = 50000
# PER = 15.79
# #013
# s = "hello"
# t = "python"
# print(s,t,sep ="! ")
# #print(s+"!",t)
# #014
# print(2 + 2 * 3)
# #예측 : 8
# #015
# a = "132"
# print(type(a))
# #str
# #016
# num_str = "720"
# num_str = int(num_str)
# #017
# num017 = 100
# num017 = str(num017)
# #018
# num018 = "15.79"
# num018 = float(num018)
# #019
# year019 = "2020"
# year019 = int(year019)
# for i in range(1,4):
#     print(year019 - i)
# #020
# 월020 = 48584
# print(월020 * 36)

# #021
# letters021 = 'python'
# print(letters021[0],letters021[2])
# #022
# license_plate = "24가 2210"
# print(license_plate[-4:])
# #023
# string023 = "홀짝홀짝홀짝"
# print(string023[::2])
# #024
# string024 = "PYTHON"
# print(string024[::-1])
# #025
# phone_number = "010-1111-2222"
# phone_number = phone_number.replace("-"," ")
# print(phone_number)
# #026
# phone_number = phone_number.replace(" ","")
# print(phone_number)
# #027
# url = "http://sharebook.kr"
# print(url[-2:])
# #ulr_split = url.split('.')
# #print(url_split)
# #28
# lang = 'python'
# #lang[0] = 'P'
# print(lang)
# #타입 에러 문자열은 item assignment 안됨
# #29
# string029 = 'abcdfe2a354a32a'
# string029 = string029.replace('a','A')
# print(string029)
# #30
# string = 'abcd'
# string.replace('b', 'B')
# print(string)
# #abcd replace한걸 다시 지정안해줬기 때문

# #031
# a = "3"
# b = "4"
# print(a + b)
# #예상 34
# #032
# print("Hi" * 3)
# #HiHiHi
# #033
# print("-" * 80)
# #034
# t1 = 'python'
# t2 = 'java'
# print((t1 + " " +  t2 + " ")* 4)
# #035
# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print('이름: %s 나이: %d' % (name1,age1))
# print('이름: %s 나이: %d' % (name2,age2))
# #036
# print('이름: {} 나이: {}' .format(name1,age1))
# print('이름: {} 나이: {}' .format(name2,age2))
# #37
# print(f'이름: {name1} 나이: {age1}')
# print(f'이름: {name2} 나이: {age2}')
# #38
# 상장주식수 = "5,969,782,550"
# 상장주식수 = int(상장주식수.replace(',',''))
# print(상장주식수, type(상장주식수))
# #39
# 분기 = "2020/03c(E) (IFRS연결)"
# print(분기[0:7])
# #40
# data040 = "   삼성전자    "
# data040 = data040.strip()
# print(data040)

# #041
# ticker041 = "btc_krw"
# ticker041 = ticker041.upper()
# print(ticker041)
# #042
# ticker042 = "BTC_KRW"
# ticker042 = ticker042.lower()
# print(ticker042)
# #043
# string043 = 'hello'
# string043 = string043.capitalize()
# print(string043)
# #044
# file_name044 = "보고서.xlsx"
# if file_name044.endswith('xlsx'):
#     print(file_name044 + "는 xlsx로 끝납니다.")
# #045
# #if file_name044.endswith('xlsx','xls'):
# #한개만 넣을 수 있고 튜플로 넣을 수 있다.
# if file_name044.endswith(('xlsx','xls')):
#     print(file_name044 + "는 xlsx 또는 xls로 끝납니다.")
# #046
# file_name046 = "2020_보고서.xlsx"
# if file_name046.startswith('2020'):
#     print(file_name046 + '는 2020으로 시작합니다')
# #047
# a047 = "hellow world"
# # a047_0 = a047.split(" ",0)
# # a047_1 = a047.split(" ",1)
# # print(a047 + "는 ",a047_0 + "와",a047_1 + "로 나뉩니다." )
# a047_split = a047.split()
# print(a047 + "는 ",a047_split[0] + "와",a047_split[1] + "로 나뉩니다." )
# #048
# ticker048 = "bet_krw"
# ticker048 = ticker048.split(sep="_")
# print(ticker048[0], ticker048[1],sep = '와 ')
# #049
# date049 = "2020-05-01"
# date049 = date049.split(sep = "-")
# print(date049[0], date049[1], date049[2], sep = ", ")
# #050
# data050 = "039490     "
# data050.rstrip()

#051
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
# print(*movie_rank)
# #출력시 리스트앞에 * 넣으면 []랑 '' 빼고 전체 출력 가능
# #052
# movie_rank.append('배트맨')
# #append는 리스트로 추가하면 1요소가 리스트임, extend는 그냥 늘어서 붙이기, +는 extend 처럼 되는데 list id가 바뀜(append랑 extend는 안바뀜)
# print(*movie_rank)
# #053
# superman = '슈퍼맨'
# movie_rank.insert(1,superman)
# print(*movie_rank)
# #054
# movie_rank.remove('럭키')
# #del movie_rank[3]
# print(*movie_rank)
# #055
# #movie_rank.remove(['스플릿','배트맨'])
# #movie_rank.remove('스플릿')
# #movie_rank.remove('배트맨')
# del movie_rank[2:]
# print(*movie_rank)
# #제거함수들 차이 : del은 인덱스 삭제 및 슬라이스 사용 가능 여러개 제거가능, remove는 해당 삭제, pop은 삭제한 element 리턴
# #056
# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]
# lang = lang1 + lang2
# print(*lang)
# #057
# nums057 = [1, 2, 3, 4, 5]
# print("max  :", max(nums057), "min :", min(nums057))
# #058
# nums058 =  [1, 2, 3, 4, 5]
# print("sum =", sum(nums058))
# #059
# cook059 = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
# print(len(cook059))
# #060
# nums060 = [1, 2, 3, 4, 5]
# print(sum(nums060)/len(nums060))

# #061
# price061 = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price061[1:])
# #062
# nums062 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums062[::2])
# #063
# nums063 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums063[1::2])
# #064
# nums064 = [1, 2, 3, 4, 5]
# print(nums064[::-1])
# #065
# interest065 = ['삼성전자', 'LG전자', 'Naver']
# print(*interest065[::2])
# #print(interest065[0], interest065[2])
# #066
# interest066 = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(*interest066,sep = " ")
# #print(" ".join(interest066))
# #문자열.join(리스트) : 리스트를 쭉 문자열을 사잇값으로 두고 쭉 나열
# #067
# print("/".join(interest066))
# #068
# print("\n".join(interest066))
# #069
# string069 = "삼성전자/LG전자/Naver"
# interest069 =string069.split('/')
# print(interest069)
# #070
# data070 = [2, 4, 3, 1, 5, 10, 9]
# #print(data.sort())
# #sort는 none을 리턴시켜줌, sorted는 정렬된 리스트를 리턴함
# print(sorted(data070))
# #오름차순
# #print(sorted(data070,reverse=True))

# #071
# my_variable = ()
# #072
# movie_rank072 = ('닥터 스트레인지', '스플릿', '럭키')
# #073
# tuple073 = (1)
# #tuple073 = (1,)
# #074
# #튜플은 수정불가
# #075
# #괄호없이 선언되는게 튜플이기도하다
# #076
# t076 = ('a', 'b', 'c')
# print(t076)
# t076 = ('A', 'B', 'C')
# print(t076)
# #077
# interest077 = ('삼성전자', 'LG전자', 'SK Hynix')
# interest077 = list(interest077)
# print(interest077)
# #078
# interest078 = ['삼성전자', 'LG전자', 'SK Hynix']
# intereset078 = tuple(interest078)
# print(intereset078)
# #079
# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)
# #apple, banana, cake
# #080
# tuple080 = tuple(range(2,100,2))
# print(tuple080)

# #081
# scores081 = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_score081, a, b= scores081
# print(valid_score081)
# #start experssion
# #082
# scores082 = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a,b,*valid_score082 = scores082
# print(valid_score082)
# #083
# scores083 = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a,*valid_score083,b = scores083
# print(valid_score083)
# #084
# temp084 = { }
# #085
# dic085 = {'메로나' : 1000, '폴라포' : 1200, '빵빠레' : 1800}
# print(dic085)
# #086
# dic086 = dic085.update({'죠스바' : 1200, '월드콘' : 1500})
# print(dic085)
# # 정답
# # ice["죠스바"] = 1200
# # ice["월드콘"] = 1500
# #087
# ice087 = {'메로나': 1000, '폴로포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
# print("메로나 가격:", ice087['메로나'])
# #088
# ice088 = {'메로나': 1000, '폴로포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
# ice088["메로나"] = 1300
# print(ice088)
# #089
# ice089 = {'메로나': 1000, '폴로포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
# ice089.pop("메로나")
# #del ice089["메로나"]
# print(ice089)
# #090
# #딕셔너리에 없는 키 인덱싱해서 에러발생

#091
inventory091 = dict(메로나 = [300,20], 비비빅 =  [400,3], 죠스바 = [250,100])
#inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
print(inventory091)
#092
inventory092 = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
print(inventory092["메로나"][0],'원')
#약간 2차원 배열 느낌
#093
inventory093 = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
print(inventory092["메로나"][1],'개')
#094
inventory094 = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
inventory094.setdefault('월드콘', [500,7])
#inventory094["월드콘"] =  [500,7]
print(inventory094)
#095
icecream095 = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream095_keys = list(icecream095.keys())
#리스트로 안만들어주면 dict_keys()하고 안에 list 들어가 있음
print(icecream095_keys)
#096
icecream096 = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream096_values = list(icecream095.values())
print(icecream096_values)
#097
print(sum(icecream096_values))
#098
icecream098 = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product098 = {'팥빙수':2700, '아맛나':1000}
icecream098.update(new_product098)
print(icecream098)
#099
keys099 = ("apple", "pear", "peach")
vals099 = (300, 250, 400)
result099 = dict(zip(keys099,vals099))
print(result099)
#100
data100 = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price100 = [10500, 10300, 10100, 10800, 11000]
close_table100 = dict(zip(data100,close_price100))
print(close_table100)