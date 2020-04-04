#!/usr/bin/env python3

def parenting_partner(M):
    pass

t = int(input()) # read a line with a single integer
for i in range(1, t + 1): # number of testcases
    # read in each time to form a testcase
    Matrix = []
    for s in range(int(input())):
        Matrix.append([int(s) for s in input().split()]) # matrix row
    trace, row, col = vestigium(Matrix)
    # print(f"Case #{i}: {s.getTrace()} {s.get_dup_row()} {s.get_dup_col()}")
    print('Case #{}: {} {} {}'.format(i, trace, row, col)) # MUST use this format!!! Don't know why, tested in GCP's VM on Python 3.5.3 which is the code platform code jam is using
