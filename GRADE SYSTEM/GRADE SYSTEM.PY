# Loop until user enters valid marks
while True:
    try:
        marks = float(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print(" Please enter a number between 0 and 100.")
    except ValueError:
        print(" Invalid input! Please enter a number.")

# Grade calculation
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)
