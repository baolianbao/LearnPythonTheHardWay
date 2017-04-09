def while_f(i):

    numbers = []
    while i < 6:  # keep loop if i < 6

        numbers.append(i) # put the value of  i into the list numbers

        i = i + 1  # every time  increase 1 for i
        print "Numbers now:", numbers

    print numbers


while_f(0)
