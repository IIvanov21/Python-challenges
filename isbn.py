isbn_number=input("Enter ISBN:")
digit_12=0
index=0
for char in isbn_number:
    if (char == '-'):
         continue 
    a=int(char)
    if (index % 2==0):
        digit_12+=a
    else:
        digit_12+=(3*a)
    index+=1

digit_12=10-(digit_12%10)

print("Your ISBN is:" + isbn_number + '-' + str(digit_12))

