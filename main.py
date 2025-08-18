import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

from stats import word_count, character_count, sort_character


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
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
