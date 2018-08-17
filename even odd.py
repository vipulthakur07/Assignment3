a=[]
odd=0
even=0
size=int(input("enter the size ot the list: "))
for i in range(0,size):
    b=int(input(""))
    a.append(b)
    if b%2==0:
        even+=1
    else:
        odd+=1;
print("list is :",a)
print("list contains %d odd and %d even numbers."%(odd,even))
