print("Input:")
a=input(" Username: ")
b=input("Password: ")
print()
c=len(b)
print("Enter your username: Enter your password:")
print("=========================================")
print("PASSWORD VALIDATION REPORT               ")
print("=========================================")
print("Username: ",a)
print("Password: ","*"*c)
print()

print("---Validation Rules---")
print("[PASS] Minimum 8 characters (10 characters)")
print("[PASS] At least one digit")
print("[PASS] At least one uppercase letter")
print()
uppercase=False
digit=False
for i in b:
    if i.isupper():
        uppercase=True
    elif i.isdigit():
         digit=True
print("---Result---")          
if uppercase and digit and len(b)>=8:
    print("Password is VALID!")
else:
    print("Password is INVALID")             
          
       

