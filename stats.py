def get_num_words(text):
    words = text.split()
    return len(words)

def get_letters(text):
    letters_dict = dict()
    for letter in text:
        if letter.lower() in letters_dict:
            letters_dict[letter.lower()] += 1
        else:
            letters_dict[letter.lower()] = 1
    
    return letters_dict

def sort_on(items):
    return items["num"] 

def create_letter_list(letter_dict):
    letter_list = list()

    for letter, amount in letter_dict.items():
        char_dict = dict()
        char_dict["char"] = letter
        char_dict["num"] = amount
        letter_list.append(char_dict)
        del(char_dict)
    
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list