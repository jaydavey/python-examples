'''
Tuples are creted using parentheses ().
Tuples are just like lists, but you cannot modify their values. 
The initial values are the values that will stay for the rest 
of the program. An example where tuples are useful is when 
your program needs to store the names of the months of the year.
'''

monthsOfYear = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec") 
letters = ('a', 'b', 'c', 'd', 'e')
print(monthsOfYear) #print all the months
print(monthsOfYear[1]) #print 'Feb'
#check if an item is in a tuple
print('A' in monthsOfYear)  #=>Is 'A' in monthsOfYear? False! Print 'False'

#concatenate tuples
myTuple = monthsOfYear + letters
print(myTuple)

#multiplication of tuples
print(letters*3)
