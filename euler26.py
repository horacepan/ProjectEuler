import primes

p = primes.populatePrimes(1000)[3:]
max = (0, 0)
for prime in p:
	count = 1
	divis = False
	while not divis:
		#print "We are on prime %d and count %d" %(prime, count)
		if ((10**count - 1) % prime) == 0:
			divis = True
		else:
			count += 1
	if count > max[1]:
		max = (prime, count)
		
print max
