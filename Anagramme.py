import sys
argument1 = str(sys.argv[1])
argument2 = str(sys.argv[2])

with open(argument2) as input_file :
    text = input_file.read()
    list_of_words = text.split('\n')

def anagramme(word):
    # Etape 1:
    unique_letters = []
    frequency = []
    for letter in word:
        if unique_letters.count(letter) == 0 :
            unique_letters.append(letter)
    for letter in unique_letters:
        freq = word.count(letter)
        frequency.append(freq)

    # Etape 2:
    list_of_anagramms = []
    for item in list_of_words:
        if len(item) == len(word):
            freq_item = []
            for letter in unique_letters:
                occurence = item.count(letter)
                freq_item.append(occurence)
            if freq_item == frequency:
                list_of_anagramms.append(item)
            else:
                continue
        else:
            continue
    return print(list_of_anagramms)

anagramme(argument1)
