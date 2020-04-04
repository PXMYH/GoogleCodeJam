#!/usr/bin/env python3

# Algorithm
# get the time elapsed since midnight as array, including start and end time
# sort the 1D array of arrays based on starting time
# assign the first shift to Jamie
# maintain two arrays for Jamie and Cameron's shift(s)
# loop through the rest activities
# if the next shift's starting time compare with J&C's end time:
# overlap with one, assign to the other
# overlap with both, return IMPOSSIBLE
# overlap with none, then randomly pick one, in this case, pick Jamie

def parenting_partner(M):
    # sort the array based on starting time
    # M.sort(key=lambda x: x[0])
    sorted_activities = sorted(M,key=lambda x: x[0])
    
    J, C, schedule = [[float('-inf'),float('-inf')]], [[float('-inf'),float('-inf')]], ''
    for activity in sorted_activities:
        # print("current activity = {}".format(activity))
        # print("current Jamie's schedule = {}, Cameron's schedule ={}".format(J, C))
        if activity[0] < J[-1][1] and activity[0] < C[-1][1]:
            # print("No one can take this activity, Jamie's schedule = {}, Cameron's schedule ={}".format(J, C))
            return "IMPOSSIBLE"
        
        elif activity[0] < J[-1][1]:
            # conflict with Jamie, Cameron takes the shift
            C.append(activity)
            # print("adding to Cameron, Cameron's schedule now = {}".format(C))
        elif activity[0] < C[-1][1]:
            # conflict with Cameron, Jamie takes the shift
            J.append(activity)
            # print("adding to Jamie, Jamie's schedule now = {}".format(J))
        else:
            C.append(activity)
            # print("adding to Jamie, Jamie's schedule now = {}".format(J))

    # return the schedule back to original order
    for activity in M:
        # print("activity now is {}".format(activity))
        if activity in J:
            schedule += "J"
            J.remove(activity)
        else:
            schedule += "C"
            C.remove(activity)

    return schedule

# driver code
# M = [[360,480],[420,540],[620,660]]
# M = [[0,1440],[1,3],[2,4]]
# M = [[99,150],[1,100],[100,301],[2,5],[150,250]]
# M = [[0,720],[720,1440]]
# M = [[0,150],[150,340],[1,3],[5,8],[100,152],[151,189]]
# M = [[0,720],[0,720]]
# M = [[0,720],[0,720],[450,890]]
# schedule = parenting_partner(M)
# print("Parenting shift = {}".format(schedule))

t = int(input()) # read a line with a single integer
for i in range(1, t + 1): # number of testcases
    # read in each time to form a testcase
    Matrix = []
    for s in range(int(input())):
        Matrix.append([int(s) for s in input().split()])
    print('Case #{}: {}'.format(i, parenting_partner(Matrix)))