#indexing in a string-------

name = "Raviteja"

print(name[1])  #positive indexing----left to right 0,1,2,3...

print(name[7])

print(name[0])

topic = "python is a high level progamming language"

print(topic[-1]) #negative indexing---Right to left -1,-2,-3,...

print(topic[-12])

#slicing-------
#   variablename[startindex : endindex]

print(topic[0:7+1])

print(topic[11 : 21])

#   variablename[startindex : endindex : step]

numbers = '1234567890'

print(numbers[0:9:2])

print(topic[0:10:2])

print(numbers[1:10:3])
