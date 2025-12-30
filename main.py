# import funktioner til tekstanalyse
from stats import count_words, count_each_letter, dict_to_sorted_list
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    letters = count_each_letter(book_text)
    print(f"""
============ BOOKBOT ============
Analyzing book found at {book_path}
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    
    sorteret = dict_to_sorted_list(letters)
    for bogstav in sorteret:
       print(f"{bogstav["char"]}: {bogstav["num"]}")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

    
main()
