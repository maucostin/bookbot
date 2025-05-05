def word_count(text):
    words= text.split()
    return len(words)

def char_counter(text):
    charcount = {}
    
    for c in text:
        c = c.lower()
        charcount[c]= charcount.get(c,0)+1
        
    return charcount

def sort_on(dict):
    return dict["num"]

def sort_text(letter_dict):
    sorted_list =[]
    for char in letter_dict:
        if char.isalpha():
            pair ={"name":char,"num":letter_dict[char]}
            sorted_list.append(pair)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


