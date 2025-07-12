from stats import get_words, get_num_chars, sorted_dict
import sys

def get_book_path():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def print_report(num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_chars:
        print(f"{char}: {count}")



def main():
    book_text = get_book_text(get_book_path())
    num_words = get_words(book_text)
    num_chars = get_num_chars(book_text)
    sorted_chars = sorted_dict(num_chars)

    print_report(num_words, sorted_chars)

if __name__ == "__main__":
    main()