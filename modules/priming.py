#check if a number is prime 
def checkIfPrime (numberToCheck):
	for x in range(2,numberToCheck):
		if (numberToCheck%x == 0):
			return False
		return True
