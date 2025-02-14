def main(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

def word_count(book_as_string):
    return len(book_as_string.split())

def letter_count(book_as_string):
    letter_dict = dict()
    for letter in book_as_string:
        if letter.lower() in letter_dict:
            letter_dict[letter.lower()] = letter_dict[letter.lower()] + 1
        else:
            letter_dict[letter.lower()] = 1
    
    return letter_dict

def report(file_path, words, letters):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    print(f"--- Begin report of {file_path} ---")
    print(f"{words} words found in the document")
    print()
    for letter, count in letters.items():
        if letter in alphabet:
            print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")
    

if __name__ == "__main__":
    file_path = 'books/frankenstein.txt'
    book = main(file_path)
    words = word_count(book)
    letters = letter_count(book)
    report(file_path, words, letters)
