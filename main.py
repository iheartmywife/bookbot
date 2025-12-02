def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
from stats import character_count
    
def main():
    char_count = character_count(get_book_text("books/frankenstein.txt"))
    print(char_count)
main()