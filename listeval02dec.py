#list

l=eval(input("enter your list:"))
print(l[0])
print(type(l))

print(type(l[1]))

#list without using eval
print("------------------------")

num=input("enter your list:")
l=num.split(",")
print(l[0])
print(type(l))

print(type(l[1]))
