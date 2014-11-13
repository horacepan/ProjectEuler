import time

def revNumbers(num):
	count = 0
	odds = set(['1','3','5','7','9'])
	for i in [ x for x in xrange(num) if x%10 != 0]:
		if len(str(i)) > len(str(
		r = i + int(str(i)[::-1])

		if r%2 != 1 or (r/10)%2 != 1: # or (r/100)%2 != 1:
			continue
		isRev = 1
		for c in str(r)[:-2]:
			if c not in odds:
				isRev = 0
				break
		count += isRev	
	return count

if __name__ == "__main__":
	start_time = time.time()
	print revNumbers(1000000)	
	print (time.time() - start_time), " seconds"

