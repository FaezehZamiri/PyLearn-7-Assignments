num1=int(input("Enter A Integer Number : "))
num2=int(input("Enter An Other Integer Number : "))

counter = max(num1 , num2) 

result = None

while ( counter > 1):
	if ( (num1 % counter) == 0 ) and ( (num2 % counter) == 0 ):
		if result == None:
			result = counter			

	counter -= 1

if result == None:
	print(f"The B.M.M of {num1} and {num2} is 1")
else:
	print(f"The B.M.M of {num1} and {num2} is {result}")