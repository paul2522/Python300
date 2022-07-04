#101
#bool type
#102
print(3==5)
#False
#103
print(3<5)
#True
#104
x = 4
print(1 < x < 5)
#True
#105
print ((3 == 3) and (4 != 3))
#True
#106
#print(3 => 4)
#부등호가 등호 앞에 나와야함
#107
if 4 < 3:
    print("Hello World")
 #아무것도 출력되지않는다
 #108
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")
#Hi. there.  출력
#109
if True:
    print ("1")
    print ("2")
else:
    print("3")
print("4")
#출력 1 2 4
#110
if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")
#3 5

#111
string111 = input()
print(string111*2)
#112
int112 =input()
int112 = int(int112)
print(int112 +10)
#113
int113 = input()
int113= int(int113)
if int113%2 == 0:
	print('짝수')
else:
	print('홀수')
#114
int114 = input('입력값: ')
int114 = int(int114)
int114 += 20
if int114 > 255:
	int114 = 255
print('출력값:', int114)
#115
int115 = input('입력값: ')
int115 =int(int115)
int115 -= 20
if int115 > 255:
	int114 =255
elif int115 < 0:
	int115 = 0
print('출력값:', int115)
#116
time116 = input('현재시간: ')
time116 =int(time116[-2:])
if time116 == 0:
	print('정각입니다.')
else:
	print('정각이 아닙니다.')
#117
fruit117 = ["사과", "포도", "홍시"]
string117 = input('좋아하는 과일은?')
if string117 in fruit117:
	print('정답입니다.')
else:
	print('오답입니다.')
#118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
investment = input('투자 종목 입력:')
if investment in warn_investment_list:
	print('투자 경고 종목입니다.')
else:
	print('투자 경고 종목이 아닙니다.')
#119
fruit119 = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
	
