s = 'azcbobobegghakl'
v = 'bob'
temp = len(s)
count = 0
for i in range(0,temp,1):
    if s[i:i+3] == v:
        count = count + 1
print count