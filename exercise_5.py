string1 = "Playing around python"
string2 = "This is crazy"
number1 = 34
number2 = 7.67

print "{:.4f}".format(number2)          # this will print my floating point number with 4 precisions
print  "{},{}".format(string1, string2)   # this displays two strings seperated by commas
print "{0!s} to check if string is passed to format or not".format(string1)                    # this will raise error when no string is passed for formatting
print "To display my number:{:4d}".format(number1)     #to diplay with 4 digits, it will lead to trailing spaces