a=int(input("Input:"))
b="Enter the number of rows:"
print("Pattern 1: Star Triangle ")
print("----------------------------")

for i in range(1,a+1):
    print("*"*i)
print()
print("Pattern 2: Number Triangle")  
print("-----------------------------")
for c in range(1,a+1):
    for j in range(1,c+1):
        print(j, end=" ")
    print() 
print()
print("Pattern 3:Inverter Star Triangle")  
print("-------------------------------")
for i in range(a,0,-1):
    print("*"*i)
print() 
print("Pattern 4: Pyramid")
print("-------------------------------")
for i in range (1,a+1):
    print(" " * (a-i),end="")
    print("*" * (2 * i - 1))


