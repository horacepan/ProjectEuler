from numpy import zeros

def build_table(matrix, table):
	x_max,y_max = table.shape
	
	for i in range(x_max-1, -1, -1):
		for j in range(y_max-1, -1, -1):
			if j < y_max-1 and i < x_max-1: # non edge piece
				right_best_path = table[i+1][j] 
				down_best_path = table[i][j+1]
				best_path = min(right_best_path, down_best_path)
			elif j < y_max-1: # edge x piece room for y value to move
				best_path = table[i][j+1]	
			elif i < x_max-1: # edge y piece room for x to move
				best_path = table[i+1][j]
			else:
				best_path = 0
			table[i][j] = matrix[i][j] + best_path

if __name__ == "__main__":
	matrix = zeros((80, 80))
	table = zeros((80, 80))
	line_num = 0
	for line in open('matrix.txt', 'r'):
		values = map(lambda r: int(r), line[:-1].split(','))
		matrix[line_num] = values	
		line_num += 1

	# init
	table[79][79] = matrix[79][79]
	build_table(matrix, table)	
	print table[0][0]
