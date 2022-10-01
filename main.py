#dev
num1 = int(input("Enter diapazon first number: "))
num2 = int(input("Enter diapazon second number: "))
for i in range(num1,num2+1):
    if i %3==0 ^ i%5==0:
        print(f"Fizz Buzz ")
    elif i %5==0:
        print(f"Buzz ")
    elif i%3==0:
        print(f"Fizz " )
    else:
        print(i)
