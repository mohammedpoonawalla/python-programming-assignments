# Assignment No – 03
# Title: Sequences:- Types and Operators


assignments = ["Assignment 1", "Assignment 2", "Assignment 3"]
print("Initial list of assignments:")
print(assignments)
new_assignment = "Assignment 4"
assignments.append(new_assignment)
print(f"Added '{new_assignment}' to the list of assignments.")
completed_assignment = "Assignment 2"
if completed_assignment in assignments:
    assignments.remove(completed_assignment)
    print(f"Removed '{completed_assignment}' from the list of assignments (completed).")
else:
    print(f"'{completed_assignment}' is not found in the list of assignments.")

print("\nUpdated list of assignments:")
print(assignments)