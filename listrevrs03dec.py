#output = "do tahw uoy tnaw"
#output = "want you what do"

s="do what you want"
print(s[::-1])

#reverse list by using slicing:
print("----------------------------")

s="do what you want"

s1 =" ".join(s.split()[::-1]) 
print(s1)

print("-------------------------")
s = "do what you want"
n1 = s.split()[::-1] 
rs = ""

for n in n1:
    rs += n + " "

rs = rs.strip()

print(rs)



