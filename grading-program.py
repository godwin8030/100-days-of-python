student_scores={
    "Sam": 89,
    "Prince":78,
    "Sofia": 69,
    "Tyler": 49
}

student_grades={}

for key,values in student_scores.items():
    if values >=91 and values<=100:
        student_grades[key] = "Outstanding"
    elif values >=81 and values<=90:
        student_grades[key] = "Exceeds Expectations"
    elif values >=71 and values<=80:
        student_grades[key] = "Exceeds Expectations"
    else:
        student_grades[key] = "Fail"

print(student_grades)