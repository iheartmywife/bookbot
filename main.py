def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
from stats import word_count
    
def main():
    print(f"Found {word_count(get_book_text("books/frankenstein.txt"))} total words")

main()