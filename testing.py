import time
from math import ceil

def mystery_num():
	m0, m1 = int(ceil((1.02 * 10 ** 16) ** 0.5)), int(ceil((1.93 * 10 ** 16) ** 0.5))
	m0, m1 = m0 / 1000 * 1000, (m1 / 1000 + 1) * 1000 + 1
	for r in (x for x in xrange(1000) if x * x % 10 == 9 and (x * x % 1000) / 100 == 8):
		for m in xrange(m0 + r, m1, 1000):
			if str(m * m)[::2] == '123456789': return 10 * m

if __name__ == "__main__":
	start_time = time.time()
	n = mystery_num()
	print n, n*n
	print"seconds:", time.time() - start_time
