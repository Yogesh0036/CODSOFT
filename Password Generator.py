import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"
all_characters = letters + numbers + symbols
length = int(input("How long should the password be? "))
password = ""
for i in range(length):
    password += random.choice(all_characters)
print("Your new password is:", password)
