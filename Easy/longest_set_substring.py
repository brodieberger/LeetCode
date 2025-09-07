s = "dvdf"

count = 0
maxcount = 0
tempset = set('')

for i in range(len(s)):
    if count > maxcount:
        maxcount = count

    count = 1
    for j in range(i+1, (len(s))):
        if s[j] not in tempset:
            count += 1
            tempset.add(s[j])
        else:
            tempset.remove(s[i])
            break
    
if maxcount > count:
    print(maxcount)
else:
    print(count)