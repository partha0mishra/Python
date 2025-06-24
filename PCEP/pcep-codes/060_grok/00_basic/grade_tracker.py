# grade_tracker.py
def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

def get_student_summary(student_name, grades_dict):
    if student_name in grades_dict:
        grades = grades_dict[student_name]
        avg = calculate_average(grades)
        return (student_name, avg)  # Tuple: (name, average)
    return None

# Main program
students = {
    "Alice": [85, 90, 88],
    "Bob": [78, 82, 80],
    "Charlie": [95, 92]
}

if __name__ == "__main__":
    while True:
        action = input("Enter 'add', 'view', or 'quit': ").lower()
        if action == "quit":
            print("Exiting...")
            break
        elif action == "add":
            name = input("Student name: ")
            grade = float(input("Grade: "))
            if name in students:
                students[name].append(grade)  # Add to existing list
            else:
                students[name] = [grade]  # New list for new student
            print(f"Added {grade} for {name}")
        elif action == "view":
            name = input("Student name: ")
            summary = get_student_summary(name, students)
            if summary is None:
                print(f"{name} not found")
            else:
                print(f"{summary[0]}'s average: {summary[1]:.2f}")
        else:
            print("Invalid action")