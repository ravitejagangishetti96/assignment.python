#Removing spaces from string

username = "raviteja "

#strip()
print(len(username))

ss = username.strip()
print(ss)

print(len(ss))

#strip()
username = " raviteja "
print(len(username))

rs = username.rstrip()  #right strip-----

print(len(rs))

#lstrip()
username = " raviteja "
print(len(username))

ls = username.lstrip() 
print(len(ls))


#replace(-----------------)
s = "python is a high level progamming language"

ns = s.replace(" ","")      #ns:no space 

print(ns)

rs = s.replace("python","java") #rs:replace of string

print(rs)

ns = s.replace(" ","*")

print(ns)

