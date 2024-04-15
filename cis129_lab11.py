# CIS129_GraceSauber_Lab11.py
# Module 11 Lab-11
# Author: Grace Sauber
# Date: April 15th, 2024
# This program allows the user to choose from three menu options to gather, sort,
# and display student grade data.


def write_grades_to_file():
    # Open the file in write mode
    with open("grades.txt", "w") as file:
        while True:
            # Obtain the user's input for grades
            grade = input("Enter a grade (or 'q' to quit): ")

            # Check if user wants to quit
            if grade.lower() == 'q':
                break

            # Write the grade to the file
            file.write(grade + "\n")

def read_grades_from_file():
    try:
        # Open the file in read mode
        with open("grades.txt", "r") as file:
            grades = file.readlines()

        # Display grades individually
        for i, grade in enumerate(grades, start=1):
            print(f"Grade {i}: {grade.strip()}")

        # Calculate total, count, and average
        total = sum(float(grade) for grade in grades)
        count = len(grades)
        average = total / count

        print(f"Total: {total}")
        print(f"Count: {count}")
        print(f"Average: {average:.2f}")

    except FileNotFoundError:
        print("No grades file found.")

# Calling the function to read grades from the file
read_grades_from_file()

def write_student_records_to_csv():
    # Open the file in write mode
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        while True:
            # Get student information
            first_name = input("Enter student's first name: ")
            if first_name.lower() == 'q':
                break

            last_name = input("Enter student's last name: ")
            exam1_grade = int(input("Enter exam 1 grade: "))
            exam2_grade = int(input("Enter exam 2 grade: "))
            exam3_grade = int(input("Enter exam 3 grade: "))

            # Write the student information into the CSV file
            writer.writerow([first_name, last_name, exam1_grade, exam2_grade, exam3_grade])

# Main program ?
option = input("Choose an option:\n1. Write grades to file\n2. Read grades from file\n3. Write student records to CSV\nEnter your choice: ")

if option == '1':
    write_grades_to_file()
    print("Grades have been written to grades.txt file.")
elif option == '2':
    read_grades_from_file()
elif option == '3':
    write_student_records_to_csv()
    print("Student records have been written to grades.csv file.")
else:
    print("Invalid option. Please choose 1, 2, or 3.")
