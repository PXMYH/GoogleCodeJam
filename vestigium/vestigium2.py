#!/usr/bin/env python3

def vestigium(M):
    trace, row, col = 0, 0, 0

    # compute trace
    R, C = len(M), len(M[0])

    for r in range(0,R):
        trace += M[r][r]

    # check if there's duplication in rows
    for r in M:
        if len(set(r)) != len(r):
            row += 1

    # check if there's duplication in columns
    for c in range(0, C):
        column = [sub[c] for sub in M]
        if len(set(column)) != len(column):
            col += 1

    return trace, row, col

# input
# 3
# 4
# 1 2 3 4
# 2 1 4 3
# 3 4 1 2
# 4 3 2 1
# 4
# 2 2 2 2
# 2 3 2 3
# 2 2 2 3
# 2 2 2 2
# 3
# 2 1 3
# 1 3 2
# 1 2 3

# output
# Case #1: 4 0 0
# Case #2: 9 4 4
# Case #3: 8 0 2


# driver code
# testcase #1
# M1 = [[1,2,3,4],[2,1,4,3],[3,4,1,2],[4,3,2,1]]
# print(f"M1 = {M1}")
# trace1, row1, col1 = vestigium(M1)
# print(f"trace={trace1}, row={row1}, col={col1}")

# # testcase #2
# M2 = [[2,2,2,2],[2,3,2,3],[2,2,2,3],[2,2,2,2]]
# print(f"M2 = {M2}")
# trace2, row2, col2 = vestigium(M2)
# print(f"trace={trace2}, row={row2}, col={col2}")

# # testcase #3
# M3 = [[2,1,3],[1,3,2],[1,2,3]]
# print(f"M2 = {M3}")
# trace3, row3, col3 = vestigium(M3)
# print(f"trace={trace3}, row={row3}, col={col3}")

# input() reads a string with a line of input, stripping the ' ' (newline) at the end
# This is all you need for most Code Jam problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1): # number of testcases
    # read in each time to form a testcase
    Matrix = []
    for s in range(int(input())):
        Matrix.append([int(s) for s in input().split()]) # matrix row
    trace, row, col = vestigium(Matrix)
    # print(f"Case #{i}: {s.getTrace()} {s.get_dup_row()} {s.get_dup_col()}")
    print('Case #{}: {} {} {}'.format(i, trace, row, col)) # MUST use this format!!! Don't know why, tested in GCP's VM on Python 3.5.3 which is the code platform code jam is using
