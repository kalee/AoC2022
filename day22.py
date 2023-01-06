#!/usr/bin/python
#
from collections import defaultdict, deque
import re


#######################################
# Check next value based on direction.  If valid, return it, else return original.  May loop back around to
# to continue check. If next available space is valid, and return it, else return original.
#######################################
def check_next_part1(R,C,D):
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    calc = direction[D]
    rNew = R+calc[0]
    cNew = C+calc[1]
    dNew = D

    # Col changes.
    if D==0 or D==2:
        if cNew < 0: # Case Col < 0
            for col in range(maxC-1,-1,-1):
                if grid[R][col] == '#':
                    return R,C,D
                elif grid[R][col] == '.':
                    return R, col, D
        elif cNew >= maxC:
            for col in range(maxC):
                if grid[rNew][col] == '#':
                    return R,C,D
                elif grid[rNew][col] == '.':
                    return rNew, col, D
        else:  # valid range, so standard checks.  If blank, must loop.
            if grid[R][cNew] == '#':
                return R,C,D
            elif grid[R][cNew] == '.':
                return R,cNew,D
            elif D==0:
                for col in range(maxC):
                    if grid[rNew][col] == '#':
                        return R,C,D
                    elif grid[rNew][col] == '.':
                        return rNew, col, D
            elif D==2:
                for col in range(maxC-1,-1,-1):
                    if grid[R][col] == '#':
                        return R,C,D
                    elif grid[R][col] == '.':
                        return R, col, D
    elif D==1 or D==3:  # Row Changes
        if rNew < 0:
            for row in range(maxR-1,-1,-1):
                if grid[row][C] == '#':
                    return R,C,D
                elif grid[row][C] == '.':
                    return row, C, D
        elif rNew >= maxR:
            for row in range(maxR):
                if grid[row][C] == '#':
                    return R,C,D
                elif grid[row][C] == '.':
                    return row, C, D
        else:  # valid range, so standard checks.  If blank, must loop.
            if grid[rNew][C] == '#':
                return R,C,D
            elif grid[rNew][C] == '.':
                return rNew,C,D
            elif D==1:
                for row in range(maxR):
                    if grid[row][C] == '#':
                        return R,C,D
                    elif grid[row][C] == '.':
                        return row, C, D
            elif D==3:
                for row in range(maxR-1,-1,-1):
                    if grid[row][C] == '#':
                        return R,C,D
                    elif grid[row][C] == '.':
                        return row, C, D
    assert False, "Didn't find a value that would work"


#######################################
# get_region
# r1 0,100   to  49,149   r:0-49    c:100-149
# r2 50,0    to  99,49    r:50-99   c:0-49
# r3 50,50   to  99,99    r:50-99   c:50-99
# r4 50,100  to  99,149   r:50-99   c:100-149
# r5 100,100 to  149,149  r:100-149 c:100-149
# r6 100,150 to  149,199  r:100-149 c:150-199
#
#######################################
def get_region(R,C):
    if R >= 0 and R <= 49 and C >= 50 and C <= 99:
        return 1
    elif R >= 0 and R <= 49 and C >= 100 and C <= 149:
        return 2
    elif R >= 50 and R <= 99 and C >= 50 and C <= 99:
        return 3
    elif R >= 100 and R <= 149 and C >= 0 and C <= 49:
        return 4
    elif R >= 100 and R <= 149 and C >= 50 and C <= 99:
        return 5
    elif R >= 150 and R <= 199 and C >= 0 and C <= 49:
        return 6
    else:
        return 0


