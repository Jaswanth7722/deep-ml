def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	values = 0
	rows = 0
	outputs = []
	if mode == "column":
		for j in range(len(matrix[0])):
			values = 0
			for i in range(len(matrix)):
				values += matrix[i][j]
			outputs.append(values / len(matrix))
	
	else:
		import numpy as np
		return np.mean(matrix, axis=1).tolist()
	return outputs