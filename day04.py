#!/usr/bin/python

filename='../data/data-4.txt'
#filename='../data/google-4.txt'
#filename='../data/reddit-4.txt'
data = [[y.split('-') for y in x.split(',')] for x in open(filename).read().strip().split('\n')]

containedCount = 0
counter = 0
tempEven = []
tempOdd = []
for i in (data):
	for j in (i):
		id = ''
		for cnt in range(int(j[0]),int(j[1])+1):
			id+=str(cnt)
			if counter%2==0: #even
				tempEven.append(cnt)
			else:
				tempOdd.append(cnt)
		if counter%2==1: #odd, we have both values		
			#if all(map(lambda i: i in tempO, tempE)) or all(map(lambda i: i in tempEven, tempOdd)):
			if all(map(lambda i: i in tempOdd, tempEven)) or all(map(lambda i: i in tempEven, tempOdd)):
				containedCount += 1
			tempEven.clear()
			tempOdd.clear()
		counter+=1


print("part1:",containedCount)


containedCount = 0
counter = 0
tempEven = []
tempOdd = []
for i in (data):
	for j in (i):
		id = ''
		for cnt in range(int(j[0]),int(j[1])+1):
			id+=str(cnt)
			if counter%2==0: #even
				tempEven.append(cnt)
			else:
				tempOdd.append(cnt)
		if counter%2==1: #odd, we have both values		
			if any(map(lambda i: i in tempOdd, tempEven)) or any(map(lambda i: i in tempEven, tempOdd)):
				containedCount += 1
			tempEven.clear()
			tempOdd.clear()
		counter+=1

print("part2:",containedCount)


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