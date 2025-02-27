def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    for character in text:
        lower_char = character.lower()
        if lower_char not in characters:
            characters[lower_char] = 1
        else:
            characters[lower_char] += 1
    return characters

def sort_characters(char_dict):
    def sort_on(char_dict):
        for char in char_dict:
            return char_dict[char]
    char_list = []
    for char in char_dict:
        if char.isalpha():
            char_list.append({char: char_dict[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    