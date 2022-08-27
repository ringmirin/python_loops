## diamond shape ##
num=int(input("enter the number"))
for x in range(1,num+1):
   print(" "*(num-x)+"* "*x)
for x in range(num-1,0,-1):
      print(" "*(num-x)+"* "*x)
      