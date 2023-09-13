using System;

public class Program {
  public int[,] TransposeMatrix(int[,] matrix) {
    int[,] solutionMatrix = new int[matrix.GetLength(1), matrix.GetLength(0)];
    for (int i = 0; i < matrix.GetLength(0); i++) {
        for (int j = 0; j < matrix.GetLength(1); j++) {
            solutionMatrix[j, i] = matrix[i, j];
        }
    }
    return solutionMatrix;
  }
}