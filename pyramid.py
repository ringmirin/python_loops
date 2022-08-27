      ##pyramid    
#
num=int(input("enter the number"))

for x in range(num+1):
   print(" "*(num-x)+"* "*x)
for x in range(num-1,0,-1):
   print(" "*(num-x)+"* "*x)
   
   
n=int(input("enter the number"))
for row in range(n):
   for col in range(row+1):
      print(col+1,end=" ")
   print()
   
n=int(input("enter the number"))
for row in range(n):
   for col in range(row,-1,-1):
      print(col+1,end=" ")
   print()


n=int(input("enter the number"))
num=1
for row in range(n):
   for col in range(row+1):
      print(num,end=" ")
      num+=1
   print()