def even_digits(digit_one,digit_two):
    even_list=[]
    for i in range(digit_one,digit_two+1):
      for j in map(int, str(i)):
          if j % 2: break
      else : even_list.append(str(i))
    return ",".join(even_list)
   

if __name__ == "__main__":
    n1=int(input("Please enter the first number:"))
    n2=int(input("Please enter the second number:"))

    print(even_digits(n1,n2))

