from stats import word_count

from stats import character_count

from stats import sort_character


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    num_words = word_count(book_text)
    count = character_count(book_text)
    ordered_count = sort_character(count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("------- Character Count ---------")
    for item in ordered_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")





main()
