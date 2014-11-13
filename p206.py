import math
import time

def hasRightForm(num):
	if num%100 != 0:
		return False
	str_num = str(num/100)
	if str_num[::2] != '123456789':
		return False
	return True

	return True	

if __name__ == "__main__":
	start_time = time.time()
	current = 1010100930
	print hasRightForm(1020304050607081900)
	found = False
	while not found:
		current += 100
		if hasRightForm(current**2):
			found = True
		if not found and hasRightForm((current+40)**2):
			found = True
			current += 40	
	print current
	print "Time elapsed: ", time.time()-start_time
