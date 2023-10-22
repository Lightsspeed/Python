n=int(input("enter the number to which you want to print: "))


i=1
sum=0

while (i<=n):
    if i%2==0: #to check even nums
        sum=sum+i #summing the even nums
    
    i=i+1 #incrementing i till given value of n

print("sum of even nums: ", sum)