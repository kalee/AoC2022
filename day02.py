#!/usr/bin/python
#10153 Guess 1, too low
#10633 Guess 2, too low
#11621 Guess 3, too low
#1309 Gues 4, right
#9865, too low
#10398, right

#filename='../data/data-2.txt'
#filename='../data/google-2.txt'
#filename='../data/reddit-2.txt'

data = [x.strip().split(' ') for x in open(filename).read().strip().split('\n')]
#print(len(data))
theirscore=0
myscore=0
myscore2=0
for e in (data):
	if e[0]=='A':   # Rock
		if e[1]=='X':  # Rock  # lose Scissors
			# tie
			myscore+=(1 + 3)
			myscore2+=(3 + 0)
		elif e[1]=='Y':  # Paper  # draw Rock
			# win
			myscore+=(2 + 6)
			myscore2+=(1 + 3)
		elif e[1]=='Z':  # Scissors  # win Paper
			# lose
			myscore+=(3 + 0)
			myscore2+=(2 + 6)

	elif e[0]=='B':    # Paper  
		if e[1]=='X':  # Rock  # lose Rock
			# lose
			myscore+=(1 + 0)
			myscore2+=(1 + 0)
		elif e[1]=='Y':  # Paper  # draw Paper
			# tie
			myscore+=(2 + 3)
			myscore2+=(2 + 3)
		elif e[1]=='Z':  # Scissors  #win Scissors
			# win
			myscore+=(3 + 6)
			myscore2+=(3 + 6)

	elif e[0]=='C':  # Scissors  
		if e[1]=='X':  # Rock  # lose Paper
			# win
			myscore+=(1 + 6)
			myscore2+=(2 + 0)
		elif e[1]=='Y':  # Paper # draw Scissors
			# lose
			myscore+=(2 + 0)
			myscore2+=(3 + 3)
		elif e[1]=='Z':  # Scissors  # win Rock
			# tie
			myscore+=(3 + 3)
			myscore2+=(1 + 6)

print("Part1:",myscore)
print("Part2:",myscore2)


# Another more simple way
#    matchups = {
#        'A': {'X': 1+3, 'Y': 2+6, 'Z': 3+0},
#        'B': {'X': 1+0, 'Y': 2+3, 'Z': 3+6},
#        'C': {'X': 1+6, 'Y': 2+0, 'Z': 3+3},
#    }
#    matchups2 = {
#        'A': {'X': 3+0, 'Y': 1+3, 'Z': 2+6},
#        'B': {'X': 1+0, 'Y': 2+3, 'Z': 3+6},
#        'C': {'X': 2+0, 'Y': 3+3, 'Z': 1+6},
#    }





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