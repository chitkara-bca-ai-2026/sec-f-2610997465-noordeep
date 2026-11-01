print("=============================================")
print("       CALENDER VERIFICATION SYSTEM          ")
print("=============================================")
a=int(input("Enter year:"))
print("---------------------------------------------")

print("Year            :",a)
if a<0:
    print("status          :Not a leap year")
    print("Days in Year    :365 days")
    print("Days in February:28 days")
    print("Reason          :Not Divisible by 4 and a century year")    
elif a%4==0:
    print("Staus           :LEAP YEAR")
    print("Days in Year    :366 days")
    print("Days in February:29 days")
    print("Reason          :Divisible by 4 and not a century year")
    
else:
    print("status          :Not a leap year")
    print("Days in Year    :365 days")
    print("Days in February:28 days")
    print("Reason          :Not Divisible by 4 and a century year")
print("----------------------------------------------")