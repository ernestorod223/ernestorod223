import random

print("Your Password Generator is ready!")

chars = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+"
length = int(input("Enter the length of the password:"))
password = ""
for x in range(length):
    password += random.choice(chars)

    print("Your password is:", password)

