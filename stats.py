def word_count(book_text):
    words = book_text.split()
    return len(words)


def character_count(book_text):
    count = {}
    for letter in book_text:
        letter = letter.lower()
        if letter not in count:
            count[letter] = 0
        count[letter] += 1
    return count