import re
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = word_count(text)
    character_dict = character_count(text)
    #print(count_words)
    list_of_dict = character_list(character_dict)
    print(list_of_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    lowered_string = re.sub("[^a-zA-Z]"," ", text.lower())
    count = {}
    for character in (lowered_string):
        if character not in count:
            count[character] = 1
        elif character in count:
                count[character] += 1
    return count

def character_list(dict):
    list_of_characters = []
    for character, num in dict.items():
          list_of_characters.append({character:num})
    return list_of_characters


def sort_on(character_dict):
     return character_dict["num"]

def report_characters(count_words, character_dict):
     character_dict.sort(reverse=True, key=sort_on)



main()