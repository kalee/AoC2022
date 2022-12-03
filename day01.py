#!/usr/bin/python

filename='../data/data-1.txt'
#filename='../data/google-1.txt'
#filename='../data/reddit-1.txt'

with open(filename) as file:
    rows = [line for line in file.read().strip().splitlines()]


lst=[]
count=0
maxcount=0
for i in (rows):
	
	if i != '':
		#print(count,i)
		count += int(i)
	elif i == '':
		if count>maxcount:
			maxcount = count
		lst.append(count)
		count = 0

if count>0:
	lst.append(count)

print("part1:",maxcount)
#lst.sort(reverse=True)
print("part2:",lst[:-1]+lst[:-2]+lst[:-3])

print(rows)
print(lst)


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