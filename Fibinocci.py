def fibinocci(n):
    a=0
    b=1
    if a<0:
        print("incorrect value")
    elif n==0:
        return a
    elif n==1:
        return 1
    else:
        for i in range(2,n):
            c=a+b
            a=b
            b=c
        return b
num=int(input())
print(fibinocci(num))
