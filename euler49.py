import primes

p4 = [ p for p in primes.populatePrimes(10000) if p/1000 > 1 ]

map = {}

for p in p4:
	key = list(str(p))
	key.sort()
	dkey = reduce(lambda x, y: x + y, key)
	if dkey in map:
		map[dkey].append(p)
	else:
		map[dkey] = [p]
		
count = 0
for k, v in map.iteritems():
	v.sort()
	
for k,v in map.iteritems():
	if len(v) >= 3:
		if len(v) == 3:
			if 2*v[1] == v[0] + v[2]:
				print "THE ANSWER!!!!!!!!!!!!!! is %d, %d, %d" %(v[0], v[1], v[2])
		else:
			found = False
			s = {}
			for p1 in v:
				for p2 in v:	
					if p1-p2 in s and p1 != p2 and p1 == s[p1-p2][1]:
						print "%d, %d. And %d, %d" %(s[p1-p2][0], s[p1-p2][1], p1, p2)
					else:
						s[p1-p2] = (p1,p2)
	