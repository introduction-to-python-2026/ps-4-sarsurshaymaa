def split_before_each_uppercases(formula):

    if formula == "":
         return [] 
    current=0
    end=1  
    new_list = [] 
  
    
    for char in formula [1:]:
        if char.isupper():
            new_list.append(formula[current:end])
            current = end
        end += 1
            
    new_list.append(formula[current:end])
        
        
    return new_list

 

def split_at_first_digit(formula):
    for i in range(len(formula)):
        if formula[i].isdigit():
            prefix = formula[:i]
            number = int(formula[i:])
            return prefix, number
    return formula, 1
