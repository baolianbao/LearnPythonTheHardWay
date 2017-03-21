from sys import argv

script, user_name = argv
prompt = '> ' #Set variable "prompt",and give the value in it

print "Hi %s, I'm the %s script."% (user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
like = raw_input(prompt) # give the "prompt" to raw_input,instead of typing it over and over,If we want to make the prompt something else ,we just change it in this one spot.

print "where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me .
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (like, lives, computer)
