binary=int(input("enter the number"))
decimal=0
i=0
temp=binary
while temp>0:
   decimal=(temp%2)*(10**i)+decimal
   temp=int(temp/2)
   i=i+1
print(decimal)


##using built-in

print(bin(234))
