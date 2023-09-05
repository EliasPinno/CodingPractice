using System;
using System.Linq;

public class Program {
  public int[] SortedSquaredArray(int[] array) {
    // Write your code here.
    int[] squaredNumbers = new int[array.Length];
    int leftSide = 0;
    int rightSide = array.Length-1;
    int nextValue = array.Length-1;
    while (nextValue >= 0) {
        int leftValue = array[leftSide]*array[leftSide];
        int rightValue = array[rightSide]*array[rightSide];
        if(leftValue > rightValue) {
            squaredNumbers[nextValue] = leftValue;
            leftSide += 1;
        } else {
            squaredNumbers[nextValue] = rightValue;
            rightSide -= 1;
        }
        nextValue -= 1;
    }
    return squaredNumbers;
  }
}
// O(n) time, O(n) space.