#1. Python Program to count occurrence of a given characters in string. 

string=input("enter the string:")
char_count=input("enter the charecter to count:")

count_string=string.count(char_count)

print("the charecter count is: ",count_string)

#2. Python Program to check if two Strings are Anagram.
print("--------------2--------------------")

string1=input("enter the first string:")
string2=input("enter the second string:")

if sorted(string1) == sorted(string2):
    print("both strings are anagram")
else:
    print("not anagram")

#3. Python program to check a String is palindrome or not. 
print("-----------------------3---------------------")
s=input("enter a string:")
if s==s[::-1]:
    print("given string is palindrome")
else:
    print("given is not a polindrome")

#4. Python program to replace the string space with a given character. 
#5. Python program to replace the string space with a given character using replace() method. 
print("----------------------5------------------")
input_string1=input("enter the string:")
char_replace=input("enter a charecter to replace spaces with:")
new_string=input_string1.replace(" ",char_replace)
print("string before replacing: ",input_string1)
print("updated string:",new_string)

#6. Python program to convert lowercase char to uppercase of string.
print("------------------6-------------")
statement=input("enter the statement here:")
lower_statement=statement.upper()
print("updated ststement to uppercase:",lower_statement)

#7. Python program to convert lowercase vowel to uppercase in string. 
print("----------------7-------------------")
string1 = input("Enter a string here: ")

vowels = "aeiou"
updated_string = string1 

for i in string1:
    if i in vowels:  
        updated_string = updated_string.replace(i, i.upper())  

if updated_string == string1:
    print("No vowels found")
else:
    print("Vowels are in uppercase:", updated_string)

#8. Python program to separate characters in a given string.
print("----------8------------")

string = input("Enter a string: ")

join_string = " ".join(string)

print("Separated characters:", join_string)
#9. Python program to remove blank space from string.
print("--------------9--------------")

user = input("Enter a username: ")

blank_space = user.replace(" ", "")

print("No spaces:", blank_space)

#10. Python program to concatenate two strings using join() method. 
print("--------------10-------------")

s=input("enter a string:")
js="".join(s)
print("after joining spaces:",js)

#11. Python program to concatenate two strings without using join() method. 
print('---------------11--------------')

n = input("Enter a string here: ")

n1 = n.replace(" ", "=")

print("Updated string after replacing spaces with '=':", n1)

#12. Python program to remove repeated character from string.
print("------------------12---------------------")

string = input("Enter a string: ")

sub_string = "" 
for i in string:
    if i not in sub_string: 
        sub_string += i

print("String without duplicates:", sub_string)

#13. Python program to check given character is vowel or consonant. 
print("---------------13----------------")

n = input("Enter the input: ").lower()  
vowels = "aeiou"

if n in vowels and len(n) == 1:  
    print(f"Given character is a vowel.")
else:
    print(f"Given character is a consonant.")

#14. Python program to check given character is digit or not.
print("----------------14-------------")

n = input("Enter the input: ")

if n.isdigit():
    print("Given character is a digit:", n)
else:
    print("It's not a digit")


#15. Python program to delete vowels in a given string.
print("-------------15------------")

n=input("enter the input:")
vowels="aeiouAEIOU"

n1=""
for i in n:
    if i not in vowels:
        n1+=i
if len(n1)==len(n):
    print("no vowels found")
else:
    print("string after deleting vowels:",n1)

#16. Python program to count the Occurrence Of Vowels & Consonants in a String. 
print("----------------16---------------------")
string = input("Enter a string: ")

vowel_count = 0
consonant_count = 0

vowels = "aeiouAEIOU"

for char in string:
    if char.isalpha():  
        if char in vowels:
            vowel_count += 1
        else:  
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

#17. Python program to print the highest frequency character in a String
print("-------------17------------------------")

s = input("enter a string :")
print(s.count("n"))
d = {}
for char in s:
    if char in d:
        d[char] += 1
    else:
        d[char] =1
print(max(d.values()))
print(max(d, key=d.get))
hfe = max(d, key=d.get)
r = {hfe:d[hfe]}
print(r)

#18. Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.
print("-------------------18--------------------")

user=input("enter a input here:")

vowels="aeiou"

user1=list(user)
for i in range(len(user1)):
    if user1[i] in vowels:
        user1[i] = '-'
        break
user2=''.join(user1)

print("updated input:",user2)

#19. Python program to count alphabets, digits and special characters. 
print("----------------19----------------")

user=input("enter the input:")
alphabet_count = 0
digit_count = 0
special_char_count = 0

for char in user:
    if char.isalpha():  
            alphabet_count += 1
            
    elif char.isdigit():  
            digit_count += 1
            
    else:  
            special_char_count += 1
            
print("Alphabets: ",alphabet_count)
print("Digits: ",digit_count)
print("Special Characters:",special_char_count)

#20. Python program to check given character is digit or not using isdigit() method. 
print("-------------20---------------")
s = "praveen1234"
count = 0
for char in s:
    if char.isdigit():
        count = count + int(char)
    else :
        pass
print(count)

#21. Python program to calculate sum of integers in string. 
print("--------------------21------------------")

s =" welcome to my world"
nc = ""
for char in s:
    if char not in nc:
        nc = nc + char
print(nc)
#23. Python program to copy one string to another string
string=input("enter a string:")

copy_string=string

print("copied string:",copy_string)
















