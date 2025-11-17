def Test_split_before_each_uppercases(formula):

    if not formula:
         return [] 
        
    new_list = [] 
    current = "" 
    
    for char in formula :
        if char.isupper() and current != "":
            new_list.append(current)
            current = char
        else:
            current += char 
            
        new_list.append(current)
        return new_list

 

def split_at_first_digit(formula):
    for i in range(len(formula)):
        if formula[i].isdigit():
            prefix = formula[:i]
            number = int(formula[i:])
            return prefix, number
    return formula, 1
