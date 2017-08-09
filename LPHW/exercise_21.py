temp = []                                   # empty list
temp1 = ['python', 'java', 'php', 'scala']  # initialized list

print "enter the 10 numbers"
for i in range(0,10):                       # get user input, and append to the list
    temp.append(raw_input())

print temp
print sorted(temp)                          # sort the list, sorted is the in-built function

for res in temp1:                           # for loop, iterating in the temp2 list
    print res