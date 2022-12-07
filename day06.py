#!/usr/bin/python


def TuningTrouble(count):
	#filename='../data/data-6.txt'
	filename='../data/google-6.txt'
	#filename='../data/reddit-6.txt'
	data = read_file(filename)

	for i in range(count,len(data)):
		dataset = data[i-count:i]
		if len(set(dataset)) == count:
			return i


def main():
	print("part1:",TuningTrouble(4))
	print("part2:",TuningTrouble(14))



###
## UTIL
#
def read_file(filename):
	with open(filename, encoding='utf-8') as file:
		#return file.readlines()
		return file.read().strip().split('\n')[0]


if __name__ == '__main__':
	main()






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