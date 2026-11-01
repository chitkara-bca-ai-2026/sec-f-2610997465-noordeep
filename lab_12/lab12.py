a=input("Input:")
print()
print("Enter a sentence: ")
print("===================================")
print("DOCUMENT ANALYSIS REPORT           ")
print("===================================")
print("Sentence:",a)
print("Total characters:",len(a))
print()
print("---Character Breakdown---")
words=0
vowel="aeiouAEIOU"
count=0
digits=0
spaces=0
specialcharacters=0
consonants=0
for i in a:
    if i==" ":
        words+=1
        spaces+=1
    elif i in vowel:
     count+=1 
    elif i.isalpha():
       consonants+=1  
    elif i.isdigit():
        digits+=1  
    
    else:
        specialcharacters+=1          

print("Words:"       ,words+1) 
print("Vowels:"      ,count)
print("Consonants:"   ,consonants)
print("Digits:"        ,digits) 
print("Spaces:"         ,spaces)
print("Special characters:",specialcharacters)  
print()
c=words+1
print("---Summary---")
print("Total letters:",consonants)
print("Vowel percentage:",count/(consonants+count)*100,"%")
print()
print()
print("==================================================================")
print("Analysis Complete                                          ")
print("==================================================================")    

