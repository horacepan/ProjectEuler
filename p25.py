import math

def nextFib(prev, prev2):
	return prev+prev2

if __name__ == "__main__":
	found = False
	prev = 1; prev2 = 1
	index = 3
	while not found:
		current = nextFib(prev, prev2)
		if math.log(current, 10) >= 1000:
			found = True
		else:
			prev2 = prev
			prev = current
			index += 1

	print index, " is index"

