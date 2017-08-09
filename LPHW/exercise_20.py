print "Enter the following numbers"
print "Enter the turtle speed"
input1 = raw_input()                       # getting the user input
print "Enter the rabbit speed"
input2 = raw_input()
print "Enter the human speed"
input3 = raw_input()
print "Enter the horse speed"
input4 = raw_input()

if input1 < input4 and input4 > input2:          # checks if both condition is true
    print input4+" horse wins"
elif input4 < input3:                            # if fails, then elif checks for the condition
    if input3 > input1:                            # nested if checks further condition once the elif pass
        print input3+"human little slower than horse, much better than turtle "+input4
elif input4 < input2:
    print input2+"rabbit great job!"
else:                                             # None matches then execute this default statement
    print "everyone wins"
