password = input("Enter the password : ")

result = {}

# To check the password length
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

# To check if the password has at least 1 digit
digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digit"] = digit

# To check if the password has at least 1 uppercase
uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result["uppercase"] = uppercase

if all(result.values()):
    print("Strong password")
else:
    print("Weak password")
