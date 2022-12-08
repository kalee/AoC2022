#!/usr/bin/python

#filename='../data/data-8.txt'
filename='../data/google-8.txt'
#filename='../data/reddit-8.txt'
#rows = open(filename).read().strip().split('\n')
with open(filename) as file:
    rows = [line for line in file.read().strip().splitlines()]

# Load data into grid (dictionary structure grid(r,c)=val)
r=0
c=0
grid={}
maxlen = len(rows[0])
for row in (rows):
	for char in str(row).split()[0]:
		grid[r,c]=int(char)
		c += 1
		c %= maxlen
	r += 1

# Part 1
maxTD = -1
maxLR = -1
maxBU = -1
maxRL = -1
treeview = set()
for i in range(maxlen):
	maxTD = -1
	maxLR = -1
	for j in range(maxlen):
		# top down check
		if grid[i,j] > maxLR:
			maxLR = grid[i,j]
			treeview.add(tuple([i,j]))
		# left right check
		if grid[j,i] > maxTD:
			maxTD = grid[j,i]
			treeview.add(tuple([j,i]))
for i in range(maxlen-1,-1,-1):
	maxBU = -1
	maxRL = -1
	for j in range(maxlen-1,-1,-1):
		# right left check
		if grid[i,j] > maxRL:
			maxRL = grid[i,j]
			treeview.add(tuple([i,j]))
		# bottom up check
		if grid[j,i] > maxBU:
			maxBU = grid[j,i]
			treeview.add(tuple([j,i]))
print("part1:",len(treeview))


# Part2
treecnt = {}
for row in range(maxlen):
	for col in range(maxlen):
		# up 
		cntUp = 0
		for i in range(row,-1,-1):
			if i != row:
				if grid[i,col] < grid[row,col]:
					cntUp += 1
				elif grid[i,col] == grid[row,col]:	
					cntUp += 1
					break
				else:
					cntUp += 1
					break

		# down
		cntDown = 0
		for i in range(row,maxlen):
			if i != row:
				if grid[i,col] < grid[row,col]:
					cntDown += 1
				elif grid[i,col] == grid[row,col]:
					cntDown += 1
					break
				else:
					cntDown += 1
					break

		# left
		cntLeft = 0
		for i in range(col,-1,-1):
			if i != col:
				if grid[row,i] < grid[row,col]:
					cntLeft += 1
				elif grid[row,i] == grid[row,col]:
					cntLeft += 1
					break
				else:
					cntLeft += 1
					break

		# right
		cntRight = 0
		for i in range(col,maxlen):
			if i != col:
				if grid[row,i] < grid[row,col]:
					cntRight += 1
				elif grid[row,i] < grid[row,col]:
					cntRight += 1
					break
				else:
					cntRight += 1
					break

		treecnt[row,col] = cntUp * cntDown * cntLeft * cntRight

#print(treecnt)
print("Part2:", max(treecnt.values()))



#data = open(filename).read().strip().split('\n')

#data = [[y.split('-') for y in x.split(',')] for x in open(filename).read().strip().split('\n')]

#with open(filename) as file:
#    rows = [line for line in file.read().strip().splitlines()]



#with open('../data/google-1.txt', 'r') as f:
#    captcha = f.read()

#data = [x for x in open(filename).read().rstrip()]
#print(data)



#lst = [int(x) for x in open(filename).read().strip().split(',')]
#with open(filename) as file:
#	line =int(read().rstrip()) in file
#	print(line)
#	#while(line)


#lst = [int(x) for x in open(filename).read().rstrip()]
#print(lst)