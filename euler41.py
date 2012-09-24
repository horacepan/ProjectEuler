import itertools
import math
import primes

def run():
	pr = primes.populatePrimes( 3162 ) #3162 ~= sqrt of (10000000)
	def prime(n, primes):
		isPrime = True
		index = 0
		p = primes[index]
		limit = int(math.sqrt(n)) + 1
		while p < limit:
			if n % p == 0:
				isPrime = False
				break
			else:
				index += 1
				p = primes[ index ]
		return isPrime
	panPrimes = []
	for i in list(itertools.permutations('1234567')):
		s = ''
		for letter in i:
			s += letter
		num = int(s)
		if num%2 == 0:
			continue
		else:
			if prime(num, pr):
				panPrimes.append(num)
	return max(panPrimes)

print run()