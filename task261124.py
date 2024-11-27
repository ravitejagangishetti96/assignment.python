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
string1=input("enter a string here:")

vowels="aeiou"
for i in string1:
    if i in vowels:
        upper_string1=i.upper()
        string=string1.replace(i,upper_string1)
        print("vowels are in uppercase",string)
    else:
        print("No vowels found")

#8. Python program to separate characters in a given string.
print("----------8------------")

string=input("enter a string")
join_string=" ".join(string)
print("show separate charecters:",join_string)

#9. Python program to remove blank space from string.
print("--------------9--------------")

user=input("enter a user name :")
blank_space=user.replace(" ","")
print("no spaces :",blank_space)

#10. Python program to concatenate two strings using join() method. 
print("--------------10-------------")

s=input("enter a string:")
js="".join(s)
print("after joining spaces:",js)

#11. Python program to concatenate two strings without using join() method. 
print('---------------11--------------')

n=input("enter a string here:")
n1=n.replace(" ","=")
print("updated without using join:",n1)

#12. Python program to remove repeated character from string.
print("------------------12---------------------")

string=input("enter a string:")

sub_string=""
for i in string:
    if i not in sub_string:
        sub_string=sub_string + i
print("duplicates",sub_string)

#13. Python program to check given character is vowel or consonant. 
print("---------------13----------------")

n=input("enter the input:")
vowels="aeiou"

if n in vowels:
    print("given charecter is vowels:",vowels)
else:
    print("given charecter is a consonant")

#14. Python program to check given character is digit or not.
print("----------------14-------------")
n=input("enter the input:")
n1=n.isdigit()

if n == n1:
    print("given charater is digit:",n1)
else:
    print("its not a digit")

#15. Python program to delete vowels in a given string.
print("-------------15------------")

n=input("enter the input:")
vowels="aeiouAEIOU"

n1=""
for i in n:
    if n not in vowels:
        n1+=n
print("string after deleting vowels:",n1)

#16. Python program to count the Occurrence Of Vowels & Consonants in a String. 











