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
    if len(str) == 0:
        print(tmp)

    for i in range(len(str)):
            ch = str[i]
            left_part = str[:i]
            right_part = str[i+1:]
            permutation(left_part + right_part, tmp + ch)

while(True):                                                
    word = input("write word: ")      
    
    if not re.match("^[a-zA-Z]*$", word):                              
        print("Not a word, try again")    
        continue                                          
    break

permutation(word)
