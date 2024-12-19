#1.Define a function called `greet` that takes a name as an argument and prints a greeting message like: "Hello, [name]!"

def greet():
    name = input("Enter your name here: ") 
    greet_message = f"Hello, {name}!"
    print(greet_message)
greet()

#2.Write a function `add_numbers` that takes two numbers as arguments and returns their sum. Test the function by passing different numbers.
print("----------------------------------")

def add_numbers():
    a = int(input("enter first number:"))
    b = int(input("enter a second number:"))

    print(f"The sum of the two numbers:{a + b}")
add_numbers()

#3.Create a function `is_even` that takes a number as an argument and returns `True` if the number is even, and `False` otherwise.
print("----------------------------")

def is_even():
    i = int(input("eneter a number :"))

    if i % 2==0:
        print(True)
    else:
        print(False) 
is_even()

#4.Write a function `factorial` that takes a positive integer as input and returns the factorial of that number. Remember, `factorial(5)` should return \(5 \times 4 \times 3 \times 2 \times 1 = 120\).
print("--------------------------------")

def factorial(n):
    if n == 0 or n == 1:  

        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number: "))  
print(factorial(n)) 

#5.Define a function `find_max` that takes three numbers as input and returns the largest of the three. Test the function with various sets of numbers.
print("------------------------------------")

def find_max(n1, n2, n3):
    print(max(n1, n2, n3))
n1 = input("enter the first number: ")
n2 = input("enter the second number: ")
n3 = input("enter the third number: ")
find_max(n1, n2, n3)

#6.Write a function `count_vowels` that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.
print("----------------------------------")

def count_vowels(str):
    vowels = "aeiouAEIOU"  
    count = 0

    for i in str:
        if i in vowels:
            count = count + 1
    print("count of vowels in given string is: ",count)
str = input("enter a string: ")
count_vowels(str)

#7.Create a function `is_prime` that takes a number as input and returns `True` if the number is prime, and `False` otherwise.
print("------------------------------------")

def is_prime(n):
    if n <= 1:  
        print(False)
    else:
        for i in range(2, n):  
            if n % i == 0:  
                print(False)
                break
        else:
            print(True)  


n = int(input("Enter a number: "))
is_prime(n)

#8.Write a recursive function `recursive_sum` that takes a positive integer `n` and returns the sum of all numbers from 1 to `n`. For example, `recursive_sum(5)` should return \(1 + 2 + 3 + 4 + 5 = 15\).
print("----------------------------------------")

#9.Write a function `calculator` that takes three parameters: two numbers and an operator (as a string: `"+"`, `"-"`, `"*"`, `"/"`). The function should perform the operation on the two numbers and return the result.
print("------------------------------------------")

def calculator(num1, num2, operator):
    if operator == "+":
        print("addition of 2 number is: ", num1 + num2)
    elif operator == "-":
        print("substraction of 2 nmbes is: ", num1 - num2)
    elif operator == "*":
        print("multiplication of 2 numbers is: ", num1 * num2)
    elif operator == "/":
        print("division of 2 no is: ",num1 / num2)
    else:
        print("Invalid operator")
num1 = int(input("enter the  firt number: "))
num2 = int(input("enter the second number: "))
operator = input("enter the operator: ")
calculator(num1, num2, operator)


#10.Write a function `find_common_elements` that takes two lists as input and returns a list of elements that are present in both lists.
print("------------------------------------------")

l = []
def find_common_elements(l1, l2):
    for i in l1:
        if i in l2:
            l.append(i)
    print(l)
    
l1 = [1, 2, 3, 4, 6]
l2 = [3, 1, 6, 8]
find_common_elements(l1, l2)


#11.Write a function `reverse_string` that takes a string as input and returns the string reversed.
print("-------------------------------")

def reverse_string(str):
    rs = str[::-1]
    print(rs)
str = input("enter the string: ")
reverse_string(str)


#12.Write a function `sort_dict_by_value` that takes a dictionary as input and returns a list of tuples sorted by the dictionary values in ascending order.
print("--------------------------------")

def get_value(item):
    return item[1]  

def sort_dict_by_value(d):
    
    sorted_list = sorted(d.items(), key=get_value)
    
    for item in sorted_list:
        print(item)

my_dict = {'ravi': 10, 'sita': 20, 'ram': 40}
sort_dict_by_value(my_dict)