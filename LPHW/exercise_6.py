string1 = "happy"
string2 = "Life"                                #initialize strings
string3 = "I am doing python practise"
concatenate_strings = string1 + string3
s = "crazy test"
calculate_length = len(s)                                             # calculate string length
print "This is test and playing around string %s" % string1+string2
print "This is concatenation %s" % concatenate_strings                 # concatenate strings
print "Printing my %s to lowercase %s" % (string1, string1.upper())   # string to upper case

temp = string3.split(' ',1)
print "converting the sentence to the list using split in-built function %s" % temp     #converting the string to list
                                                                                        #using split in-built function

string_splice = string3[0:4:1]
print "aplicing strings %s: %s" %(string3, string_splice)         # splicing string using the start index, stop index and step