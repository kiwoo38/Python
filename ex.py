def merge(a,b):
    new_list=[]
    for i in a:
        new_list.append(i)
    for j in b:
        new_list.append(j)
    return new_list,len(new_list)

a=["handong","global","university"]
b=[3,8,1,5]

new_list,length=merge(a,b)
print("두 리스트를 병합한 결과는",new_list)
print("리스트의 길이는",length)