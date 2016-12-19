from sys import argv

script, first = argv

temp = open(first)

def print_content(get_input):
    print temp.read()

def print_specific(get_input):
    print temp.seek(0,0)
    print temp.read()

def find(get_input):
    print temp.isatty()

print_content(temp)
print_specific(temp)
find(temp)
temp.close()