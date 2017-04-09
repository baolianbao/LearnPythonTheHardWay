i = 0
numbers = []

while i < 6:  # keep loop if i < 6
    print "At the top i is %d" % i # print the value of varibales on the top
    numbers.append(i) # put the value of  i into the list numbers

    i = i + 1  # every time  increase 1 for i
    print "Numbers now:", numbers
    print "At the bottom i is %d" % i # print the value of i after increase


print "The numbers:"
for num in numbers:  # take the elements from numbers into num
    print num
