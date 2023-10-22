n=int(input("enter the number to which you want to print: "))


sum=0

while (n>0):
    sum=sum+(n%10)*(n%10)
    n=n//10
print(sum)