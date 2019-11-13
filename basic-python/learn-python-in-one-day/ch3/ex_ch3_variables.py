#python2.7
#describes how to use and create basic variables

#define and init a single variable
userAge = 0

#define and init multiple vars inline
userAge, userName = 30, 'Peter'

#Division and floor division
x = 5
y = 2

print('x:', x, ' y: ', y)
print('x//y: ', x//y)  #==2 (rounds down to the nearest whole int)
print('x%y: ', x%y)    #==1 (gives remainder with 5 is div by 2)
print('x**y:', x**y)   #==25 (5 to the power of 2)

print('x: ', x)
x+=2
print('x += 2:', x )      #==12 where x = x + 2, where right side is evaluated first

