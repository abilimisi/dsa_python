def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10  # Get the last digit
        reversed_num = reversed_num * 10 + digit  # Add the digit to the reversed number
        num = num // 10  # Remove the last digit from the original number
    return reversed_num

# Test the function
num = 7899
reversed_num = reverse_number(num)
print(f"The reversed number of {num} is {reversed_num}.")
