#!/usr/bin/env python3

# Algorithm

def pascalWalk(N):
    res = ''
    if N <= 501:
        for i in range(N-5):
            res += '{} {}\n'.format(i+4, i+4)

    # if N > 501:
    #     total_sum = 0
    #     for row in range(1,N):
    #         if total_sum()
    #         break
    
    return res.rstrip('\n')

class Node():
    def __init__(self):
        self.left_up = Node(float('-inf'))
        self.left = Node(float('-inf'))
        self.right = Node(float(-inf))
        self.right_up = Node(float(-inf))
        self.left_down =  Node(float(-inf))
        self.right_down = Node(float(-inf))

    def assign_val(self, row, column):
        self.val = Node(row - 1, column -1) + Node(row -1, column)

# def dfs()

# driver code
# N = 100
# res = pascalWalk(N)
# print("res = {}".format(res))

t = int(input()) # read a line with a single integer
for i in range(1, t + 1): # number of testcases
    # read in each time to form a testcase
    N = int(input().strip())
    print('Case #{}:\n{}'.format(i, pascalWalk(N)))