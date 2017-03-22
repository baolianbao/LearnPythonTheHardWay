from sys import argv

script, filename = argv
#line 1-3 should be familiar use of argv to get a filename.
txt = open(filename) # "open" is a new command , Pydoc said:   a file using the file() type, returns a file object.  This is the preferred way to open a file.

print "Here's your file %r:" % filename # print  a  little line,include the filename that you just typed.
print txt.read() # on line 8 we hdve something very new and exciting. It 's a function on txt, You give a filename by use . (dot or period), the name of the command, and parameters.Just like "open" and "raw_input".
print "Type the filename again:"
file_again = raw_input("> ")
# use raw_input get filename again

txt_again = open(file_again)
#set a new variable "txt_again" to read file again.

print txt_again.read()
