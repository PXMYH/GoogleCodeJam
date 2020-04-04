#!/usr/bin/env python3

class Solution:
    def __init__(self):
        self.trace = 0
        self.row = 0
        self.col = 0

    def vestigium(self, M):
        # compute trace
        R, C = len(M), len(M[0])

        for r in range(0,R):
            self.trace += M[r][r]

        # check if there's duplication in rows
        for r in M:
            if len(set(r)) != len(r):
                self.row += 1

        # check if there's duplication in columns
        for c in range(0, C):
            column = [sub[c] for sub in M]
            if len(set(column)) != len(column):
                self.col += 1
    
    def getTrace(self):
        return self.trace
    
    def get_dup_row(self):
        print(f"number of duplicated row= {self.row}")
        return self.row

    def get_dup_col(self):
        print(f"number of duplicated column = {self.col}")
        return self.col

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
M1 = [[1,2,3,4],[2,1,4,3],[3,4,1,2],[4,3,2,1]]
print(f"M1 = {M1}")
s = Solution()
s.vestigium(M1)
s.getTrace()
s.get_dup_row()
s.get_dup_col()

# testcase #2
M2 = [[2,2,2,2],[2,3,2,3],[2,2,2,3],[2,2,2,2]]
print(f"M2 = {M2}")
s = Solution()
s.vestigium(M2)
s.getTrace()
s.get_dup_row()
s.get_dup_col()

# testcase #3
M3 = [[2,1,3],[1,3,2],[1,2,3]]
print(f"M2 = {M3}")
s = Solution()
s.vestigium(M3)
s.getTrace()
s.get_dup_row()
s.get_dup_col()

# input() reads a string with a line of input, stripping the ' ' (newline) at the end
# This is all you need for most Code Jam problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1): # number of testcases
    tc_lines = input()
    # read in each time to form a testcase
    Matrix = []
    for s in range(int(tc_lines)):
        Matrix.append([int(s) for s in input().split(" ")]) # matrix row
    s = Solution()
    s.vestigium(Matrix)
    print(f"Case #{i}: {s.getTrace()} {s.get_dup_row()} {s.get_dup_col()}")