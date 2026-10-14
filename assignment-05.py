# Assignment No – 05
# Problem Statement: A teacher wants to calculate the average grade of their students from multiple test scores.


num_students = int(input("Enter the number of students: "))
class_total = 0

# Loop through each student
for student in range(1, num_students + 1):
    print(f"\nEnter scores for Student {student}:")
    student_total = 0
    
    
    for test in range(1, 6):
        score = float(input(f"Enter score for Test {test}: "))
        student_total += score
        
    
    student_average = student_total / 5
    
   
    print(f"Average score of Student {student}: {student_average:.2f}")
    
    class_total += student_total

overall_average = class_total / (num_students * 5)

print(f"\nOverall average score of the class: {overall_average:.2f}")