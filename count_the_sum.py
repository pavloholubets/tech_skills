q=[[156, 784, 15, 367], [98, 67, 111], [344, 658,14, 3]]

n=0

for i in q:
	for p in i:
		if p%2==0:
			n+=p

print(n)


# option 2

a=[o for i in q for o in i if o%2==0]
print(sum(a))

