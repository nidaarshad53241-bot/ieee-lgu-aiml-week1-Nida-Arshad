def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"


def get_attendance_percentage(classes_held, classes_attended):
    return (classes_attended / classes_held) * 100


def main():
    print("====================================")
    print("   STUDENT GRADE & ATTENDANCE")
    print("====================================")

    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")

    subjects = {}

    print("\nEnter marks for 3 subjects:")

    for i in range(3):
        subject = input(f"\nEnter subject {i + 1} name: ")

        while True:
            try:
                marks = float(input(f"Enter marks for {subject} (0-100): "))

                if 0 <= marks <= 100:
                    subjects[subject] = marks
                    break
                else:
                    print("Please enter marks between 0 and 100.")

            except ValueError:
                print("Invalid input! Please enter a number.")

    average = sum(subjects.values()) / len(subjects)
    grade = get_grade(average)

    print("\n--- Attendance Information ---")

    while True:
        try:
            classes_held = int(input("Enter total classes held: "))
            classes_attended = int(input("Enter classes attended: "))

            if classes_held <= 0:
                print("Total classes must be greater than 0.")
            elif classes_attended < 0 or classes_attended > classes_held:
                print("Attended classes cannot be greater than total classes.")
            else:
                break

        except ValueError:
            print("Invalid input! Please enter whole numbers.")

    attendance = get_attendance_percentage(
        classes_held,
        classes_attended
    )

    if attendance >= 75:
        eligibility = "Eligible for exams"
    else:
        eligibility = "Not eligible for exams"

    print("\n====================================")
    print("          STUDENT REPORT")
    print("====================================")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_number}")

    print("\nSubject Marks:")
    for subject, marks in subjects.items():
        print(f"{subject}: {marks}")

    print(f"\nAverage: {average:.2f}%")
    print(f"Grade: {grade}")
    print(f"Attendance: {attendance:.2f}%")
    print(f"Exam Eligibility: {eligibility}")
    print("====================================")


if __name__ == "__main__":
    main()
