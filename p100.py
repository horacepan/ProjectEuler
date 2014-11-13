import pdb
import sys

found = False

def find_blue(minimum):
	found = False
	current = minimum 
	rt_half = 0.5**0.5
	while not found:
		# Condition only holds if total discs is 0 or 1 mod 3
		current += 1
		total_prod = current*(current-1)
		blue = int(rt_half*current)
		while not found:
			diff = 2*(blue*(blue-1)) - total_prod
			if diff < 0:
				blue += 1
			elif diff == 0:
				found = True
			else:
				break

	return blue, current

if __name__ == "__main__":
	minimum = int(sys.argv[1])
	print find_blue(minimum)	
