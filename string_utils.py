def split_before_each_uppercase(formula):
    if not formula:
        return []

    new_list = []
    current = formula[0]

    for char in formula[1:]:
        if char.isupper():
            new_list.append(current)
            current = char
        else:
            current += char

    new_list.append(current)
    return new_list

def split_at_digit(formula):
    for i in range(len(formula)):
        if formula[i].isdigit():
            prefix = formula[:i]
            number = int(formula[i:])
            return prefix, number
    return formula, 1
