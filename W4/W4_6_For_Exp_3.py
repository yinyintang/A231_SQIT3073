import os 
#window
os.system('cls') 

# List of integers
numbers = [1, 2, 3, 4, 5, 6]

# For loop to go through each element in the list
for num in numbers:
    # If-else statement to determine if a number is even or odd
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")

print('This show the iteration of for loop in the list and utilized if else conditions')
