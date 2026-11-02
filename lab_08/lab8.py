print("========================================")
print("      SCHOOL RESULT PROCESSING          ")
print("========================================")
a=input("Enter Student Name:")
c=int(input("Enter Roll Number:"))
print("---Enter Marks for 5 subjects (0-100)---")
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
print("Roll Number   :",c)
print("-------------------------------------")

j=e+d+n+b+f
print("Total Marks   :",j,"/500")
y=j/500*100
print("Percentage    :",y,"%")
if 80<=y<100:
    print("Result      :Pass")
    print("Grade       :A")
    print("Remarks     :Excellent")
elif 70<=y<80:
    print("Result       :Pass")
    print("Grade        :B")
    print("Remarks      :Good")
elif 60<=y<70:
    print("Result       :Pass")
    print("Grade        :C")
    print("Remarks      :Average") 
else:
    print("fail")    
print("=====================================")       


