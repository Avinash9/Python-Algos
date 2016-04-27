

class Anagram:

	def __init__(self):
		pass

	def check_anagram_dynamic(self,string1,string2):
		is_a=False
		arr = [0]*128
		
		for i in range(len(string1)):
			arr[ord(string1[i])%128]=arr[ord(string1[i])%128]+1
		
		for i in range(len(string2)):
			arr[ord(string2[i])%128]=arr[ord(string2[i])%128]-1
			
		print(arr)
		
		if arr == [0]*128:
			is_a=True
		return is_a

	def check_anagram_sorting(string1,string2):
		is_anagram=False
		a=list(string1)
		a.sort()
		b=list(string2)
		b.sort()
		if a==b:
			is_anagram=True
			
		return is_anagram


