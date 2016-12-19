from sys import argv

script, first, second = argv    # get the input from the prompt

print "what's the day today?"
prompt = '> '                        # variable assignment
get_userinput = raw_input(prompt)    # > user_input
print "Today is ",get_userinput

temp = first + second               # concatenates two input strings which is passed before the execution of .py file
print "This is concatenation", temp
