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

# 좋아하는 것 10개의 이름을 한 줄에 모두 출력하기 위해 반복문을 사용하여 단어를 result에 하나씩 붙인다
result=""
for i in list:
    result+=i+" "
print(result)

## 잘못된 문자열을 입력하면 바로 종료하기 위한 flag 
flag=True

# 사용자에게 원하는 것을 고르라고 하기
user_input=input("원하는 것을 고르시오 :")
# 해당하는 문자열을 입력하면 상세내용 출력 
if user_input=="축구":
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
else:
    print("잘못된 이름입니다! 프로그램을 종료합니다.")
    flag=False

# flag가 True이면 두번째 질문 실행    
if flag:
    # 두번째 질문 종료 조건 b나 f를 입력하지 않았을 때 
    while True:
        user_two=input("두 번째 질문 b 또는 f를 입력하세요: ")
        # 두 번째 질문 입력 값이 b이거나 f이면 두 번째 질문 반복.
        if user_two=="b" or user_two=="f":
            continue
        else:
            print("잘못된 값이 입력되었습니다. 프로그램을 종료합니다!")
            break