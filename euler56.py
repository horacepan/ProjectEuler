
def run():
	m = 0
	def digitalSum( base, exp ):
		n = base ** exp
		sum = 0
		for l in str(n):
			if l != 'L':
				sum += int(l)
		return sum
	
	for a in range(90, 100):
		for b in range(90, 100):
			m = max(m, digitalSum(a, b))
	print m
	
if __name__ == '__main__':
	run()
