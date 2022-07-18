def add(a,b):
    return a + b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divide(a,b):
    return a//b
def mod(a,b):
    return a%b
print("Select the option:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Exit")
while True:
    option=int(input())
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    if option==1:
        print(x,"+",y,"=",add(x,y))
    elif option==2:
        print(x,"-",y,"=",sub(x,y))
    elif option==3:
        print(x,"*",y,"=",mul(x,y))
    elif option==4:
        print(x,"//",y,"=",divide(x,y))
    elif option==5:
        print(x,"+",y,"=",mod(x,y))
    else:
        break
    


