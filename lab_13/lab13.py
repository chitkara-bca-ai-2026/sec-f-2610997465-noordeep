a=["notebook","pen","eraser","ruler"]
# print(a.insert(1,"marker"))
# print(a)
# print(a.remove("pen"))
# print(a)
# print(a.sort())
# print(a)
print("===================================================")
print("           INVENTORY CONTROL SYSTEM                ")
print("===================================================")
print()
print("Select an operation:" )
print("1.View Inventory")
print("2.Add Item")
print("3.Remove Item")
print("4.Sort Inventory")
print("5.Exit")
print()
while True:
    b=int(input("Enter your choice (1-5):"))
    print()
    if b==1:
        print("---Current Inventory---")
        print(a[0])
        print(a[1])
        print(a[2])
        print(a[3])
        print()
    elif b==2:
        c=input("Enter item name to add:")
        print("[SUCCESS],c ,added to inventory")
        print(a.insert(1,c))
        print(a)
    elif b==3:
        d=input("Enter item name to remove:")
        print("[SUCCESS],d,removed from inventory")
        print(a.remove(d))
        print(a)
    elif b==4:
        print(a.sort())
        print(a)
    elif b==5:
        break
    else:
        print("invalid option")    

print("---Current Inventory---")
print(a)

