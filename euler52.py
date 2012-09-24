#only need to check numbers divis by 3

def run():
	def checkDigits( digits, input):
		inputSet = set(int(i) for i in str(input))
		if len(inputSet) != len(digits):
			return False
		if sum(digits) != sum(inputSet):
			return False
		else:
			return digits == inputSet

# get the next possible candidate		
	def next( n ):
		if len(str(6*n)) != len(str(6*n+18)):
			n = 10**len(str(n)) + 2
		else:
			n += 3
		return n

	found = False
	n = 102 # start point
	while not found:
		digits = set(int(i) for i in str(n))
		multiples = [2*n, 3*n, 4*n, 5*n, 6*n]
		same = reduce( lambda x, y: x and y, map(lambda x: checkDigits(digits, x), multiples))
		if same:
			found = True
		else:
			#increase n
			n = next(n)
	print 'The answer is %d' %n
	
if __name__ == '__main__':
	run()