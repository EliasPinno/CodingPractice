using System;
using System.Collections.Generic;

public class Program {
  public static int[] TwoNumberSum(int[] array, int targetSum) {
    // Idea: Create a hash table of all of our values. Then check for each value once
    // Inside of the hashtable to see if we can find
    Dictionary<int, int> arrayDict = new Dictionary<int, int>();
    for(int i = 0; i < array.Length; i++){
        if(!arrayDict.ContainsKey(array[i])){
            arrayDict.Add(array[i], 1);
        }
        else {
            arrayDict[array[i]] = arrayDict[array[i]]+1;
            }
    }
    bool foundSolution = false;
    int[] solution = new int[2];
    for(int i = 0; i < array.Length; i++){
        if(arrayDict.ContainsKey(targetSum - array[i])){
            if(array[i] == targetSum - array[i] && arrayDict[array[i]] == 1) {
                continue;
            }
            solution[0] = array[i];
            solution[1] = targetSum - array[i];
            foundSolution = true;
            break;
        }
    }
    if(foundSolution){
        return solution;
    }
    return new int[0];
  }
}
// Space: O(n) where n is number of values in array
// Time: O(n) where n is number of value in array (2n runtime)