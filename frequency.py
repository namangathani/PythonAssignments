most_frequent = str(input())
all_freq = {}
for i in most_frequent:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print ("Count of all characters is :\n "+  str(all_freq))