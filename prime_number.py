####prime number {2,3,5,7,11,17......}
    
for i in range(1,100+1): 
   if i>1:
      for j in range(2,i):
         if (i%j)==0:
            break
      else:
         print(i)



#####
n=int(input("enter the number"))
count=0
i=1
while i<=n:
   if (n%i==0):
      count+=1
   i+=1
if count==2:
   print("prime")
else:
   print("not prime")







   

   
