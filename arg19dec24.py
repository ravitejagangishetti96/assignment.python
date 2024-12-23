#Type of arguments:
#positional arguments >> It will assign values based on position.

def book_room(customer_name,room_type,no_of_nights):
    
    print("Room Booked For.",customer_name)
    print("Room Type :",room_type)
    print("number of nights:",no_of_nights)

book_room("Teja","Deluxe",3)

#Keyword arguments >> It will assign values based on key.
print("----------------------------------")

def place_order(order_number,platform,bill_amount,dish):

    print("Order No:",order_number)
    print("Booking platform:",platform)
    print("Dish name:",dish)
    print("Total Bill amount:",bill_amount)
place_order(order_number=111,bill_amount=2000,dish="Chicken biryani",platform="Zomato")

#variable length arguments >> allows you to pass a variable number of positional arguments to a function.It stores arguments in tuple.
print("----------------------------")

def greet(message,*names,**details):
    print(message)
    for name in names:
        print("Hello:",name + "!")
    for key,value in details.items():
        print(key,":"+ str(value))
greet("Welcome to Event","Abhiram",age=24,city="hyderabad")

#keyword variable length arguments >> allows you to pass a variable number of keyword arguments to a function.It stores arguments in dictionary.
print("----------------------------------")

def student_data(**data):
    print(data)
    for key,value in data.items():
        print(key,":",value)
student_data(Name="Ram",standard=10,section="A",Marks_Obtained=580,Total_Marks=600,percentage=96)

#Default arguments >> if caller doesn't provide a value for a arguments,It takes Default value.
print("---------------------------------")

def wish(name="You"):
    print("Happy Birth Day to :",name)
wish()
wish("bhagwan")