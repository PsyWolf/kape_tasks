
characters_map = { 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz" }

digits = "37"

def get_combinations(digits:str, result:list[str], combination:str="", pos:int=0) -> None:
    digit = int(digits[pos])
    options = characters_map[digit]
    for letter in options:
        new_combination = combination + letter
        if len(new_combination) == len(digits):
            result.append(new_combination)
        else:
            get_combinations(digits, result, new_combination, pos+1)

def get_letter_combinations(digits:str):
    length = len(digits)
    result = []
    if length <= 4:
        for digit in digits:
            if not digit.isdigit():
                print("Please enter valid digits 2-9")
                return result
            digit = int(digit)
            if digit < 2 or digit > 9:
                print("Please enter valid digits 2-9")
                return result
        if length != 0:
            get_combinations(digits, result)
    else:
        print("digits length should be 0-4")
    return result

print("input: a")
result = get_letter_combinations("a")
print(result)

print("input: 012")
result = get_letter_combinations("012")
print(result)

print("input: 87654")
result = get_letter_combinations("87654")
print(result)

print("input: 28")
result = get_letter_combinations("28")
print(result)

print("input: 479")
result = get_letter_combinations("479")
print(result)

print("input: empty")
result = get_letter_combinations("")
print(result)
