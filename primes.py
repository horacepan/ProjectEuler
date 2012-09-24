import math

# return all primes up to n
def populatePrimes( n ):
	primes = [2,3,5]
	if n < 2:
		return
	else:
		index = 1
		while (6*index + 1) <= n:
			upperBoundA = int(math.sqrt(6*index+1)) + 1
			upperBoundB = int(math.sqrt(6*index+1)) + 1
			isPrimeA = True
			isPrimeB = True
			for prime in primes:
				if prime > upperBoundA:
					break
				if (6*index+1) % prime == 0:
					isPrimeA = False
					break
			for prime in primes:
				if prime > upperBoundB:
					break
				if (6*index+5) % prime == 0:
					isPrimeB = False
					break
			if isPrimeA:
				primes.append(6*index+1)
			if isPrimeB:
				primes.append(6*index+5)
			index += 1
	return primes

# max = how high to populate, primes = list of all primes up to max
def primeFactorize( max, primes ):
	pFactorizations = {}
	for n in range(2, max + 1):
		if n in primes:
			pFactorizations[ n ] = { n: 1}
		for i in range(2, int(math.sqrt(n) + 1)):
			#print i, n
			#print pFactorizations
			if n%i == 0:
				factorization = pFactorizations[ n/i ].copy() # might not be correct?
				if i in factorization:
					factorization[ i ] = factorization[ i ] + 1
				else:
					factorization[ i ] = 1
				pFactorizations[ n ] = factorization
				break


#pFactorization = prime factorization dict, div = dict to populate
def getDivisors( pFactorization ):
	div = {}
	for k, v in pFactorization.iteritems():
		product = 1
		for a, b in v.iteritems():
			num = a**(b+1) - 1
			den = a-1
			product *= num/den
		div[ k ] = product - k

		

