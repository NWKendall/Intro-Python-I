"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open('foo.txt', 'r') as foo:

    for line in foo:
        print(line, end='')

# foo_read = foo.readline()
#     print(foo_read, end='')

# size_to_read = 100
# put in while loop
# foo_read = foo.read(size_to_read)
#     print(foo_read, end='')



# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('bar.text', 'w') as bar:
    bar_write = bar.write("testing 1 2 3 4 5")
