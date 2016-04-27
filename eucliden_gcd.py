

class ComputeGCD:

	def __init__(self):
		pass
		

	def  compute_gcd(self,number1,number2):
		if (number2>number1):
			temp = number2
			number2 = number1
			number1 = number2

		while number1 % number2 != 0:
			print "::::::::::",number1,number2
			temp= number2
			number2 = number1 % number2
			number1 = temp
			print "::::::::::",number1,number2

		return number2




