using System;

public class Program {
  public static int[] TwoNumberSum(int[] array, int targetSum) {
      int[] solution = new int[2];
      bool solutionFound = false;
      for(int i = 0; i < array.Length; i++){
          int target = targetSum - array[i];
          for(int j = i+1; j < array.Length; j++) {
              if(array[j] == target){
                  solution[0] = array[i];
                  solution[1] = array[j];
                  solutionFound = true;
                  break;
              }
          }
          if(solutionFound){
              break;
          }
      }
    // Write your code here.
    if(solutionFound)
        return solution;
    return new int[0];
  }
}
// Time complexity: O(n^2) where n is the number of items in the array
// Space complexity: O(n)