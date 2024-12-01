def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = word_count(text)
    print(text)
    print(count_words)
    print(character_count(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    lowered_string = text.lower()
    count = {}
    for character in (lowered_string):
        if character not in count:
            count[character] = 1
        elif character in count:
                count[character] += 1
    return count


main()