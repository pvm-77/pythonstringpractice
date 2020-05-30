'''
index method  returns index of first occurence  of specified  substring if available 
and if specified  substring not present then it  returns value error:substring not found
'''
user_input_string = input('enter a string:')
print('you have enter "{}" as main string:'.format(user_input_string))
specified_substring = input('enter a  sub string that you want to find in given string:')
#logic to find substring
return_value_holder = user_input_string.index(specified_substring)
print('"{}" is available at index {}'.format(specified_substring,return_value_holder))

