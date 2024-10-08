name = input("Enter your name : ")

realName = (f"User {name}")

age = int(input("Enter your age : "))

realAge = (f"age : {age}")

if age >= 18:
    print("You're welcome")     
else:
    print("wait for some years to reach legal age")

print(realName)
print(realAge)