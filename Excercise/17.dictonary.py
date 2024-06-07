
# declaration of dict type of data, which is similar to object in js

dictionary = {"one":'One number', "two":'Two number', 'three':'Three Number'}
# can be accessed with the keys
print(dictionary['one'])

# Updating the data inside the dict,  same can be followed to add 
dictionary['one'] = 'This is updated one'

# resetting the complete dict
dictionary ={}



# Score maker
student_scores = { "Harry": 81, "Ron": 78, "Hermione": 99, "Draco": 74, "Neville": 62 }

student_grades = {}

for key in student_scores :
    if student_scores[key] > 90 :
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80 :
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70 :
        student_grades[key] = "Acceptable"
    else :
        student_grades[key] = "Fail"

print(student_grades)
