using System;
using System.Linq;

public class Program {
  public int[] SortedSquaredArray(int[] array) {
    // Write your code here.
    var squaredNumbers = array.Select(x => x * x).ToArray();
    Array.Sort(squaredNumbers);
    return squaredNumbers;
  }
}
// O(n) space and O(nlogn) time.