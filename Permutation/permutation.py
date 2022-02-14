#Program pro generování hesel generující všechny kombinace k–písmenných slov
#Vít Ježek, III. ročník BGEKA
#zimní semestr 2021/2022
#Úvod do programování

import re

def permutation(str, tmp=""):
    """
    permutation function

    parameters
    ----------
    str : string
        input word
    tmp : string
        temporary string used by recursion
    """
    #end of recursion 
    if len(str) == 0:
        print(tmp)

    #lock the prefix and permutate rest of the word
    for i in range(len(str)):
            ch = str[i]
            left_part = str[:i]
            right_part = str[i+1:]
            permutation(left_part + right_part, tmp + ch)


def load_data():
    while(True):                                                
        word = input("write word: ")      
        
        #match only if contains letters from EN alphabet
        if not re.match("^[a-zA-Z]*$", word):                              
            print("Not a word, try again")    
            continue                                          
        break
    return word  


def program(): 
    word = load_data()
    permutation(word)

if __name__ == '__main__':
    program()
