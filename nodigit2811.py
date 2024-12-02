#1.Python program to check given character is digit or not  without using isdigit() method.
s = input("Enter a character: ")

if s.isnumeric():
    print("The character is a digit.")
else:
    print("The character is not a digit.")