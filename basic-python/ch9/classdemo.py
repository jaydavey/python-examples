#demo on using classes

class Staff:
	def __init__(self, pPosition, pName, pPay):
		self._position = pPosition  #underscore lets other 'consenting adults' know they should not access 'position' directly
		self.name = pName
		self.pay = pPay
		print('Creating Staff object')

	def __str__(self):
		return "Postiion = %s, Name = %s, Pay = %d" %(self._position, self.name, self.pay)

	def calculatePay(self):
		prompt = '\nEnter number of hours worked for %s: ' %(self.name)
		hours = input(prompt)
		prompt = 'Enter the hourly rate for %s: ' %(self.name)
		hourlyRate = input(prompt)
		self.pay = int(hours)*int(hourlyRate)
		return self.pay

	@property
	def position(self):
		print ("Getter Method")
		return self._position

	@position.setter
	def position(self, value):
		if value =='Manager' or value == 'Basic':
			self._position = value
		else:
			print('Position is invalid. No changes made.')

#to use this class, 
#python
#>>> from classdemo import Staff
#>>> officeStaff1 = Staff('Basic','Yvonne',0)
#>>> officeStaff2 = Staff('Basic','Bob',0)


#>>> officeStaff1.name

#output: 
#'Yvonne'

#>>> officeStaff2.position = 'Manager'
#output:
#'Manager'

#officeStaff1.calculatePay()

#output:
#Enter number of hours worked for Yvonne: 10
#Enter the hourly rate for Yvonne: 15

#output:
#150

#print(officeStaff2)

#output
#"Postiion = Manager, Name = Bob, Pay = 0"