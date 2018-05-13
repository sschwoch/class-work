def count(word, letter):
    count = 0
    for character in word:
        if character == letter:
            count = count + 1
print(count)
        
word = input('Enter the word: ')
letter = input('Enter the letter: ')
count(word, letter)