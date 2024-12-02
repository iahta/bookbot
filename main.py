import re
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = word_count(text)
    character_dict = character_count(text)
    list_of_dict = character_list(character_dict)  
    sorted_list = sort_characters(list_of_dict)
    print(sorted_list)
    book_report(count_words, sorted_list )


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    lowered_string = re.sub("[^a-zA-Z]","", text.lower())
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
        char_num_dict = {}
        char_num_dict["character"] = character
        char_num_dict["num"] = num 
        list_of_characters.append(char_num_dict)
    return list_of_characters


def sort_on(dict):
     return dict["num"]

def sort_characters(list_of_dict):
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

def book_report(count_words, sorted_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words} words found in the document")
    print(" ")

    for dict in sorted_list:
        character = dict["character"]
        num = dict["num"]
        print(f"The {character} character was found {num} times")
    print("--- End Report ---")

main()