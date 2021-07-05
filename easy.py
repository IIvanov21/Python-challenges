#print("Welcome to Grade Calculator!")
mathMark = int(input("Please enter your mark:"))
chemistryMark = int(input("Please enter your mark:"))
physicsMark = int(input("Please enter your mark:"))

finalMark = ((mathMark+chemistryMark+physicsMark)/300)*100

if finalMark >= 70:
    print("You scored a grade of: A")
elif finalMark >= 60 and finalMark < 70:
    print("You scored a grade of: B")
elif finalMark >= 50 and finalMark < 60:
    print("You score a grade of: C")
elif finalMark >= 40 and finalMark < 50:
    print("You score a grade of: D")
else :
    print("You failed!")