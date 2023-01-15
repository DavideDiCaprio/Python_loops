def print_reversed_string():
    enter_string = input("enter string: ")
    
    for i in range(len(enter_string)):
        
        i = i - 1
        
        print(enter_string[i])


print_reversed_string()
