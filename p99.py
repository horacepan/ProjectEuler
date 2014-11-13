import math

if __name__ == "__main__":
	max_exp = 0
	max_line = 1
	line_num = 1
	for line in open('base_exp.txt', 'r'):
		[base, exp] = map(lambda r: int(r), line[:-1].split(','))
		# natural log is a monotonically increasing function
		# so if ln(x) > ln(y), then x>y
		if exp*math.log(base) > max_exp:
			max_exp = exp*math.log(base)
			max_line = line_num
		line_num += 1	
	print max_line
			
