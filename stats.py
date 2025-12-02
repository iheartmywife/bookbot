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
