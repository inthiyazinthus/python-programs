l=[22,56,76,89,94,23,100,43,76]
m=[]
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i]>l[j]:
            l[i], l[j] = l[j], l[i]
print(l)