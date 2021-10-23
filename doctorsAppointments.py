if __name__ == "__main__":
    # Number of test cases
    test_cases = int(input())
    # Iterate through each of the test cases
    for i in range(test_cases):
        # Get the number of patients in the case
        noPatients = int(input())
        # Iterate through each patient
        # Create an array to store the intervals available
        intervals = []
        for j in range(noPatients):
            patient = input().split(" ")
            intervals.append((int(patient[0]), int(patient[1]), j + 1))
            
        # Sort the intervals by start date
        intervals_sorted = sorted(intervals, key=lambda x: (x[1] - x[0], x[0]))
        
        # Create placeholder arrays for the occupied days and what day each patient is on
        occupied = []
        schedule = noPatients * [0]
        for interval in intervals_sorted:
            for j in range(interval[0], interval[1] + 1):
                if j not in occupied:
                    occupied.append(j)
                    schedule[interval[2]-1] = j
                    break
        if len(occupied) == noPatients:
            print(' '.join(str(i) for i in schedule))
        else:
            print('impossible')
            