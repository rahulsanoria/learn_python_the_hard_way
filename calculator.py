print " CALCULATOR "

def add(a, b):
	return a + b 

def sub(a, b):
	return a - b

def multi(a, b):
	return a * b

def div(a, b):
	return a / b

def mod(a, b):
	return a % b

print " Select Operation for two numbers "

print " 1. Addition "
print " 2. Subtraction "
print " 3. Multiply " 
print " 4. Divide "
print " 5. Modulus "

print " You can choose only these 5 operation \n"

ope = raw_input(" Enter the operation choose ( 1 / 2 / 3 / 4 / 5 ) :   " ) 

num_1 = float(input(" Enter the first number :  ")) 
num_2 = float(input(" Enter the first number :  "))

if ope == '1':
	print   num_1 , " + " , num_2 ," = " , add(num_1, num_2) 
elif ope == '2' :
	print   num_1 ," - ", num_2, " = " ,sub(num_1, num_2) 
elif ope == '3':
	print  num_1 ," * ", num_2, " = ", multi(num_1, num_2) 
elif ope == '4':
	print   num_1 ," / "  , num_2, " = " ,div(num_1, num_2) 
elif ope == '5' :
	print  num_1, " % ", num_2, " = " ,add(num_1, num_2) 
else :
	print " not valid operation or input , try again  "