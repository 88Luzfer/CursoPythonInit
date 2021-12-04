phone_numbers = {"Jhon Smith": "+348569856", "Marry Simson": "+3465298526"}

#for pair in phone_numbers.items():
    #print("{} has a phone number {}".format(pair[0], pair[1]))

for pair in phone_numbers.items():
    pair=list(pair)
    print("%s %s" % (pair[0], pair[1]))