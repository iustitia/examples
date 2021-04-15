"""
Input:
2

5
1 2 3 4 5

2
-100 100

Output:
15
0
"""

n = int(input())
sum_list = []

for i in range(n):
    x = int(input())

    # 1. case
    l = input().split()
    l = [int(a) for a in l]
    print(l)

    # 2. case
    l2 = []
    for j in range(x):
        l2.append(int(input()))

    print(l2)

    sum_list.append(sum(l2))

print(sum_list)
