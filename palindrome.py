#to check whether strig is palindrome 
s= input('emter string:')
if s==s[::-1]:
	print('{} is palindrome '.format(s))
else:
	print('{} is not a palindrome'.format(s))

