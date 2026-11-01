print("========================================")
print("      SCHOOL RESULT PROCESSING          ")
print("========================================")
print("---Enter Marks for 5 subjects (0-100)---")
a=input("Enter Student name:")
c=int(input("Enter Roll Number:"))
d=float(input("Enter marks for subject 1:"))
e=float(input("Enter marks for subject 2:"))
n=float(input("Enter marks for subject 3:"))
b=float(input("Enter marks for subject 4:"))
f=float(input("Enter marks for subject 5:"))
print()
print("===================================")
print("       STUDENT REPORT CARD         ")
print("===================================")

print("Student Name  :",a)
print("Roll Number   :",b)
print("-------------------------------------")

j=e+d+n+b+f
print("Total Marks   :",j,"/500")
y=j/500*100
print("Percentage    :",y,"%")
if 90<=y<100:
    print("Result    :Pass")
    print("Grade     :A")
    print("Remarks   :Excellent")
elif 80<=y<90:
    print("Result     :Pass")
    print("Grade      :B")
    print("Remarks    :Good")
elif 70<=y<80:
    print("Result     :Pass")
    print("Grade      :B")
    print("Remarks    :Average") 
else:
    print("fail")    
print("=====================================")       


