#program to remove space  from  input string
user_input=input('enter your favourite social media platform:')
if user_input == 'fb ' or 'facebook' or 'Facebook':
	print('you can add new friends here in {}'.format(user_input))
elif user_input == 'twitter':
	print('you can tweet on {} '.format(user_input))
elif user_input == 'quora':
	print('you can ask question here in {}'.format(user_input))
else:
	print('entry {} is not  among [fb,twitter and quorq] try again'.format(user_input))

