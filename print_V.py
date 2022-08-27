# #print V ##

for row in range(6):
   for col in range(5):
      if ((col==0 or col==4) and row!=4 and row!=5) or (row==4 and col==1) or (row==4 and col==3) or (col==2 and row==5):
         print("*",end="")
      else:
         print(end=" ")
   print()
