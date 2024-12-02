#adding element to list
#append >> add elements to the end of the list

l=[]
for i in range(1,20+1):
    l.append(i)
print(l)

#odd numbers
print("---------------------------------")
l=[]
for i in range(1,20):
    if i%2 !=0:
        l.append(i)
print(l)

#even numbers only
print("-------------------------------")
l=[]

for i in range(1,12):
    if i%2 ==0:
        l.append(i)
print(l)

#Python program that prints a list of integers divisible by 7 but not divisible by 5 from 100 to 200:
print("-----------------------------------")
l=[]

for i in range(100,200):
    if i%7 ==0 and i%5 !=0:
        l.append(i)
print(l)

#Python program that prints a list of integers divisible by 8 and  also divisible by 3 from 100 to 200:
print("-------------------------------")
l=[]

for i in range(100,200+1):
    if i%8 ==0 and i%3 ==0:
        l.append(i)
print(l)

l1=[300,400,500]

for i in l1:
    l.append(i)
print(l)