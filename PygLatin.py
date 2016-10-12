pyg = 'ay'

print ('Welcome to the Pig Latin Translator!')

# Input
original = input('Enter a word:')

# Verify a word was entered
if len(original) > 0 and original.isalpha():
    print (original)
    word = original.lower()
    first = word[0]
    new_word = (word + first + pyg)
    new_word = new_word[1:len(new_word)]
else:
    print ('empty')

print (new_word)


