#dev
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
z=[]


while x>=y:
    z.append(x)
    x-=1
    for i in z[::-28]:
        if i %7==0:
            print(i )
            break

while x<=y:
    z.append(y)
    y-=1
    for i in z[::-28]:
        if i %7==0:

            print(i )
            break