# random numbers and imports

import random as r

random_number = r.randint(1,100)

for i in range(5):
    print('a random number between 1 and ' + str(random_number) + ' is ' + str(r.randint(1,random_number))) 