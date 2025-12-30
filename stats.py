def count_words(text):
    words = text.split()
    return len(words)

def count_each_letter(text):
    letters = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

def dict_to_sorted_list(dict):
    unsorted_list = []
    for key, value in dict.items():
        unsorted_list.append({"char": key, "num": value})
    unsorted_list.sort(key=lambda x: x["num"], reverse=True)
    return unsorted_list

