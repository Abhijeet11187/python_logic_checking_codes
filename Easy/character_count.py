def give_char_count(inputString):
    freq={}
    for char in inputString:
        freq[char]=freq.get(char,0)+1
    return freq

print(give_char_count("aaaabhhddkk"))

#Output is {'a': 4, 'b': 1, 'h': 2, 'd': 2, 'k': 2}