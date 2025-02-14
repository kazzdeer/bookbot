def main():
    with open("books/frankenstein.txt") as f:
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


if __name__ == "__main__":
    book = main()
    words = word_count(book)
    letters = letter_count(book)
    print(letters)
