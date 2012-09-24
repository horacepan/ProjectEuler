def run():
	def isPandigital( n ):
		digits = set(str(i) for i in range(1,10))
		isPan = True
		for letter in str(n):
			if letter not in digits:
				isPan = False
				break
			else:
				digits.remove( letter )
		return isPan
		
	def concat( num, n ):
		s = ''
		for i in range (1, n + 1):
			s += str(num*i)
		return int(s)

	maxPandigital = 0
	for n in range(25, 35):
		number = concat( n, 4 )
		if isPandigital(number):
			print "%d: %d" %( n, number )
			maxPandigital = max( maxPandigital, number )
	for n in range(334, 500):
		number = concat( n, 3 )
		if isPandigital(number):
			print "%d: %d" %( n, number )
			maxPandigital = max( maxPandigital, number )
	for n in range(5000, 9999):
		number = concat( n, 2 )
		if isPandigital(number):
			print "%d: %d" %( n, number )
			maxPandigital = max( maxPandigital, number )
	print maxPandigital
			
if __name__ == '__main__':
	run()
