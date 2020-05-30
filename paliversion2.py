#using for loop to check whether input string is palindrome or not
s= input('enter string:')
i = len(s)-1
palindrome_holder=''
for  i in range(i,-1,-1):
	palindrome_holder =  palindrome_holder + s[i]
	i = i - 1
if  s==palindrome_holder:
	print('{} is a palindrome'.format(s))
else:
	print('{} is not a palindrome .thanks'.format(s))

