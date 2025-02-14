def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    return file_contents

def word_count(book_as_string):
    return len(book_as_string.split())


if __name__ == "__main__":
    book = main()
    words = word_count(book)
    print(words)
