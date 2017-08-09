print "Enter the number to repeat while block"
temp = int(raw_input())

while temp >= 0:                 # compare user input from default value
    print temp
    temp = temp - 1              # reduce the temp value each time the while block is executed

print "Enter the number"
temp3 = int(raw_input())         # get user input
temp2 = 10

while temp3 > temp2:             # if the input value is greater than temp2 this while block will execute
    print "your input, I will reduce your value soon", temp3
    temp3 = temp3 - 1
print "You are loser!"