def calculate_student_marks():
    """Main function to calculate marks, percentage and assign grade"""
    
    print("=" * 50)
    print("STUDENT MARKS CALCULATOR & GRADE ASSIGNER")
    print("=" * 50)
    
    # Take input for number of subjects
    while True:
        try:
            num_subjects = int(input("\nEnter number of subjects: "))
            if num_subjects <= 0:
                print("Please enter a positive number!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    marks = []
    max_marks_per_subject = 100  # Assuming maximum marks per subject is 100
    
    print(f"\nEnter marks for {num_subjects} subjects (out of {max_marks_per_subject}):")
    print("-" * 40)
    
    # Input marks for each subject
    for i in range(1, num_subjects + 1):
        while True:
            try:
                mark = float(input(f"Subject {i} marks: "))
                if 0 <= mark <= max_marks_per_subject:
                    marks.append(mark)
                    break
                else:
                    print(f"Marks should be between 0 and {max_marks_per_subject}!")
            except ValueError:
                print("Invalid input! Please enter a number.")
    
    # Calculate results
    total_marks = sum(marks)
    max_possible_marks = num_subjects * max_marks_per_subject
    percentage = (total_marks / max_possible_marks) * 100
    
    # Assign grade based on percentage
    if percentage >= 90:
        grade = "A+"
        remarks = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remarks = "Excellent"
    elif percentage >= 70:
        grade = "B+"
        remarks = "Very Good"
    elif percentage >= 60:
        grade = "B"
        remarks = "Good"
    elif percentage >= 50:
        grade = "C"
        remarks = "Average"
    elif percentage >= 40:
        grade = "D"
        remarks = "Pass"
    else:
        grade = "F"
        remarks = "Fail"
    
    # Display results
    print("\n" + "=" * 50)
    print("RESULT SHEET")
    print("=" * 50)
    
    print(f"\nNumber of Subjects: {num_subjects}")
    print(f"Maximum Marks per Subject: {max_marks_per_subject}")
    
    print("\nMarks Obtained:")
    for i, mark in enumerate(marks, 1):
        print(f"  Subject {i}: {mark:.2f}")
    
    print("\n" + "-" * 40)
    print(f"Total Marks: {total_marks:.2f} / {max_possible_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(f"Remarks: {remarks}")
    print("=" * 50)

# Run the program
if __name__ == "__main__":
    calculate_student_marks()