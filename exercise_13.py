from sys import argv

script, first = argv         # get the file name

temp = open(first,'w')       # open file using the 'w' write
print temp
print "write to the file"
get_input = raw_input()      # get user input
temp.write(get_input)        # write to the file
print "truncate file"
temp.truncate()              # It will delete all contents
print "tell me about your life"
get_user_input = raw_input()
temp.write(get_user_input)
temp.close()                # closes the file