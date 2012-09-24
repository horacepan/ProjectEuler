def run():
	masterList = []
	listPrev = [1,1]
	masterList.append(listPrev)
	index = 1 # tells us how many rows we've done
	count = 0 # number greater than 1 mil
	while index < 100:
	
		listNext = []
		for i in range(0, index + 2):
			if i == 0 or i == index +1:
				listNext.append(1)
			else:
				val = listPrev[i-1] + listPrev[i]
				listNext.append(val)
				if val > 1000000:
					count += 1
		index += 1
		listPrev = listNext
		masterList.append(listNext)
	print count
	
if __name__ == '__main__':
	run()