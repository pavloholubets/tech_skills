x = [[156, 784, 15, 367], [98, 67, 111], [344, 658,14, 3]]

sum = 0
for i in x:
    for y in i:
        if y % 2 == 0:
            sum = sum + y
print (sum)