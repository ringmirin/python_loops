# Write a program to find the greatest common divisor (GCD) 
# or highest common factor (HCF) of given two numbers.

y=int(input("enter the first number"))
z=int(input("enter the second number")) 
i=1
gcd=0
while i<=y and i<=z:
    if y%i==0 and z%i==0:
        gcd=i
    i=i+1
print(gcd)
