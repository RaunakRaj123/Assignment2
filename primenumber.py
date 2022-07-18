n=int(input("Enter a number: "))
flag=0
t=n//2
for t in range(2,t+1):
    if n%t==0:
        flag+=1
if flag>0:
    print(n,"is not a prime number")    
else:
    print(n,"is a prime number")
