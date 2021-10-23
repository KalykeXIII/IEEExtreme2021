# Task 7

inputs = list(input().split(' '))
p, q, n, m = int(inputs[0]), int(inputs[1]), int(inputs[2]), int(inputs[3])

sn = 0
for k in range(1, n + 1):
    sn += ((pow(p % m, k, m) % m * pow(k % m, q, m) % m))
    sn = sn % m

sn = int(sn)
print(sn)
