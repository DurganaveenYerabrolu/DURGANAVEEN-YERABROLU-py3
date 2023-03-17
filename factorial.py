n=int(input("enter the number:"))
fact=1
if n<=0:
    print("it is invalid")
elif n==1:
    print(1)
else:
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
num=int(input("enter the number:"))
def fac(num):
    if num==1:
        return 1
    else:
        return (num*fac(num-1))
result=fac(num)
print(result)
   
