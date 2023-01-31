def factorial(n):
    start=1
    for i in range(2,n+1):
        start=start*i
    return start
number=int(input())
print(factorial(number))

