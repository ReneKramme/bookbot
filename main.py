# import funktion til tekstanalyse
from stats import * #get_book_text, count_words

def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    
main()
