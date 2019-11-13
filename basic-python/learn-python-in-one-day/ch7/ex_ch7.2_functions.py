#def functionName(list of parameters):
	#"function docstring"
	#code detailing what the function should do
	#return [expression]

#def functionName(farg, *args, **kwargs):


#formal arguments 
#example function - check if a number is prime 
def checkIfPrime (numberToCheck):
	for x in range(2,numberToCheck):
		if (numberToCheck%x == 0):
			return False
		return True

print(checkIfPrime(13))


#assigning default values to formal arguments
#All parameters with default values must be placed at the end of the parameter list.
def someFunction(a,b,c=1,d=2,e=3):
	print(a,b,c,d,e)
	return None

print(someFunction(4,5))


#Non key worded variable length argument list (variable length argument list)
def addNumbers(*num):
	sum = 0
	for i in num:
		sum = sum + i
	print(sum)

print(addNumbers(1,2,3,4,5))


#key worded arguments (passing dicts to functions)
def printMemberAge(**age):
	for i,j in age.items():
		print("Name = %s, Age = %s" %(i,j))

print(printMemberAge(Peter = 5, John = 7, Yvonne = 10))
