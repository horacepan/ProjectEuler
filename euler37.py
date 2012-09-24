import primes

def run():
	p = primes.populatePrimes(1000000)
	pSet = set(p)
	# returns true if first digit is 2, 3 or 7
	def firstDigit( n ):
		first = int(str(n)[0])
		return first == 2 or first == 3 or first == 7 or first == 5

	# returns true if last digit is 3 or 7
	def lastDigit( n ):
		return n%10 == 3 or n%10 == 7
		
	# return true if its prime for all "right truncations"
	def rightPrime( n ):
		if n/10 == 0 and n in pSet:
			return True
		else:
			trunc = n/10
			return trunc in pSet and rightPrime(trunc)

	# return true if its prime for all "left truncations"
	def leftPrime( n ):
		if n/10 == 0 and n in pSet:
			return True
		else:
			trunc = int(str(n)[1:])
			return trunc in pSet and leftPrime(trunc)
	
	count = 0
	answers = []
	exempt = set([2,3,5,7])
	for p in pSet:
		if not firstDigit(p) and not lastDigit(p):
			continue
		else:
			if rightPrime(p) and leftPrime(p) and p not in exempt:
				count += 1
				answers.append(p)
	print answers
	print sum(answers)

	
if __name__ == '__main__':
	run()
			