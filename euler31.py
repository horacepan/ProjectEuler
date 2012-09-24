def val(a = 0, b = 0, c = 0, d = 0, e = 0, f = 0, g = 0, h = 0):
	sum = (200*a + 100*b +50*c + 20*d + 10*e + 5*f + 2*g + h)
	return sum

count = 0
for a in range(0, 2):
	if val(a) > 200:
		continue
	if val(a) == 200:
		count += 1
		continue
	for b in range(0, 3):
		if val(a, b) > 200:
			continue
		if val(a,b) == 200:
			count += 1
			continue
		for c in range(0, 5):
			if val(a,b,c) > 200:
				continue
			if val(a,b,c) == 200:
				count += 1
				continue
			for d in range(0, 11):
				if val(a,b,c,d) >200:
					continue
				if val(a,b,c,d) == 200:
					count +=1
					continue
				for e in range(0, 21):
					if val(a,b,c,d,e) > 200:
						continue
					if val(a,b,c,d,e) == 200:
						count +=1
						continue
					for f in range(0, 41):
						if val(a,b,c,d,e,f) > 200:
							continue
						if val(a,b,c,d,e,f) == 200:
							count += 1
							continue
						for g in range(0, 101):
							if val(a,b,c,d,e,f,g) > 200:
								continue
							if val(a,b,c,d,e,f,g) == 200:
								count +=1 
								continue
							for h in range(0, 201):
								if val(a,b,c,d,e,f,g,h) > 200:
									continue
								if val(a,b,c,d,e,f,g,h) == 200:
									count += 1
									continue
print count