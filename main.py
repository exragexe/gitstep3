#dev
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
for i in range(num1, num2 +1):
    if i % 7==0:
        print(i)
else:
            for i in range(num2,num1+1):
                if i % 7 == 0:
                    print(i)