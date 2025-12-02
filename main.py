def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
# def book_report(list_of_dictionaries):
    

from stats import character_count, list_of_dictionaries
    
def main():
    char_count = character_count(get_book_text("books/frankenstein.txt"))
    test = list_of_dictionaries(char_count)
    print(test)
main()