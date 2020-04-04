#!/usr/bin/env python3

import collections

# Algorithm
# read the digit one by one
# if digit is 0, do nothing, just push the digit directly to queue
# if current digit is smaller than previous digit, start pushing (Di+1 - Di) closing parenthesis to queue, then push the current digit
# if current digit is equal to previous digit, do nothing , just push the current digit
# if current digit is larger than previous digit, push (Di - Di+1) opening parenthesis, then push the current digit
# if reaching the end of digits and no more digits to be pushed, push the remaining closing parenthesis

# so we'll need the following:
# a queue to hold the list so we can print the final result
# a close bracket count
# a open bracket count
# a pointer to know current value
# a pointer to know previous value

# nums: List
def nestingPair(nums):
    nesting_pair_queue = collections.deque()
    pre_digit, current_digit, open_cnt, close_cnt = float('-inf'), float('-inf'), 0, 0
    for index, num in enumerate(nums):
        current_digit = num

        if current_digit == pre_digit:
            nesting_pair_queue.append(str(current_digit))
        
        if current_digit > pre_digit:
            if open_cnt == 0:
                open_cnt = current_digit
                nesting_pair_queue.append(open_cnt*'(')
            else:
                nesting_pair_queue.append((current_digit-(open_cnt - close_cnt)) * '(')
                open_cnt = current_digit
            
            nesting_pair_queue.append(str(current_digit))

        if current_digit < pre_digit:
            close_cnt = pre_digit - current_digit
            nesting_pair_queue.append(close_cnt * ')')
            open_cnt -= close_cnt
            close_cnt = 0
            nesting_pair_queue.append(str(current_digit))

        pre_digit = current_digit
        if (index + 1 >= len(nums)):
            nesting_pair_queue.append((open_cnt - close_cnt)*')')
    
    return ''.join(nesting_pair_queue)

# driver code
# nums = [3,1,2]
# nums = [0,2,1]
# nums = [4]
# nums = [0,0,0,0]
# nums = [2,2,1]
# nums = [1,0,1]
# nums = [4,0,1,5]
nums = [4,1,2,0,1,5]
pair = nestingPair(nums)
print("nesting string = {}".format(pair))

# t = int(input()) # read a line with a single integer
# for i in range(1, t + 1): # number of testcases
#     # read in each time to form a testcase
#     nums = [int(s) for s in str(input().strip())]
#     print('Case #{}: {}'.format(i, nestingPair(nums)))