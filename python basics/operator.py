#Q1
def rev_sentence(sentence): 
	words = sentence.split(' ')  
	reverse_sentence = ' '.join(reversed(words))  
	return reverse_sentence 

if __name__ == "__main__": 
	input =("A boy is good")
	print (rev_sentence(input)) 

#Q2

string = "“hello this is me and rohan and vijay" 
 
print(string.replace("and", ",")) 


#Q3

word = "AttainU"[::-1]
print(word)

#Q4

sample_text = "hello everybody"

result = sample_text.title()
print(result)