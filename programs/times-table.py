index=int(input("Enter a number you want the times table for:"))
timestable=[x+1 for x in range(index)]
for i in timestable:
    for j in timestable:
        output=i*j
        print("%s   " %(output),end='')
    print("\n")
    