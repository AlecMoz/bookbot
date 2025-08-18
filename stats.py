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


def get_num(dict):
    return dict["num"]


def sort_character(count):
    ordered_count = []
    for char, num in count.items():
        new_dict = {"char": char, "num": num}
        if new_dict["char"].isalpha():
            ordered_count.append(new_dict)
    ordered_count.sort(reverse=True, key=get_num)
    return ordered_count
