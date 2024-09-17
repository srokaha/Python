# Continuously ask the user for input until a valid number is provided 
while True:
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
        print("You entered a valid number:", number)
        break
    except ValueError:
        print("Invalid input, please enter a number.")

# Nested If-Else 
mark=int(input("Enter mark: "))
if mark <= 50:
    print("Student fail")
elif 50 < mark <= 60:
    print("Student got : D")
elif 60 < mark <= 75:
    print("Student got : D+")
elif 75 < mark <= 80:
    print("Student got : B") 
elif 80 < mark <= 90:
    print("Student got: B+")
elif 90 < mark <= 95:
    print("Student got : A")
else:
    print("Student got : A+")

# Multiple COnditions Example: Positive, Negative, or Zero
number=int(input("Enter a number: "))
if number > 0:
print("Positive number")
elifnumber==0:
print("Zero")
else:
print("negative number")
email = input(|"Enter your email")
if "@" in email and "." in email:
    print("Valid email address")
else:
    print("Invalid email address")


