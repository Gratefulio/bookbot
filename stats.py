def counting(text):
    words = text.split()
    num_words = len(words)
    return num_words

def character_count(text):
    num_character = {}
    lower_case = text.lower()
    for character in lower_case:
        if character in num_character:
            num_character[character] += 1
        else:
            num_character[character] = 1
    return num_character

def sort_list(character_count):
    dic_list = []
    for character in character_count:
        dic_list.append({"char": character, "num": character_count[character]})
    dic_list.sort(reverse=True, key=sort_on)
    return dic_list

def sort_on(items):
    return items["num"]


    

