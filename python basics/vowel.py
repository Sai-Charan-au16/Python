# type1
words = input()
for i in words:
  if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
    print(i)

#type2
words = input()    
vowels = 'AEIOU'
for i in words:
    if i in vowels:
        print(i)