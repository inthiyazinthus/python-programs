s="mam"
palin=False
for i in range(int(len(s)/2)):
    if s[i]!=s[len(s)-i-1]:
        palin= False
    else:
        pal=True
if palin:
    print("is a palindrome")
else:
    print("is not a plaindrome")
