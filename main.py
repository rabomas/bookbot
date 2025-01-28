with open("books/Frankenstein.txt") as f:
    file_contents = f.read()

def word_count(string):
    words = string.split()
    return len(words)

total_words = word_count(file_contents)

def character_count(string):
    lowcase_string = string.lower()
    character_dict = {}
    for character in lowcase_string:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

dictionary = character_count(file_contents)

def dict_to_list(dict):
    list = []
    for character, count in dict.items():
        if character.isalpha():
            counter_dict = {"character": character, "count": count}
            list.append(counter_dict)
    return list

character_list = dict_to_list(dictionary)

def sort_on(list):
    return list["count"]

character_list.sort(reverse=True, key=sort_on)

def report_printer(total_words, character_list):
    print("--- Begin report of books/frankenstein.txt ---\n")
    print(f"{total_words} words found in the document\n")
    for item in character_list:
        print(f"the '{item["character"]}' character was found {item["count"]} times\n")    
    print("--- End report ---")
    

report_printer(total_words, character_list)