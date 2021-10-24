# Task 11

class Node:
    def __init__(self, key, parent, children):
        return None
        
tests = int(input())

for i in range(tests):
    case_info = list(input().split(' '))
    red, blue, events = int(case_info[0]), int(case_info[1]), int(case_info[2])
    # Construct the red tree
    red_hierarchy = list(input().split(' '))
    root = red_hierarchy[0]
    # Construct the blue tree
    blue_hierarchy = list(input().split(' '))
    root = blue_hierarchy[0]
    
    
        