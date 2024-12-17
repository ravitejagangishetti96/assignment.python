#16.Write a python program to  add a key to a dictionary ?
print("------------------------------")

dict = {"name" :"ravi", "age" :25}

dict["city"]="hyd"

print("After add key to dictionary:",dict)

#17.Write a python program to check weather the given value is present in the dictionary or not ?
print("-------------------------------")

dict = {'name': 'ravi', 'age': 25, 'city': 'hyd'}

value = "ravi"

if value in dict.values():
    print("value present in dictionary:",value)
else:
    print("value not present in dictionary")

#18.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
print("------------------------------")

d={}

for i in range(1,15+1):
    d[i] = i ** 2

print("squares of the keys:",d)

#21.Write a python program to create a dictionary from the string ?
print("-------------------------------")

string1 = "hello world"

char_count = {}

for char in string1:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print("char count in dictionary:",char_count)

#22.Write a python program to combine two dictionaries by adding values of common keys ?
print("------------------------")

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 15, "c": 25, "d": 35}

combined_dict = dict1.copy()

for key, value in dict2.items():
    if key in combined_dict:
    
        combined_dict[key] += value
    else:
    
        combined_dict[key] = value
print("Combined Dictionary:", combined_dict)

#23.Write a python program to merge two python dictionaries ?
print("--------------------------------")
dict1 = {"a": 10, "b": 20}
dict2 = {"b": 30, "c": 40}

dict1.update(dict2)

print("Merged Dictionary:", dict1)

#24.Write a Python program to create a dictionary from a string.  Note: Track the count of the letters from the string.
print("-----------------------------------------")

string1 = 'skywavessoftwares'

char_count = {}

for char in string1:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print("char count in dictionary:",char_count)