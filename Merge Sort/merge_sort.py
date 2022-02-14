#Merge Sort
#Vít Ježek, III. ročník BGEKA
#zimní semestr 2021/2022
#Úvod do programování

def merge_sort(arr):
    """
    merge sorting function

    parameters
    ----------
    arr : list
        list of integer numbers

    return
    ------ 
    list
        a sorted list of integer numbers
    """
    if len(arr) > 1:
        #split array into two parts
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        #recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        #merge
        i = 0 #left_arr index
        j = 0 # right arr index
        k = 0 # merged arr index
 
        #merging until finish one of the parts
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        #append rest of the left part
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        #append rest of the right part
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


def load_data(): 
    list = []

    while(True):                                                
        n = input("Enter number of elements : ")       
        
        if not n.isnumeric():                               
            print("Not number, try again")    
            continue                                          

        n = int(n)                                      
        
        if(n < 2):                                         
            print("Try again and enter positive integer larger than 2")  
        else:
            break     

    for i in range(0, n):
        while(True):                                                
            ele = input()       
        
            try:
                ele = float(ele)
                break
            except ValueError: 
                print("Not number, try again")    
                                                                                                                                          
        list.append(ele)
    return list

def program():
    list = load_data()
    merge_sort(list)
    print(list)

if __name__ == '__main__':
    program()
