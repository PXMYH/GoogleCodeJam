#!/usr/bin/env python3

# Algorithm

def patternMatching(patterns):
    max_index, max_length, sanitized_pattern = 0, 0, []
    for index, pattern in enumerate(patterns):
        pattern = pattern.strip('*')
        sanitized_pattern.append(pattern.strip('*'))
        if len(pattern) > max_length:
            max_index, max_length = index, len(pattern)

    base_pattern = sanitized_pattern[max_index]
    print(f"sanitized pattern = {sanitized_pattern}")
    print(f"base_pattern = {base_pattern}")
    for pattern in sanitized_pattern:
        if not base_pattern.endswith(pattern):
            return '*'

    
    # all patterns are in base pattern
    return base_pattern


# driver code
# patterns = ['*CONUTS', '*COCONUTS', '*OCONUTS', '*CONUTS', '*S']
# res = patternMatching(patterns)
# print("res = {}".format(res))

t = int(input()) # read a line with a single integer
for i in range(1, t + 1): # number of testcases
    # read in each time to form a testcase
    patterns, lines = [], int(input())
    for line in range(lines):
        patterns.append(input().strip())
        
    print('Case #{}: {}'.format(i, patternMatching(patterns)))