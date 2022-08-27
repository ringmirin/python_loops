###1!=1+4!=24+5!=120=145   

###for loop###
n=int(input("enter the number"))
sum=0
temp=n
while temp>0:

   fact=1
   digit=temp%10
   for i in range(1,digit+1):
      fact=fact*i

   sum=sum+fact
   temp//=10
if n==sum:
   print("strong")
else:
   print("not")


   
###while loop  ###
n=int(input("enter the number"))
sum=0
temp=n
while temp>0:
   fact=1
   i=1
   digit=temp%10
   while i<=digit:
      fact=fact*i
      i=i+1
   sum=sum+fact
   temp//=10
if n==sum:
   print("strong")
else:
   print("not")
   
   
   
