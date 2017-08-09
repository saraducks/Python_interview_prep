'''
The dictionary will store the values of states and its abbreviation
'''
dict = {"newyork" : {"NY" : "newyork"}, "portland" : {"OR" : "portland"}, "Michigan": {"MI": "detriot"},
            "california": {"CA": "sanfrancisco"},"oregon": {"OR": "portland"}}


for i in dict:                                          # loops over the state and it's abbreviated key
    print i," is abbreviated as ",dict[i].keys()

for j in dict:                                          # loops over the state, it's keys and values
    print j,"is abbreviated as",dict[j].keys()," it has the state ",dict[j].values()


temp = dict["Michigan"].keys()                          # manually enter the key to get the sub-keys
print temp