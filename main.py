# import funktion til tekstanalyse
from stats import count_words, count_each_letter

def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    letters = count_each_letter(book_text)
    print(f" Disse bogstaver findes i bogen: {letters}")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

    
main()