#######################################
# check_next_part2(R,C,D)
# Use cube.  Map and change direction for each face that falls off.  Keep it simple!
# D can be 0->R,1->D,2->L,3->U
#######################################
def check_next_part2(R,C,D):
    #            0->R  1->D  2->L   3->U
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    calc = direction[D]
    rNew = R+calc[0]
    cNew = C+calc[1]
    dNew = D
    # Hardcode for problem.
    # 1. 6 regions.  Each region is a 50x50 cube.
    if get_region(rNew,cNew) != 0:
        if grid[rNew][cNew]=='.':
            return rNew, cNew, dNew
        elif grid[rNew][cNew]=='#':
            return R,C,D
        else:
            assert False, "what other characters are on the screen?"

    # Which region are we in?
    #print("region:",get_region(R,C),"region:",get_region(rNew,cNew))

    # need to find the new position with cube coordinates HC VR
    # D can be 0->R, 1->D, 2->L, 3->U
    if get_region(R,C)==1 and cNew<50: # get_region(rNew,cNew)==4:  # left vert to left vert.  49:0 and 100:149
        rNew = 149-R
        cNew = 0
        dNew = 0
    elif get_region(R,C)==1 and rNew<0: # get_region(rNew,cNew)==6:  # top horiz to left vert.  50:99 to 150:199
        rNew = C+100
        cNew = 0
        dNew = 0
    elif get_region(R,C)==2 and rNew>49: # get_region(rNew,cNew)==3:  # Bot horiz to right vert.  100:199 to 50-99
        rNew = C-50
        cNew = 99
        dNew = 2
    elif get_region(R,C)==2 and cNew>149: # get_region(rNew,cNew)==5:  # right vert to right vert.  49:0 to 100-149
        rNew = 149-R
        cNew = 99
        dNew = 2
    elif get_region(R,C)==2 and rNew<0: # get_region(rNew,cNew)==6:  # top horiz to bot horiz.  100:149 to 0-49
        rNew = 199
        cNew = C-100
        dNew = 3
    elif get_region(R,C)==3 and cNew>99: # get_region(rNew,cNew)==2:  # right vert to bot horiz.  50:99 to 100-149
        rNew = 49
        cNew = R+50
        dNew = 3
    elif get_region(R,C)==3 and cNew<50: # get_region(rNew,cNew)==4:  # left vert to top horiz.  50:99 to 0:49
        rNew = 100
        cNew = R-50
        dNew = 1
    elif get_region(R,C)==4 and rNew<100: # get_region(rNew,cNew)==3:  # top horiz to left vert.  0:49 to 50:99
        rNew = C+50
        cNew = 50
        dNew = 0
    elif get_region(R,C)==4 and cNew<0: # get_region(rNew,cNew)==1:  # left vert to left vert. 100:149 to 49:0
        rNew = 149-R
        cNew = 50
        dNew = 0
    elif get_region(R,C)==5 and cNew>99: # get_region(rNew,cNew)==2:  # right vert to right vert.  100:149 to 49:0
        rNew = 149-R
        cNew = 149
        dNew = 2
    elif get_region(R,C)==5 and rNew>149: # get_region(rNew,cNew)==6:  # bot horiz to right vert.  50:100 to 150:199
        rNew = C+100
        cNew = 49
        dNew = 2
    elif get_region(R,C)==6 and cNew>49: # get_region(rNew,cNew)==5:  # right vert to bott horiz.  150:199 to 50:99
        rNew = 149
        cNew = R-100
        dNew = 3
    elif get_region(R,C)==6 and rNew>199: # get_region(rNew,cNew)==2:  # top horiz to bot horiz.  0:49 to 100:149
        rNew = 0
        cNew = C+100
        dNew = 1
    elif get_region(R,C)==6 and cNew<0: # get_region(rNew,cNew)==1:  # left vert to top horiz.  150:199 to 50-99
        rNew = 0
        cNew = R-100
        dNew = 1
    else:
        print("old: ", R,C,get_region(R,C), " new: ",rNew,cNew, get_region(rNew,cNew))
        assert False, "Never should happen."

    #print("old: ", R,C,get_region(R,C), " new: ",rNew,cNew, get_region(rNew,cNew))
    if get_region(rNew,cNew) != 0 and grid[rNew][cNew]=='.':
        return rNew, cNew, dNew
    else:
        #print("old: ", R,C,get_region(R,C), " new: ",rNew,cNew, get_region(rNew,cNew))
        return R,C,D


