print("===calculations===")
a=float(input("Total fee (before discount):Rs"))
b=float(input("Final fee (after discount):Rs"))
c=float(input("Annual fee (2 semesters):Rs"))
d=float(input("Monthly installment:Rs"))
print("=======================================================================\n        fee summary   \n=======================================================================")
e=float(input("Tution Fee                                      :Rs"))
f=float(input("Lab Fee                                         :Rs"))
g=float(input("Library Fee                                     :Rs"))
h=float(input("Exam fee                                        :Rs")) 
i=e+f+g+h
print(        "Total Fee                                       :Rs",i)
j=float(input("Discount                                        :Rs"))
k=i-j
print(         "Final Fee                                      :Rs",k)
l=k*2
print(         "Annual Fee                                     :Rs",l)
i=l/12
print(         "Monthly fee                                    :Rs",i)
print("======================================================================")


      