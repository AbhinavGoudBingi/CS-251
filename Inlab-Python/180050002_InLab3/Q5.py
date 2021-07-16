word = input("")
diction = {key: 0 for key in word}
for i in word:
   diction[i] = diction[i]+1;
for key, value in sorted(diction.items(), key=lambda x: (x[1],x[0]), reverse=True):
    print("%s: %s" % (key, value))

