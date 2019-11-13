#Put your modules in the same folder as your script and you'll always be able to import them.  
#For global modules:
import sys

if '/home/pi/Documents/Python/python-examples/modules' not in sys.path:
	sys.path.append('/home/pi/Documents/Python/python-examples/modules')

import priming as p

print(p.checkIfPrime(13))

