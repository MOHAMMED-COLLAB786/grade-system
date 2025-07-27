<h1>grade-system</h1>
<br>
<p></p>This is a simple Python project that calculates and displays a student's grade based on the marks entered.</p>
<br>
<h1></h1>Grade Calculator (Python)</h2>
<br>
brief description about the python program
<br>
This is a beginner-friendly Python program to calculate grades based on marks out of 100.

- A+ : 90–100
- A  : 80–89
- B  : 70–79
- C  : 60–69
- D  : 50–59
- F  : Below 50
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
