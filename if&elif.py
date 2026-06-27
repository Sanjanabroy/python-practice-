m1=int(input("enter marks english "))
m2=int(input("enter marks hindi "))
m3=int(input("enter marks marathi "))
total=m1+m2+m3
per=(total/300)*100
print ('total',total,'per',per)
if per>=75:
    print("grade A")
elif per>=60:
    print("grade B")
elif per>=50:
    print("grade C")
else:
    print("fail")
 
    
    
       


