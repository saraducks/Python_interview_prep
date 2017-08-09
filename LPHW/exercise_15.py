def __init__(self):        # This will initialize the __init__ to current object that calls __init__
    print self

def test():                # no arguments
    print "No args"

def print_onearg(get_input):     # pass one argument
    print "Inside the print_onearg",get_input

def compute(x, y):                 # two arguments
    print "addition", x+y
    print "subraction", x-y if x >y else y-x

__init__(self="hello")
test()
print_onearg("this is test")
compute(12,10)
compute(5,16)
print "enter the string"
string1 = raw_input()
print_onearg(string1)
