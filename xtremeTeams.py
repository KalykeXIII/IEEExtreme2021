# Task 3

from itertools import combinations

# Binary Calculator
def binary_calc(l, result):
    # l = list of binary values to be summed
        
    for binary in l:
        if None not in result:
            break
        for j in range(len(binary)):
            if binary[j] == 'y':
                result[j] = 1

    return result
                
# Number of test cases
no_tests = int(float(input()))

# Place tests info into a list
data = []
for i in range(no_tests):
    temp = input().split(" ")
    
    # Number of students
    no_students = temp[0]
    no_students = int(no_students)
    
    # Number of Specialities
    no_spec = temp[1]
    no_spec = int(no_spec)
    
    # Students
    students = []
    for j in range(no_students):
        student = input()
        students.append(student)
        
    # Append all test info to test data
    data.append([no_students, no_spec, students])
    
for test in data:
    total = 0
    for comb in combinations(test[2], 3):
        result = [None] * test[1]
        new_result = binary_calc(comb, result)
        
        if None in new_result:
            pass
        else:
            total += 1
            
    print(total)
        