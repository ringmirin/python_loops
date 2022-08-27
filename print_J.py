# ##print J
for row in range(7):
   for col in range(5):
      if (col==4 or (row==6 and (col!=3 and col!=4 and col!=1 and col!=0)) or col==0 and (row!=0 and row!=1 and row!=2 and row!=3 and row!=6)):
         print("*",end="")
      else:
         print(end=" ")
   print()