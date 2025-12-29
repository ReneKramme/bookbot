def count_words(text):
    words = text.split()
    return len(words)

def count_each_letter(text):
    letters = {}
    for letter in text:
       # if letter.isalpha():
            letter = letter.lower()
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters