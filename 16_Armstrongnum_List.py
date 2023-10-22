# Function to check if a number is an Armstrong number
def is_armstrong_number(number):
    return number == sum(int(digit) ** len(str(number)) for digit in str(number))

# Define a range (e.g., 1 to 1000)
start = 1
end = 1000

# Create a list to store Armstrong numbers
armstrong_numbers = []

# Check for Armstrong numbers within the specified range
for num in range(start, end + 1):
    if is_armstrong_number(num):
        armstrong_numbers.append(num)

# Print the list of Armstrong numbers
print("Armstrong numbers within the range:", armstrong_numbers)
