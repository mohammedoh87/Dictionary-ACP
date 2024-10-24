test = {'Joshua' : 9,
        'Khan' : 9,
        'Narendri' : 8, 
        'Kumar' : 5, 
        'Rashid' : 9}

print(str(test))

f = 9
count = 0
for i in test:
    if test[i] == f:
        count = count + 1
print("The frequency of 9 is " + str(count))