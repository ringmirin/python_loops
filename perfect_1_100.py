##perfect number between 1 to 1000

num=int(input("enter the number"))
for per in range(1,num+1):
   sum=0
   for y in range(1,per):
      if per%y==0:
         sum+=y
   if sum==per:
      print(per)


####perfect number between 1 to 1000

num=int(input("enter the number"))
for per in range(1,num+1):
   sum=0
   for y in range(1,per):
      if per%y==0:
         sum+=y
   if sum==per:
      print(per)