#1.Python program to check given character is digit or not  without using isdigit() method.
s = input("Enter a character: ")

if s.isnumeric():
    print("The character is a digit.")
else:
    print("The character is not a digit.")

#2.Python program to Replace last Occurrence Of Vowel With ‘-‘ in String.
print("---------------------------------------")
n = input("Enter a string: ")

vowels = "aeiouAEIOU"
lv = -1

user1 = len(n)

for i in n:
    if n[i] in vowels:
        lv = i  
     
print(user1)

#python program to find index values of a mid charector
print("_______________________________")

string=input("enter a string:")

ms=len(string) // 2

r=string[ms]

print("mid char:",r)


