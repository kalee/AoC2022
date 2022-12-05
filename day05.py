#!/usr/bin/python

filename='../data/data-5.txt'
#filename='../data/google-5.txt'
#filename='../data/reddit-5.txt'

def setup():
	with open(filename) as file:
	    lines = file.readlines()
	    stack_temp = []

	    while(lines[0] != '\n'):
	        stack_temp.append(lines[0])
	        lines.pop(0)
	    
	    number = max([int(s) for s in stack_temp.pop(-1).split() if s.isdigit()])
	    stack = []
	    for i in range(number):
	        stack.append([])
	    
	    while(stack_temp):
	        line = stack_temp.pop(-1)
	        
	        k = 1
	        for i in range(number):
	            if(line[k] != ' '):
	                stack[i].append(line[k])
	            k += 4
	    moves = []
	    lines.pop(0)

	    for line in lines:
	        move_set = [int(s) for s in line.split() if s.isdigit()]
	        moves.append(move_set)
	return stack,moves
  
stack,moves = setup()  
for move in (moves):
	for i in range(move[0]):
		stack[move[2]-1].append(stack[move[1]-1].pop())

p1=[]
for item in (stack):
	p1.append(item.pop())

print("part1:","".join(p1))



stack,moves = setup()
for move in (moves):
	temp = []
	for i in range(move[0]):
		tmp = stack[move[1]-1].pop()
		temp.append(tmp[0])
	for i in range(len(temp)):
		stack[move[2]-1].append(temp.pop())
p2=[]
for item in (stack):
	p2.append(item.pop())
print("part2:","".join(p2))






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