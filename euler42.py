import string

def run():
	f = open('words.txt', 'r')
	count = 0
	alphaDict = dict(zip(string.uppercase, range(1, 27)))
	triangleNumbers = set((n*(n+1))/2 for n in range(1, 31) if (n*(n+1))/2 < 364)

	def parse(word):
		return word[1:len(word)-1]

	def isTriangle( word ):
		sum = 0
		for letter in word:
			sum += alphaDict[letter]
		return sum in triangleNumbers

	count = 0
	number = 0
	for line in f:
		x = line.split(',')
		for word in x:
			word = parse(word)
			if isTriangle(word):
				count += 1
			number += 1
	print count
	
if __name__ == '__main__':
	run()