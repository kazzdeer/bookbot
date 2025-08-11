import sys
from stats import get_num_words
from stats import get_letters
from stats import create_letter_list

def main(book_path):
#   book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters = get_letters(text)
    letters_list = create_letter_list(letters)
#   print(f"{num_words} words found in the document")
    print(sys.argv)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in letters_list:
        if letter["char"].isalpha() is True:
            print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()

if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])