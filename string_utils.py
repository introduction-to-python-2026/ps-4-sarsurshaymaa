def Test_split_before_each_uppercases(formula):
    start = o
    end = 1
    new_list = []

    if not formula:
         return new_list 

    while end < len(formula):
        if formula[end].isupper():
            new_list.append(formula[start:end])
            start = end
            end+=1 
        new_list.append(formula[start:])
        return new_list

 

def split_at_first_digit(formula):
    for i in range(len(formula)):
        if formula[i].isdigit():
            prefix = formula[:i]
            number = int(formula[i:])
            return prefix, number
    return formula, 1
