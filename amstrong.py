number=int(input())
power=0
for i in str(number):
    power=power+1
sum=0
for i in str(number):
    sum=sum+int(i)**power
if sum==number:
    print("Amstrong")
else:
    print("Not an Amstrong")