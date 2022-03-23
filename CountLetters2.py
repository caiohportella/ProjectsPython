import string

alphabet = string.ascii_letters
sentence = 'Jim quickly realized that the beautiful gowns are expensive'

def counter(input_string):
    return {i: input_string.count(i) for i in input_string if i in alphabet}

print(counter(sentence))