###Write a Python program to guess a number between 1 to 9
i=0
guess=6
while i<=9:
   g=int(input("guess number from 1 to 9:"))
   if g!=guess: 
      print("guess wrong")
   else:
       print("guess right")
       break
