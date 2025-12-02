def word_count(book_text):
    words = book_text.split()
    return len(words)

def character_count(book_text):
    book_text = book_text.lower()
    words = book_text.split()
    
    alphabet = {}

    for word in words:
        for letter in word:
            if letter not in alphabet:
                alphabet[letter] = 1
            else:
                alphabet[letter] += 1
    
    return alphabet

def sort_on(dict):
    return dict["count"]

def list_of_dictionaries(dictionary):
    dictionaries__list = []
    for char in dictionary:
        count = dictionary[char]
        new_dict = {
            "char": char,
            "count": count
        }
        dictionaries__list.append(new_dict)
        dictionaries__list.sort(reverse=True, key=sort_on)
    return dictionaries__list

    
