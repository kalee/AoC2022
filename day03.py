#!/usr/bin/python

#filename='../data/data-3.txt'
#filename='../data/google-3.txt'
filename='../data/reddit-3.txt'
data = open(filename).read().strip().split('\n')

#a-z==1-26
#A-Z=27-52
#A=65
#a=97
def getValue(letter):
	val=ord(letter)
	if val>96:
		val=val-96
	else:
		val=val-64+26
	return val



part1 = []
part2 = []
part2temp = []
for item in (data):
	temp1 = item[0:len(item)//2]
	temp2 = item[len(item)//2:]
	temp3=list(set(temp1)&set(temp2))
	part1.append(temp3)

sum = 0
for item in (part1):
	sum+=getValue(item[0])


print("part1:", sum)

for item in (data):
	part2temp.append(item)
	if len(part2temp)==3:
		temp=list(set(part2temp[0])&set(part2temp[1])&set(part2temp[2]))
		#print(part2temp, temp)
		part2.append(temp)
		part2temp.clear()

sum=0
for item in (part2):
	sum+=getValue(item[0])

print("part2:", sum)


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