#######################################
# Find first spot that can be moved.
# On the first row find the first "."
#######################################
def find_first(R,C,D):
    for i,c in enumerate(grid[0]):
        if c=='.':
            C=i
            break
    return 0,C,0


#######################################
# part1
#
#######################################
def part1():
    # Setup default values to use.
    # D can be 0->R,1->D,2->L,3->U
    R = 0
    C = 0
    D = 0 # facing right

    # find first value
    R,C,D = find_first(R,C,D)

    #follow the directions
    while len(instr)>0:
        cnt=instr.pop(0)
        dir=None
        if len(instr)>0:
            dir=instr.pop(0)
        else:
            dir=' '

        cnt = int(cnt)
        for counter in range(cnt):
            R,C,D = check_next_part1(R,C,D)

        # Change direction.  Don't change direction if there isn't one.
        if dir=='R':
            D=(D+1)%4
        elif dir=='L':
            D=(D+4-1)%4

    print("part1:",(1000*(R+1) + 4*(C+1) + D))


#######################################
# part2
#
#######################################
def part2():
    # Setup default values to use.
    # D can be 0->R,1->D,2->L,3->U
    R = 0
    C = 0
    D = 0 # facing right

    # find first value
    R,C,D = find_first(R,C,D)
    #print("R:",R," C:",C," D:",D)

    #follow the directions
    while len(instr)>0:
        cnt=instr.pop(0)
        dir=None
        if len(instr)>0:
            dir=instr.pop(0)
        else:
            dir=' '

        cnt = int(cnt)
        for counter in range(cnt):
            assert grid[R][C]=='.'
            R1,C1,D1 = check_next_part2(R,C,D)
            if R1==R and C1==C and D1==D:
                R=R1
                C=C1
                D=D1
                continue
            else:
                R=R1
                C=C1
                D=D1

            #R,C,D = check_next_part2(R,C,D)
        #print("R:",R," C:",C," D:",D)

        # Change direction.  Don't change direction if there isn't one.
        if dir=='R':
            D=(D+1)%4
        elif dir=='L':
            D=(D+4-1)%4
        #print("R:",R," C:",C," D:",D)

    # 125321
    # 129321
    # 12462 - Correct answer
    print("part2:",(1000*(R+1) + 4*(C+1) + D))

#######################################
# main program starts here.
#
#######################################
#filename='../data/data-22.txt'
filename='../data/google-22.txt'
#filename='../data/reddit-22.txt'


data = open(filename).read()
grid, ins = data.split("\n\n")

# Parse grid into list
grid = grid.split("\n")

# Put directions into a list: [(#,d), ...]
ins=ins.strip()
#instr = re.findall(r'(\d+)(\w*?)',ins)
instr = re.findall( "L|R|\d+", ins )

maxR = 0 # len(grid)
maxC = 0 # len(grid[0])
for row in grid:
    maxR += 1
    if len(row) > maxC:
        maxC = len(row)

# make each row the same length.
for i in range(maxR):
    if len(grid[i]) < maxC:
        grid[i] += ' ' * (maxC-len(grid[i]))

part1()

grid, ins = data.split("\n\n")

# Parse grid into list
grid = grid.split("\n")

# Put directions into a list: [(#,d), ...]
ins=ins.strip()
#instr = re.findall(r'(\d+)(\w*?)',ins)
instr = re.findall( "L|R|\d+", ins )

maxR = 0 # len(grid)
maxC = 0 # len(grid[0])
for row in grid:
    maxR += 1
    if len(row) > maxC:
        maxC = len(row)

# make each row the same length.
for i in range(maxR):
    if len(grid[i]) < maxC:
        grid[i] += ' ' * (maxC-len(grid[i]))

part2()

