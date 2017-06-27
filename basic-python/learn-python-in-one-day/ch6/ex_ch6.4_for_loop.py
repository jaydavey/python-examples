pets = ['cats','dogs','rabbits','hamsters']

for i in pets:
	print i

for index, i in enumerate(pets):
	print index, i

age = {'Peter':5,'John':7}

for i in age:
	print ("Name = %s, Age = %d" %(i, age[i]))

for i,j in age.items():
	print("Name = %s, Age = %d" %(i,j))

for i in range(5):
	print i

j = 0
for i in range(5):
	j = j + 2
	print "\ni = ", i, ", j = ", j
	if j == 6:
		continue
	print ('I will be skipped over if j=6')

