# Get user input
number = int(input("Enter a number: "))

# Calculate the number of digits in the number
num_str = str(number)
num_digits = len(num_str)

# Calculate the sum of digits raised to the power of num_digits
sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)

# Check if it's an Armstrong number and display the result
if sum_of_digits == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")