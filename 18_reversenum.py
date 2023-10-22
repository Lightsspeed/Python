# Get user input as an integer
num = int(input("Enter a number: "))

# Convert the number to a string and reverse it
reversed_str = str(num)[::-1]

# Convert the reversed string back to an integer
reversed_num = int(reversed_str)

# Print the reversed number
print("Reversed number:", reversed_num)
