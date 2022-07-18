n=int(input("Enter a number: "))
temp1=n
temp2=n
count=0
sum=0
while n>0:
    n//=10
    count+=1
rem=0
while temp1>0:
    rem=temp1%10
    sum+=pow(rem,count)
    temp1//=10
if sum==temp2:
    print("%d is Armstrong number"%temp2)
else:
    print("%d is not Armstrong number"%temp2)


