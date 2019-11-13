'''
A Dictionary is a collection of related data PAIRS. For instance, if we 
want to store the username and age of 5 users, we can store them in a 
dictionary.
'''

#dictionary keys must be unique, values do not need to be unique

#declaring the dictionary, dictionary keys and data can be of different data types 
myDict = {"One":1.35, 2.5:"Two Point Five", 3:"+", 7.9:2} 
#print the entire dictionary 
#You’ll get {'One': 1.35, 2.5: 'Two Point Five', 3: '+', 7.9: 2} 

print(myDict)

#Items may be displayed in a different order 
#Items in a dictionary are not necessarily stored in the same order as the way you declared them. 

#print the item with key = "One". 
print(myDict["One"]) #You’ll get 1.35 

#print the item with key = 7.9. 
print(myDict[7.9]) #You’ll get 2 

#modify the item with key = 2.5 and print the updated dictionary 
myDict[2.5] = "Two and a Half" 
print(myDict)  #You’ll get {'One': 1.35, 2.5: 'Two and a Half', 3: '+', 7.9: 2} 

#add a new item and print the updated dictionary 
myDict["New item"] = "I’m new"
print(myDict) 
#You’ll get {'One': 1.35, 2.5: 'Two and a Half', 3: '+', 7.9: 2, 'New item': 'I’m new'} 

#remove the item with key = "One" and print the updated dictionary
del myDict["One"]
print(myDict) #You’ll get {2.5: 'Two and a Half', 3: '+', 7.9: 2, 'New item': 'I’m new'}

dic1 = {1: 'one', 2: 'two'} 
dic1.get(1) 
#'one' 

dic1.get(5) 
#None 

dic1.get(5, "Custom message.  Item not found") 
#"Custom message.  Item not found"
