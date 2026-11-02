a = ["Notebook", "Pen", "Eraser", "Ruler"]

print("===================================================")
print("           INVENTORY CONTROL SYSTEM                ")
print("===================================================")

while True:
    print()
    print("Select an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")
    print()

    b = int(input("Enter your choice (1-5): "))
    print()

    if b == 1:
        print("--- Current Inventory ---")
        for i in range(len(a)):
            print(f"{i+1}. {a[i]}")
        print()

    elif b == 2:
        c = input("Enter item name to add: ")
        a.append(c)
        print(f'[SUCCESS] "{c}" added to inventory.')

    elif b == 3:
        d = input("Enter item name to remove: ")
        if d in a:
            a.remove(d)
            print(f'[SUCCESS] "{d}" removed from inventory.')
        else:
            print(f'[ERROR] "{d}" not found in inventory.')

    elif b == 4:
        a.sort()
        print('[SUCCESS] Inventory sorted alphabetically.')
        print("Updated Inventory:")
        for i in range(len(a)):
            print(f"{i+1}. {a[i]}")

    elif b == 5:
        
        break

    else:
        print("[ERROR] Invalid choice! Please enter a number from 1 to 5.")