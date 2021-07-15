# this program says hello and asks for my name and age

print('hello')

print('what is your name?')
myName = input()
print('it is good to meet you, ' + myName)
print('the length of your name is: ')
print(len(myName))
print('how old are you?')
myAge = input()
print(myName + ' you will be ' + str(int(myAge)+1) + ' in 1 year')

