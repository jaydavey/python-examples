#examples of using lists in python

userAge = [21, 22, 23, 24, 25]

print userAge[0],userAge[1],userAge[-1],userAge[-2]
# 21 22 25 24
# first item, second item, last item, second last item

#slice notation
print userAge[2:4]   #[23, 24] DOES NOT INCLUDE 25! Notation 2:4 is index 2 to 4-1 
print userAge[1:5:2] #[22, 24] 'stepper' is 2 so returns every second number

print userAge[:4]    #==userAge[0:4]   #default for first number is zero 
print userAge[1:]    #==userAge[1:5-1] #size of list is 5 

#mod items in a list
userAge[1] = 5

#add items to the list
userAge.append(99)

#remove items from a list
del userAge[2] #deletes third item

#mixing data types
myList = [1, 2, 3, 4, 5, "Hello"] 

