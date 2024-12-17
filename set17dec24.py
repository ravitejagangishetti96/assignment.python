#1.Write a program to create a set.
set={1,2,3,4,5}
print("my set:",set)


#2.Write program to iterate over sets.
print("------------------------")


for element in set:
    print("Iterate over element:", element)

#3.Write a Python program to add member to a set.
print("-----------------------------")

set = {1, 2, 3, 4, 5}
set.add(6)

print("element added to set:",set)

#4.Write a Python program to remove item from a given set.
print("----------------------------")

set = {1, 2, 3, 4, 5, 6, 7}
set.remove(6)
set.remove(7)

print("element removed from set:",set)

#5.Write a python program to create a intersection of set ?
print("---------------------------------------")

set1={1,2,3,4,5}
set2={4,5,6,7,8}

intersection_set = set1.intersection(set2)

print("After intersection:",intersection_set)

#6.Write a python program to createa unionof set ?
print("--------------------------------")

set1={1,2,3,4,5}
set2={4,5,6,7,8}

union_set = set1.union(set2)

print("union of two sets:",union_set)

#7.Write a python program to create set differance ?
print("---------------------------------")

set1={1,2,3,4,5}
set2={4,5,6,7,8}

difference_sets = set1.difference(set2)

print("difference in set:",difference_sets)

#8.Write a python program to create a symmetric defferance ?
print("---------------------------------")

set1={1,2,3,4,5}
set2={4,5,6,7,8}

symmetricdifference_sets = set1.symmetric_difference(set2)

print("After symmetric difference of sets:",symmetricdifference_sets)

#9.write a python program to find max and min values in a set?
print("--------------------------")

set = {1,2,3,4,5,6,7,8,9}

maximum_value = max(set)

minimum_value = min(set)

print("maximum value of set:",maximum_value)

print("minimum value of set:",minimum_value)

#10.Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.
print("-----------------------------------")

set1={1,2,3,4,5}
set2={4,5,6,7,8}

difference_update_sets = set1.difference(set2)

print("Difference upadated in first set:",difference_update_sets)

#11.Write a Python program to remove items 10, 20, 30 from the following set at once.?
print("-------------------------------")

set ={10,20,30,40,50,60}

for element in [10,20,30]:
    set.remove(element)
print("After removing elements from set:",set)

#12.Check if two sets have any elements in common. If yes, display the common elements?
print("----------------------------------")

set1={1,2,3,4,5}
set2={4,5,6,7,8}

commom_elements = set1.intersection(set2)

if element:
    print("common elements exist:",commom_elements)
else:
    print("No common elements")

#13.Update set1 by adding items from set2, except common items?
print("------------------------------")

set1={1,2,3,4,5}
set2={4,5,6,7,8}

common_items = set1.union(set2)

print("updated sets:",common_items)

#14.Remove items from set1 that are not common to both set1 and set2?
print("------------------------------")

set1={1,2,3,4,5}
set2={4,5,6,7,8}

commom_elements= set1.intersection(set2)

print("Not Common:",commom_elements)

#15.
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





