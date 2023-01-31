number=int(input())
assume=False
if number > 1:
    for i in range(2,number):
        if(number%i)==0:
            assume= True
            break
    if assume:
        print("is prime")
    else:
        print("is not a prime")