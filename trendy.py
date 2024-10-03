...
Write a program to check whether the given number is a trendy number or not. A number is said to be a trendy number if and only if it has 3 digits and the middle digit is divisible by 3.
Input format:
The input containing an integer 'n' which denotes the given number
Output format:
If the given number is a trendy number, then print "Trendy Number". Otherwise, print "Not a Trendy Number".
Refer the sample output for formatting.
Sample Input:
791
Sample Output:
Trendy Number
...
def is_trendy_number(n):
    # Check if the number is a three-digit number
    if 100 <= n <= 999:
        # Convert number to string to access digits
        str_n = str(n)
        # Get the middle digit
        middle_digit = int(str_n[1])
        
        # Check if the middle digit is divisible by 3
        if middle_digit % 3 == 0:
            return "Trendy Number"
    
    return "Not a Trendy Number"

# Input format
n = int(input("Enter a number: "))
# Output format
result = is_trendy_number(n)
print(result)
