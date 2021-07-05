index=int(input("Enter a number you want the times table for:"))
timestable=[1,2,3,4,5,6,7,8,9,10]
for i in timestable:
    output=i*index
    print ("%s X % s = %s" %(i,index,output))