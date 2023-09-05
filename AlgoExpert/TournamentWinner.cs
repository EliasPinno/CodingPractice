using System.Collections.Generic;
using System;

public class Program {
  public string TournamentWinner(
    List<List<string> > competitions, List<int> results
  ) {
    // Idea: Have a dictonary with an entry for each team
    // Increment each value in dict for each win
    // Give the max winner in the dict
    Dictionary<string, int> arrayDict = new Dictionary<string, int>();
    for(int i = 0; i < competitions.Count; i++) {
        // Turn winning team into the correct index
        string winningTeam = competitions[i][(results[i] ^ 1)];
        if(!arrayDict.ContainsKey(winningTeam)){
            arrayDict.Add(winningTeam, 1);
        } else { 
            arrayDict[winningTeam] = arrayDict[winningTeam]+1;
        }   
    }
    string maxWinner = "";
    int maxWinnerNumber = 0;
    foreach (string arrayKey in arrayDict.Keys) {
       if(arrayDict[arrayKey] > maxWinnerNumber) {
           maxWinnerNumber = arrayDict[arrayKey];
           maxWinner = arrayKey;
       }
    }
    return maxWinner;
  }
}
// Space: O(k) where k is number of teams with 1 or more wins
// Time: O(n) where n is the number of competitions