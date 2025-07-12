def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_words(text):
    words = []
    for word in text.split():
        words.append(word)
    return len(words)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    # print(book_text)

    num_words = get_words(book_text)
    # Get the amount of words in the document
    
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()