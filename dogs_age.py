 # Write a Python program to calculate a dog's age in dog's years
# # 
human_age=int(input("enter dogs age in human year"))
if human_age<=2:
   dog_age=human_age*10.5
else:
   dog_age=(21+(human_age-2)*4)
print("dogs age in dogs year",dog_age)
