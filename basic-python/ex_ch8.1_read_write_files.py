#-------------------
#Opening text files

f1 = open('/home/jay/python/python-examples/data/myfile.txt','r') #read mode
firstLine = f1.readline()
secondLine = f1.readline()
print firstLine, secondLine		#python 3.x print(firstLine, end = '')
f1.close()


f2 = open('/home/jay/python/python-examples/data/myfile.txt','r') #read mode
for line in f2:
	print line, #python 3.x print(firstLine, end = '')
f2.close()

f3 = open('/home/jay/python/python-examples/data/myfile.txt','a') #append mode
f3.write('\nThis sentence will be appended.')
f3.write('\nPython is fun!.')
f3.close()

#------------------------------------
#Opening and reading by a buffer size
inputFile1 = open('/home/jay/python/python-examples/data/myinputfile.txt','r') #read mode
outputFile1 = open('/home/jay/python/python-examples/data/myoutputfile.txt','w') #write mode

msg = inputFile1.read(10) #read 10 bytes

while len(msg):
	#outputFile.write(msg)  
	outputFile1.write(msg+'\n')  #to temp. prove the 10 bytes at a time works you can use this line instead
	msg = inputFile1.read(10)

inputFile1.close()
outputFile1.close()

#--------------------------------
#Reading and Writing Binary Files
inputFile2 = open('/home/jay/python/python-examples/data/image_in.jpg','rb') #read binary file mode
outputFile2 = open('/home/jay/python/python-examples/data/image_out.jpg','wb') #write binary file mode

inputBuffer = inputFile2.read(10) #read 10 bytes

while len(inputBuffer):  
	outputFile2.write(inputBuffer) 
	inputBuffer = inputFile2.read(10)

inputFile2.close()
outputFile2.close()

