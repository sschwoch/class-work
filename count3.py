def count(word, letter):
        count = 0
        for char in word:
                if char == letter:
                        count = count + 1
        print(count)
word = input('Enter word here: ')
letter = input('Enter letter here: ')
count(word, letter)