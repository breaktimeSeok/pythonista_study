def isPalindrome(s: str) -> bool:
	# create list (strs)
	strs = []
	# Repeat for element size in the list
	for char in s:
		# isalnum = Alphabet&number determin function / include only alphabet&number This is, remove special characters
		if char.isalnum():
			# conversion to lowercase letters & add list
			strs.append(char.lower())
			
	# list size > 1 loop		
	while len(strs) > 1:
		#Compare front and back of list
		if strs.pop(0) != strs.pop():
			return False
				
	return True
	
	
mystring = "A man, a plan, a canal: Panama"
mystring2 = "race a car"
print(isPalindrome(mystring))
print(isPalindrome(mystring2))

