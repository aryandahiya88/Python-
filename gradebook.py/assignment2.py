import csv
import statistics

def calculate_average(marks):
    return sum(marks.values()) / len(marks)

def calculate_median(marks):
    return statistics.median(marks.values())

def find_max_score(marks):
    return max(marks.values())

def find_min_score(marks):
    return min(marks.values())

def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_student_data():
    marks = {}
    choice = input("Enter 1 for manual input or 2 to load CSV: ")
    if choice == "1":
        n = int(input("Number of students: "))
        for _ in range(n):
            name = input("Student name: ")
            mark = int(input(f"Mark for {name}: "))
            marks[name] = mark
    elif choice == "2":
        file_name = input("Enter CSV file name: ")
        try:
            with open(file_name, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row:
                        marks[row[0]] = int(row[1])
        except:
            print("CSV file not found. Switching to manual input.")
            return get_student_data()
    return marks

def analyze_marks(marks):
    grades = {name: assign_grade(score) for name, score in marks.items()}
    grade_counts = {g: list(grades.values()).count(g) for g in ["A","B","C","D","F"]}
    passed_students = [name for name, score in marks.items() if score >= 40]
    failed_students = [name for name, score in marks.items() if score < 40]

    print("\nAverage:", round(calculate_average(marks),2))
    print("Median:", round(calculate_median(marks),2))
    print("Max:", find_max_score(marks))
    print("Min:", find_min_score(marks))
    print("\nGrade Distribution:")
    for g in ["A","B","C","D","F"]:
        print(f"{g}: {grade_counts[g]}")
    print("\nPassed:", len(passed_students), passed_students)
    print("Failed:", len(failed_students), failed_students)

    print("\nName           Marks  Grade")
    print("-"*30)
    for name, score in marks.items():
        print(f"{name:<15}{score:<7}{grades[name]}")

def main():
    print("Welcome to GradeBook Analyzer")
    while True:
        marks = get_student_data()
        analyze_marks(marks)
        again = input("\nAnalyze another set? (y/n): ")
        if again.lower() != 'y':
            break
    print("Goodbye!")

if __name__ == "__main__":
    main()
