s=input("enter the input:")
alphabet_count = 0
digit_count = 0
special_char_count = 0

for char in s:
    if char.isalpha():  
            alphabet_count += 1
            print(f"Alphabets: ")
    elif char.isdigit():  
            digit_count += 1
            print(f"Digits: ")
    else:  
            special_char_count += 1
            print(f"Special Characters:")