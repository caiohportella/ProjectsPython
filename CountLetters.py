import string

alphabet = string.ascii_letters

sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}


for letter in sentence:
    
    if letter in alphabet: 
        
        if letter in count_letters: 
            
            count_letters[letter] += 1 

        else:
            
            count_letters[letter] = 1 
print(count_letters)