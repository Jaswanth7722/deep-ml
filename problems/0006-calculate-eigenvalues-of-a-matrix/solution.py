def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	import numpy as np
	
	trace = np.trace(matrix)

	eigenvaluess = []

	det = (matrix[0][0] * matrix[1][1] ) - (matrix[0][1] * matrix[1][0] )

	eigen = (trace + (trace**2 - 4*det) ** 0.5) /2
	eigen2 = (trace - (trace**2 - 4*det) ** 0.5) /2

	eigenvaluess.append(eigen)
	eigenvaluess.append(eigen2)
	
	return eigenvaluess