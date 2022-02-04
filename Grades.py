def average_grades(grades):
    length = len(grades)
    total_grades = sum(grades)
    average = round(total_grades / length)
    return average

def grade_letter(average):
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

grades = []
for i in range(3):
    score = int(input("Enter grade numbers: "))
    grades.append(score)

average = average_grades(grades)
letter = grade_letter(average)

print("Your average is" , average)
print("Your letter grade is" , letter)
print("This is an edit")

