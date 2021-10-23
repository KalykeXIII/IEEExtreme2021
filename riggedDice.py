# Task 6

tests = int(input())

for i in range(tests):
    rolls = int(input())
    
    alice_total = 0
    bob_total = 0
    
    alice = 0
    bob = 1
    
    dice = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    
    for j in range(rolls):
        values = list(input().split(' '))
        
        alice_roll = int(values[0])
        bob_roll = int(values[1])
        
        alice_total += alice_roll
        bob_total += bob_roll
        
        dice[alice][alice_roll - 1] += 1
        dice[bob][bob_roll - 1] += 1
        
        if alice_total != bob_total:
            alice = bob
            if bob == 1:
                bob = 0
            else:
                bob = 1
    if dice[0][5] > dice[1][5]:
        print(1)
    else:
        print(2)