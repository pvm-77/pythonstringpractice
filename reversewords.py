#program to reverse the words of the sentence 
sentence = input('enter  sentence:')
#split() method breaks  the sentence into words and create a list of words
sentence_split = sentence.split()
print(sentence_split)


'''
second method
'''
reverse_word_list=[]
count = len(sentence_split) - 1
while count >= 0:
	reverse_word_list.append(sentence_split[count])
	count= count-1
output=' '.join(reverse_word_list)
print(output)
