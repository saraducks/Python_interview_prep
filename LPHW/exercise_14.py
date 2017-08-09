from sys import argv
from os import _exists,path               # to get filename path , to check if the file exists

script, from_file, to_file = argv        # get the user input from the prompt

temp = open(from_file)                    # opens the source file in read mode
copy_data = temp.read()                   # reads from source and copies to copy_data variable
print copy_data

print "To check if the destination file %s exists" % to_file
print path.exists(to_file)
if path.exists(to_file):                 # if destination file exists then copy the copy_data content to destination file
    v = open(to_file,'w')                # opens the destination file in write mode
    v.write(copy_data)
    v.close()                            # close files

temp.close()