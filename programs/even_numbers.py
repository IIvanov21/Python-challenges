def even_digits(digit_one,digit_two):
    even_list=[]
    for i in range(digit_one,digit_two):
        if i % 2==0: even_list.append(i)
    return even_list

if __name__ == "__main__":
    n1=int(input("Please enter the first number:"))
    n2=int(input("Please enter the second number:"))

    print(even_digits(n1,n2+1))

