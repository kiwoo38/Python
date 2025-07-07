import random
random.seed()
s="abcdefghijklmnopqrstuvwxyz"
base_s=[]

base_s=random.sample(s,26)
password=[]
password_hint=list(zip(s,base_s))
print(password_hint)
str=input("사용자 입력: ")

for letter in str:
    for i in range(26):
        if letter==password_hint[i][0]:
            password.append(password_hint[i][1])

print(password)
result=""

input_str2=input("암호화된 문자열 입력: ")
 
for letter2 in input_str2:
    for i in range(26):
        if letter2==password_hint[i][1]:
            result+=password_hint[i][0]
            break
print(result)