# Write your solution here
print("Person1")
name1= input("Name:")
age1= int(input("Age:"))
Person1= age1

print("Person1")
name2= input("Name2:")
age2= int(input("Age:"))
Person2= age2

if Person1 >Person2:
    print (f"Elder is: {name1}")

elif Person2 >Person1:
    print (f"Elder is: {name2}")

else:
    print(f"{name1} and {name2} are the same age")
