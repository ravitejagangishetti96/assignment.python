#1. Basic List Operations:
#1. Write a Python program to create a list of 5 integers and print the sum of all elements in the list.
n=[10,20,30,40,50]
nsum=sum(n)
print("sum of all elements in the list:",nsum)

#2.Create a list of strings containing the names of 5 fruits. Access and print the second and fourth elements using indexing.
print("----------------------------------------")
fruits=["apple","banana","mango","kiwi","cherry"]

print("second fruit:",fruits[1])
print("fourth fruit:",fruits[3])

#3.Create a list of numbers from 1 to 10. Use slicing to print the first three numbers, the last three numbers, and every second number in the list.
print("---------------------------------")
l=[1,2,3,4,5,6,7,8,9,10]

print(l[0:3])
print(l[-3:])
print(l[0:10:2])

#2. Adding and Removing Elements:
#1.Write a Python program that initializes a list with some numbers and:
#2.Adds a new number to the list using the append() method.
print("--------------------------")
l=[10,20,30,40]
print(l)
l.append(50)
print("result after adding:",l)

#3.Inserts a number at the second position using insert().
print("------------------------------------")
l=[10,30,40,50,60]
print(l)
l.insert(1,20)
print("result after insert:",l)

#4.Extends the list with another list of numbers.
print("--------------------------")
l=[10,20,30,40]
print(l)
n1=[50,60,70]
l.extend(n1)
print("result after extending:",l)

#5.Remove all occurrences of the number 3 from a list of integers.
print("-----------------------------")
l=[1,2,3,4,3,5,3,6]
print(l)

while 3 in l:
 l.remove(3)
print("after removing all occurance of 3 : ",l)

#6.Write a Python program to remove the last element of a list using pop() and print the updated list.
print("-----------------------------")
l=[1,2,3,4,5,6]
print(l)
l.pop(-1)
print("updated list:",l)

#3. Sorting and Reversing Lists:
#1.Write a Python program to sort a list of 10 random integers in ascending and descending order using sort() and reverse().
print("-----------------------")
n=[0,3,6,4,9,-3,-5,1,-1,2]
n1=n
n.sort()
print("list in ascending order:",n)
n1.reverse()
print("list in desending order:",n1)


#2.Create a list of strings and reverse the order of elements using both reverse() and slicing [::-1]. Compare the results.
print("-------------------------------")
String=["Hello", "world", "welcome" ,"to", "python"]
print("resversing using slicing:",String[::-1])

s1=String
s1.reverse()
print("reversing the list of strings:",s1)

#4. Aliasing and Cloning:
#1.Create a list of numbers. Assign the list to another variable and modify the original list. Check if the second list also changes. Then, create a copy of the original list and show that modifying the copy does not affect the original list.
print("--------------------------------------")
a=[1,2,3,4,5]
b=a
print("original list: ",a)

b[3]=40
print("after modifying-------")
print("Aliasing list: ",a)
print("Aliasing list: ",b)

b=a.copy()
b[2]=300
print("after using copy-------")
print("Cloning list: ",a)
print("Cloning list: ",b)

#2.Write a Python program to demonstrate how changes in a list's alias affect both lists, while changes in a cloned list do not.
print("------------------------------------------")
ol=[1,2,3,4,5]
al=ol
cl=ol.copy()

print("original list:",ol)
print("alies list:",al)
print("clone list:",cl)

al.append(6)
cl.append(7)
print("after modifying-------")
print("original list:",ol)
print("alies list:",al)
print("clone list:",cl)

#5. Mathematical Operations:
#1.Create two lists of numbers, and use the + operator to concatenate them. Then, use the * operator to repeat the elements of one list 3 times.
print("----------------------------")
l1=[1,2,3]
l2=[4,5,6]

cl=l1 + l2
print("concatenate list:",cl)

rl=l1 *3
print("repeat the elements 3 times: ",rl)

#2.Given a list of numbers, write a Python program to create a new list where each element is doubled (i.e., each element is multiplied by 2).
print("--------------------------------")
l=[1,2,3,4,5]
l1=[]

for i in l:
 l1.append(i * 2)
print("double numbers: ",l1)

#6. Membership Operators:
#1.Write a Python program to check if a specific element (e.g., 5) exists in a given list using the in operator. If it exists, print its position; otherwise, print "Element not found."

print("------------------------")
l=[1,2,3,4,5]

if 5 in l:
 print("Exist in position")
else:
 print("Element not found")

#Given a list of student names, check if "John" and "Sara" are in the list using the in operator.
print("---------------------------------")

student_names=["Nik","zara","John","alice","critie","sara"]

if "John" in student_names:
 print("john found in list ")
if "sara" in student_names:
 print("sara found n list")
else:
 print("students not found :")

#7. Nested Lists:
#1.Write a Python program to create a 3x3 matrix (nested list) and print the matrix. Then, access and print the element at row 2, column 3.
print("-------------------------------------")
matrix = [
    [1, 2, 3],   #index row [0,1,2]     #index column[2]
    [4, 5, 6],   #index row [0,1,2]     #index column[2] 
    [7, 8, 9]    #index row [0,1,2]     #index column[2]
]
element=matrix[1][2]

print(element)

#2.Create a nested list representing a list of students' names and their respective grades. Write a Python program to print each student's name along with their grade.
print("-----------------------------")
students_grades = [["raj", 90],
    ["ravi", 85],
    ["ram", 92],
    ["Abhi", 88],
    ["Sai", 95]
]
print("name :grade")

for student in students_grades:

    print(student[0] + ": " + str(student[1]))

#8. Advanced Challenges:
#1.Create a list of numbers from 1 to 20. Write a Python program to generate two separate lists:
#One containing only the even numbers.
#Another containing only the odd numbers.
print("-------------------------------")
l=[]

for i in range(1,20+1):
 if i%2 ==0:
  l.append(i)
print("Even numbers:",l)

l=[]

for i in range(1,20+1):
 if i%2 !=0:
  l.append(i)
print("Odd numbers:",l)

#2.Write a Python program that reads a list of integers and returns a new list containing only the unique elements (i.e., removing duplicates).
print("--------------------------------------")
l=[1,2,3,4,2,3,5,6]
l1=list(set(l))
print("After removing Duplicates:",l1)
