num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
oper = input("Choose the operation (+, -< /< *):*")

if num1.isnumeric() and num2.isnumeric():
	num1 = int(num1)
	num2 = int(num2)
	if oper == '+':
		answ = num1 + num2
		print ("The answer is %d" %(answ))
	elif oper == '-':
		answ = num1 - num2
		print ("The answer is %d" %(answ))
	elif oper == '/':
		answ = num1 / num2
		print ("The answer is %d" %(answ))
	elif oper == '*':
		answ = num1 * num2
		print ("The answer is %d" %(answ))
	else:
		print("the operation is not valid")
else:
	print ("the numbers are not valid")
