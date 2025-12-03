import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
# def book_report(list_of_dictionaries):
    

from stats import character_count, list_of_dictionaries, word_count, pretty_print
    
def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = sys.argv[1]
    book_word_count = word_count(get_book_text(book))
    char_count = character_count(get_book_text(book))
    sorted_chars = list_of_dictionaries(char_count)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {book}...")
    print(f"----------- Word Count ----------\nFound {book_word_count} total words")
    print(f"--------- Character Count -------")
    pretty_print(sorted_chars)
    print("============= END ===============")

main()