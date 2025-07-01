# 첫 글자만 대문자로 바꿈 .capitalize()
word="abcd"
new_word=word.capitalize()
print(new_word)

# 문자열 내부에 특정 문자가 몇개 포함되어 있는지 카운팅  .count()
# 문자열.count("특정문자",시작위치,마지막 위치)
word="helloworld"
print(word.count("o")) # 전체범위에서 찾을 때
print(word.count("o",1,3)) # 인덱스 1~2 범위에서 o있는지 확인하는 것. 

# 문자열 내에 존재하는 문자를 찾음 .find()
# 찾는 문자가 존재하는 위치(index)를 알려줌 
word="banana"
index=word.find("a")
print(index) # 인덱스 1
index=word.find("na")
print(index) # 인덱스 2 
index=word.find("na",3) # 두 번째 숫자는 찾기 시작하는 index number
print(index) # 인덱스 4
name="bob"
index=name.find("b",1,2) # 세 번째 숫자는 어디까지 찾을 지 지정하는 index number, 없으면 -1
print(index)

# string method  .join(), .split()
# join(): 문자열을 합쳐줌(리스트를 문자열로)   split(): 문자열을 나누어 리스트로 만들어 줌 
a=["1","2","h","a","n","d","o","n","g"]
result1="".join(a)
print(result1)
result2=result1.split() # 기본 split()은 공백문자(스페이스)를 기준으로 문자열을 쪼갭니다
print(result2)

# string method .isalpha()
a="A12"
b="AB C"
c="123"
for ch in a:
    print(ch.isalpha())
for ch in b:
    print(ch.isalpha())
for ch in c:
    print(ch.isalpha())

# string method .isdigit()
a="010-1234"
b="a1f3"
for ch in a:
    print(ch.isdigit())
for ch in b:
    print(ch.isdigit())

# string method .islower(), .isupper(), .isspace()
# islower(): 모든 요소가 소문자이면 True
# isupper(): 모든 요소가 대문자이면 True
# isspace(): 모든 요소가 공백이면 Trueß

# string methods  .lower() 모든 문자를 소문자로 바꿈
word="HELlo"
new_word=word.lower()
print(new_word)

# string methods .replace() 해당 문자를 변경 문자로 바꾸어줌
# 문자열.replace("검색문자", "변경문자")

feel="I'm so happly"
result=feel.replace("so","not")
print(result)
str="you are welcome"
result=str.replace("e","f")
print(result)

# string methods ,swapcase()
sentence="This is Python Class"
result=sentence.swapcase()
print(result)

#string methods .upper() 모든 문자를 대문자로 변환 
#string methods .find() 사용 찾는 문자 인덱스 반환
s="abcd cdef def gh"
if s.find("d")==-1:
    print("찾는 문자가 없음")
else:
    print(s.find("d"))
if s.find("f")==-1:
    print("찾는 문자가 없음")
else:
    print(s.find("f"))
if s.find("i")==-1:
    print("찾는 문자가 없음")
else:
    print(s.find("i"))

# .startswith() 
s="python methods, startswith"
print(s.startswith("p")) #True
print(s.startswith("py")) # True
print(s.startswith("python")) # True
print(s.startswith("y")) # False 

# .endswith() 
print(s.endswith("h")) # True 
print(s.endswith("th")) # True
print(s.endswith("with")) # True
print(s.endswith("s,")) # False 