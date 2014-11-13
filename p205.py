import time
import random
import sys

def rollDice(sides):
	return random.randint(1, sides)	

if __name__ == "__main__":
	trials = int(sys.argv[1])
	four_wins = 0
	for i in xrange(trials):
		four_count = 0
		six_count = 0
		for j in xrange(9):
			four_count += rollDice(4)
		for k in xrange(6):
			six_count += rollDice(6)
		if four_count > six_count:
			four_wins += 1

	print four_wins, trials	
