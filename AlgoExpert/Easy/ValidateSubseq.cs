using System;
using System.Collections.Generic;

public class Program {
  public static bool IsValidSubsequence(List<int> array, List<int> sequence) {
    if(sequence.Count > array.Count) {
        return false;
    }
    int arrPtr = 0;
    int seqPtr = 0;
    while (arrPtr < array.Count && seqPtr < sequence.Count) {
        if(array[arrPtr] == sequence[seqPtr]) {
            seqPtr += 1;
        }
        arrPtr += 1;
    }
    return seqPtr == sequence.Count;
  }
}

// O(n) time, O(1) space.