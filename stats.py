def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    lower_text = text.lower()
    characters = list(lower_text)
    
    keys = ["a","b","c","d","e","f","g","h","i","j",
    "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
    " ","æ","â","ô","ê","ë",";","?"]
    #keys = dict.fromkeys(filter_characters, 0)
    value = [0 for _ in range(len(keys))]
    for char in characters:
        for i in range(0,len(keys)):
            if char == keys[i]:
                value[i] += 1


    results = dict(zip(keys, value))
    return results 


def sort_dict(dictionary):
    temp = []
    for keys in dictionary:
        if keys.isalpha():
            temp.append({"char": keys, "number": dictionary[keys]})
    
    temp.sort(reverse=True, key=lambda dict: dict["number"])
    sorted_list = []
    for i in range(0,len(temp)):
        sorted_list.append([temp[i]["char"], temp[i]["number"]])
    return sorted_list
