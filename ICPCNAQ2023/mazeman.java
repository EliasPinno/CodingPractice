package ICPCNAQ2023;

import java.util.Scanner;

public class mazeman {

    static int[][] UDLR = {{-1,0},{1,0},{0,1},{0,-1}};

    static int n;
    static int m;
    public static void main(String args[]) {
        // Read all inputs
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        m = in.nextInt();
        in.nextLine();
        char[][] maze = new char[n][m];
        char c;
        int totalDots = 0;
        for(int i = 0; i < n; i++){
            String line = in.nextLine();
            for(int j = 0; j < m; j++){
                c = line.charAt(j);
                if(c == '.') totalDots++;
                maze[i][j] = c;
            }
        }
        in.close();
        int dotsConsumed = 0;
        int entrancesUsed = 0;
        int totalDotsConsumed = 0;
        for(int i = 0; i < n; i++){
            dotsConsumed = startDFS(maze,i,0);
            if (dotsConsumed > 0){
                totalDotsConsumed += dotsConsumed;
                entrancesUsed += 1;
            }
            dotsConsumed = startDFS(maze,i,m-1);
            if (dotsConsumed > 0){
                totalDotsConsumed += dotsConsumed;
                entrancesUsed += 1;
            }
        }
        for(int j = 0; j < m; j++){
            dotsConsumed = startDFS(maze,0,j);
            if (dotsConsumed > 0){
                totalDotsConsumed += dotsConsumed;
                entrancesUsed += 1;
            }
            dotsConsumed = startDFS(maze,n-1,j);
            if (dotsConsumed > 0){
                totalDotsConsumed += dotsConsumed;
                entrancesUsed += 1;
            }
        }
        System.out.printf("%d %d",entrancesUsed, totalDots-totalDotsConsumed);

    }

    public static int startDFS(char[][] maze, int i, int j){
        char entrance = maze[i][j];
        int total = 0;
        if(!isEntrance(entrance)) return 0;
        for (int[] pair: UDLR){
            total += dfs(maze,i+pair[0],j+pair[1],Character.toLowerCase(entrance));
        }
        return total;
    }

    /* Returns dots eaten from a traversal */
    public static int dfs(char[][] maze, int i, int j, char entrance){
        if (i < 0 || i >= n || j < 0 || j >= m){
            return 0;
        }
        char c = maze[i][j];
        if(canTraverse(c)) {
            int total = 0;
            if (c == '.') total += 1;
            maze[i][j] = entrance;
            for (int[] pair: UDLR){
                total += dfs(maze,i+pair[0],j+pair[1],entrance);
            }
            return total;
        } else {
            return 0;
        }
    }

    public static boolean isEntrance(char c) {
        return c >= 'A' && c <= 'W';
    }

    public static boolean canTraverse(char c) {
        return c == ' ' || c == '.';
    }
}