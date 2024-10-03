...
Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'.
Input format:
The input containing an integer 'n' which denotes the given number.
Output format:
If the given number is factorial, print "Yes". Otherwise, print "No".
Refer the sample output for formatting.
Sample Input:
6
Sample Output:
Yes
...
def is_factorial_number(n):
    if n < 0:
        return "No"  # Factorials are non-negative
    
    factorial = 1
    i = 1
    
    while factorial < n:
        i += 1
        factorial *= i
    
    return "Yes" if factorial == n else "No"

# Input format
n = int(input("Enter a number: "))

# Check if n is a factorial number
result = is_factorial_number(n)

# Output format
print(result)
