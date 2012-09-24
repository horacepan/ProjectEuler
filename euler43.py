import itertools

def run():
	def c1( n ):
		num = int(n[1] + n[2] + n[3])
		return num % 2 == 0

	def c2( n ):
		num = int(n[2] + n[3] + n[4])
		return num % 3 == 0

	def c3( n ):
		num = int(n[3] + n[4] + n[5])
		return num % 5 == 0

	def c4( n ):
		num = int(n[4] + n[5] + n[6])
		return num % 7 == 0

	def c5( n ):
		num = int(n[5] + n[6] + n[7])
		return num % 11 == 0

	def c6( n ):
		num = int(n[6] + n[7] + n[8])
		return num % 13 == 0

	def c7( n ):
		num = int(n[7] + n[8] + n[9])
		return num % 17 == 0		
	
	def sat( n ):
		return c1(n) and c2(n) and c3(n) and c4(n) and c5(n) and c6(n) and c7(n)
		
	permutations = list(itertools.permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']))
	permutations = [i for i in permutations if i[0] != '0' and sat(i)]
	
	print permutations
	sum = 0
	for p in permutations:
		sum += int(reduce( lambda x, y: x+y, p))
	print sum
	
if __name__ == '__main__':
	run()
	