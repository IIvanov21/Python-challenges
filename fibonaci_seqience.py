def fibonaci(n):
    if n<=1:
        return n
    else:
        return(fibonaci(n-1)+fibonaci(n-2))


nterm=int(input("Please enter a number above 0: "))

if nterm <= 0:
    nterm=int(input("I told you something...:"))
else:
    print("Sequence: ")
    for i in range(nterm+1):
        print(fibonaci(i))