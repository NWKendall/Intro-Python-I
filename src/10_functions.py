# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(n):
    if int(n) % 2 == 0:
        return True        
    else:
        return False

print(is_even(7))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
def even_odd(n):
    if int(n) % 2 == 0:
        return "Even!"
    else:
        return "Odd"
# YOUR CODE HERE

print(even_odd(num))

