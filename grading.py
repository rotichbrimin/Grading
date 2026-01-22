student_number = 0

while True:
    name = input("Enter student name: ")
    student_number += 1

    while True:
        try:
            marks = int(input("Enter student's marks between 0 and 100: "))
            if 0 <= marks <= 100:
                break
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    if marks >= 90:
        grade = "A"
        comment = "Excellent"
    elif marks >= 80:
        grade = "A-"
        comment = "Very Good"
    elif marks >= 70:
        grade = "B+"
        comment = "Good work"
    elif marks >= 60:
        grade = "B"
        comment = "Good! Aim even higher"
    elif marks >= 50:
        grade = "C+"
        comment = "Satisfactory"
    elif marks >= 40:
        grade = "C"
        comment = "Pass"
    else:
        grade = "F"
        comment = "Fail. Better luck next time"

    print(f"\nStudent: {name}")
    print(f"Marks : {marks}")
    print(f"Grade : {grade} — {comment}")

    next_student = input("\nEnter another student? (yes/no): ").lower()
    if next_student != "yes":
        break

print(f"\nTotal students entered: {student_number}")
