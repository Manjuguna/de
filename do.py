gk=int(input())
if gk< 1:
   
     print("no")
    
else:
   for i in range(2,gk):
       if (gk % i) == 0:
           print("no")
           break
           
   else:
       
       print("yes")
