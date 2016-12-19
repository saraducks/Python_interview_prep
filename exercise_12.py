from sys import argv

script, first = argv

v =  open(first)


print "This is your file name", first
print v.next()      # This will act as generator, My file has only three lines
print v.next()
print v.next()

#print "use for loop to display"        # this won't work either for loop or generator will work
#for i in v:
#    print i