from sys import argv
script, filename = argv

txt = open(filename) # "open"    a file using the file() type, returns a file object.  This is the preferred way to open a file.


print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")
# use raw_input get filename again

txt_again = open(file_again)
#set a new variable "txt_again" to read file again.

print txt_again.read()
