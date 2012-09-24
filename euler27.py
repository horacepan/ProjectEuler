import primes

# find a*b for which n^2 + an + b generates the most consecutive primes
# b is a prime
primesB = primes.populatePrimes(1000)
primes = set(primes.populatePrimes(10000))

aList = [ n for n in range(-999, 1000) if n%2 != 0]
answers = {} #key = number of consec primes generated, val = a*b
for a in aList:
	for b in primesB:
		quad = lambda x: x**2 + a*x + b 
		composite = False
		num = 0
		while not composite:
			if quad(num) not in primes:
				composite = True
			else:
				num += 1
		#answers[a*b] = num
		answers[num] = (a, b)

print max(answers)
print answers[max(answers)]
		