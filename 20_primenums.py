n=int(input("enter the nums: "))

count=0

i=1

while (i<=n):
    if (n%i==0):
        count=count+1
    i=i+1
if (count==2):
    print("prime number")
else:
    print("not prime number")


# Get the maximum number from the user
max_num = int(input("Enter the maximum number: "))

# Create a list to store prime numbers
prime_list = []

# Check each number from 2 to max_num for primality
for num in range(2, max_num + 1):
    is_prime = True
    
    # Check if num is divisible by any number from 2 to the square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    # If num is prime, add it to the prime_list
    if is_prime:
        prime_list.append(num)

# Print the list of prime numbers
print("Prime numbers up to", max_num, "are:", prime_list)
