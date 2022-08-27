
#prime
for num in range(1,200+1):
   if num>1:
      for prime in range(2,num):
         if num%prime==0:
            break
      else:
         print(num)




###write one example of break and continue         

i=1
while i<=4:
   i=i+1
   if i==4:
      continue
   print(i)

##

i=0
while i<=20:
   i+=1
   if i%3==0:
      continue
   print(i)
    
##break
i=0
while i<=10:
   i+=1
   if i%5==0:
      break
   print(i)


#######
##prime
for num in range(1,200+1):
   if num>1:
      for prime in range(2,num):
         if num%prime==0:
            break
      else:
         print(num)









