#print odd string characters of the given  string
s=input('enter string man:')
print(s[ : : 2])
#my alternative method 
char=0
ask_user = input('enter string:')
for  char  in ask_user:
	if  char%2==0:
		continue
	print(ask_user[char])
	char=char+1
