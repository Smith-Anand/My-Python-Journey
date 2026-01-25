#Write a program to enter 10 numbers and display all armstrong numbers 
#from those numbers. 

# Program to find Armstrong numbers from 10 entered numbers

def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == num

numbers = []

print("Enter 10 numbers:")
for i in range(10):
    numbers.append(int(input()))

print("\nArmstrong numbers are:")
for num in numbers:
    if is_armstrong(num):
        print(num)
