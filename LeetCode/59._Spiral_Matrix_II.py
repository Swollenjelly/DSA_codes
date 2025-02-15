class Solution {
    public int[][] generateMatrix(int n) {
         int[][] matrix = new int[n][n]; // Create an n x n matrix filled with 0s
        int num = 1; // The number to fill in the matrix

        int top = 0, bottom = n - 1;
        int left = 0, right = n - 1;

        while (num <= n * n) {
            // Traverse from left to right
            for (int i = left; i <= right; i++) {
                matrix[top][i] = num++;
            }
            top++; // Move top boundary down

            // Traverse from top to bottom
            for (int i = top; i <= bottom; i++) {
                matrix[i][right] = num++;
            }
            right--; // Move right boundary left

            // Traverse from right to left
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    matrix[bottom][i] = num++;
                }
                bottom--; // Move bottom boundary up
            }

            // Traverse from bottom to top
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    matrix[i][left] = num++;
                }
                left++; // Move left boundary right
            }
        }

        return matrix;
    }
        
    }
