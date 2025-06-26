#내가 좋아하는 것 10개의 이름을 한 줄에 하나씩 보여주기
num1="축구"
num2="고양이"
num3="휴대폰"
num4="토레타"
num5="치킨"
num6="바다"
num7="커피"
num8="유튜브"
num9="음악"
num10="영화"
list=[num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]

for i in list:
    print(i)
    print("*"*20) # 출력 후 줄 구분을 위한 특수 기호 

# 사용자에게 원하는 것을 고르라고 하기(q를 입력하지 않으면 질문 무한 반복)
# 종료조건: 사용사자 q를 입력 했을 때 
user_input=""
while user_input!="q":
    user_input=input("원하는 것을 고르시오, 종료를 원하면 q를 입력하세요 :")
     # q를 입력하면 끝인사 메시지 출력 후 프로그램 종료 
    if user_input=="q":
        print("종료되었습니다. 감사합니다!")
    # 해당하는 문자열을 입력하면 상세내용 출력 
    elif user_input=="축구":
        print("제가 좋아하는 운동은 축구입니다.")
    elif user_input=="고양이":
        print("제가 좋아하는 동물은 고양이입니다.")
    elif user_input=="휴대폰":
        print("휴대폰이 없으면 일상생활이 많이 불편합니다.")
    elif user_input=="토레타":
        print("제가 자주 마시는 음료는 토레타입니다.")
    elif user_input=="치킨":
        print("제가 자주 먹는 배달 음식은 치킨입니다.")
    elif user_input=="바다":
        print("저는 바다에서 파도치는 경치를 구경하는 것을 좋아합니다.")
    elif user_input=="커피":
        print("저는 식사 후 아이스아메리카노를 마시는 것을 좋아합니다.")
    elif user_input=="유튜브":
        print("저는 휴식시간에 유튜브를 자주 봅니다.")
    elif user_input=="음악":
        print("저는 음악 듣는 것을 좋아합니다.")
    elif user_input=="영화":
        print("저는 생각을 많이 할 수 있는 영화를 좋아합니다.")