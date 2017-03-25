from sys import argv # Import librariy "argv"

script, input_file = argv  # unpacking "argv"

def print_all(f): # define function "Print_all", purpose is read one file's content and print out!
    print  f.read()

def rewind(f): # define a function "rewind", purpose is set pointer for "readline()"
    f.seek(0)

def print_a_line(line_count, f): # this a  main function, purpose is print out the line number, and line content.
    print line_count, f.readline()

current_file = open(input_file) # key variables, put the file content in it.

print "First let's print the whole file:\n" # print out the prompting for user.

print_all(current_file)  # print out the file content

print "Now let's rewind,kind of like a tape."

rewind(current_file) # this line is important,it make "readline()" work.

print "Let's print three lines:" # prompting

current_line = 1 # set the variables line number
print_a_line(current_line, current_file)  # line number is one and print out the content of first line

current_line = 1 + current_line # manual work , set line number for "readline()"
print_a_line(current_line, current_file) # line number is two and print out the content of 2nd line

current_line = 1 + current_line
print_a_line(current_line, current_file) # line number is three and print out the content of 3rd line

# It's my first time to write English commit, I think so bad.
