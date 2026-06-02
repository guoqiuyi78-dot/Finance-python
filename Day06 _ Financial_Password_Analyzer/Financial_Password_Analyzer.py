password = input("Enter password: ")

length = len(password)

print("Password length:", length)

if length < 8:
    print("Password is too short.")
else:
    print("Password length is acceptable.")

digit_count = 0
a_count = 0

for letter in password:

    if letter.isdigit():
        digit_count = digit_count + 1

    if letter == "a":
        a_count = a_count + 1

print("Number of digits:", digit_count)
print("Number of letter a:", a_count)