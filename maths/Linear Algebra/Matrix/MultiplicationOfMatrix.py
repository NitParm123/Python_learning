def main():
  """Main method to demonstrate matrix multiplication."""
  A = [[1, 2, 3],
        [4, 5, 6]]
  B = [[7, 8],
        [9, 10],
        [11, 12]]  
  result = matrix_multiply(A, B)
  print("Result of A x B:")
  for row in result:
    print(row)


def matrix_multiply(A, B):
  """Multiplies two matrices A and B."""
  # Get the number of rows and columns of the input matrices
  rows_A = len(A)
  cols_A = len(A[0]) if A else 0
  rows_B = len(B)
  cols_B = len(B[0]) if B else 0

  # Check if the number of columns in A is equal to the number of rows in B
  if cols_A != rows_B:
    raise ValueError("Number of columns in A must be equal to number of rows in B")

  # Initialize the result matrix with zeros
  result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

  # Perform matrix multiplication
  for i in range(rows_A):
    for j in range(cols_B):
      for k in range(cols_A):
        result[i][j] += A[i][k] * B[k][j]

  return result

if __name__ == "__main__":
  main()