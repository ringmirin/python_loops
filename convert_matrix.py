# convert character matrix to single string

num=[["g","f","g"],["i","s"],["b","e","s"]]
str=" "
i=0
while i<len(num):
   j=0
   while j<len(num[i]):
      str=str+num[i][j]
      j+=1
   i+=1
print(str)

