from stats import word_count

from stats import character_count


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    num_words = word_count(book_text)
    count = character_count(book_text)
    print(f"{num_words} words found in the document")
    print(count)




main()
