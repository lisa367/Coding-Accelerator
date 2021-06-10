import sys

argument = str(sys.argv[1])

def majuscule(string):
    final_string = string[0]
    for i in range(1, len(string)):
        Maj = string[i].upper()
        Min = string[i].lower()
        if final_string[i-1] != " " :
            if final_string[i-1] == final_string[i-1].upper():
                    final_string += Min
            elif final_string[i-1] == final_string[i-1].lower() :
                    final_string += Maj

        else:
            if final_string[i-2] == final_string[i-2].upper():
                    final_string += Min
            else :
                    final_string += Maj
    return print(final_string)

majuscule(argument)









