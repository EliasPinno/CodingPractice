using System;

public class Program {
  public int NonConstructibleChange(int[] coins) {
    // Write your code here.
    if (coins.Length == 0) {
        return 1;
    }
    Array.Sort(coins);
    int currentMinimumCantMake = 1;
    while (true) {
        int currentSum = 0;
        int i = 0;
        while(i < coins.Length) {
            if(coins[i] > currentMinimumCantMake) {
                break;
            } 
            currentSum += coins[i];
            i += 1;
        }
        if (currentSum < currentMinimumCantMake) {
            return currentMinimumCantMake;
        }
        currentMinimumCantMake += 1;
    }
    return currentMinimumCantMake;
  }
}
// O(nlogn) where n is number of coins time
// O(1) space: no new space used