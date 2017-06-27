print ('''Suggested inputs to demo errors 
Please enter a number: m, 12
Please enter another number: 0, 3.\n''' )
print "https://docs.python/3/library/exceptions.html\n\n"

try:
	userInput1 = int(input("Please enter a number: "))
	userInput2 = int(input("Please enter another number: "))
	answer =userInput1/userInput2
	print "The answer is ", answer
	#myFile = open("missing.txt", 'r')
except NameError:
	print ("Error: You did not enter a number")
except ValueError:
	print ("Error: You did not enter a number")
except ZeroDivisionError:
	print ("Error: Cannot divide by zero")
except IOError:
	print ("Error: Cannot find missing.txt")
except Exception as e:
	print ("Unknown error: ", e)

#
