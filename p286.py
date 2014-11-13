from numpy import zeros

def getProb(q):
	prob = zeros((51, 51)) # probTable[x][y] = prob of hitting y shots given the shots 1,2,3...,x	
	prob[0][0] = 1
	for x in range(1,51):
		for y in range(0,51):
			if y > 0:
				prob[x][y] += prob[x-1][y-1] * (1-(float(x)/q))	
			prob[x][y] += prob[x-1][y] * (float(x)/q)
	
	return prob[50][20]

def search():
	lo = 50; hi = 60
	mid = 0.5*(lo+hi)
	found = False
	iters = 100
	while (hi-lo > 1e-13):
		if getProb(mid) > 0.02:
			lo = mid
		else:
			hi = mid
		mid = 0.5*(lo+hi)
		print mid	
	return mid

if __name__ == "__main__":
	print search()
