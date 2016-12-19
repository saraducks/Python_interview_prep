string1 = "MON TUE WED THURS FRI SAT SUN"     # Initialize variable
formatter = "%r %r %r %r"                     # This is formatting output initialization
string2 = "20\n30\n40\n\50"                   # playing with /n , /50 prints the equivalent ascii character

print formatter % ("this", "that", "which", "what")
print formatter % (1,2,3, 4)                  # If you pass less number to the formatter then it will throw error
print "The days are ", string1
print "using \n", string2