//========================================================================
// ubmark-matrix-mult
//========================================================================
// This function performs dense matrix multiplication of two input matrices A and B
// and returns the result matrix C. Inputs:
// n is the number of rows in input matrix A
// m is the number of columns in input matrix A and number rows in input matrix B
// p is the number of coloumns in input matrix B
// Note: output matrix C is of dimension A[n x m] * B[m x p] = C[n x p]

// #include "ece4750.h"
#include "ubmark-matrix-mult.h"
// #include "ubmark-matrix-mult.dat"


//------------------------------------------------------------------------
// Matrix Multiplication
//------------------------------------------------------------------------
// A: input matrix A
// B: input matrix A
// C: ouput matrix
// n: defines the number of rows in matrix A
// m: defines the number of columns in matrix A and number of rows in matrix B
// p: defines the number of columns in matrix B
void matrix_multiply(int* A, int* B, int* C, int n, int m, int p) {
    // Perform matrix multiplication
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // Initialize the value of C[i][j] to 0
            C[i * p + j] = 0;

            // Calculate each element of C
            for (int k = 0; k < m; k++) {
                C[i * p + j] += A[i * m + k] * B[k * p + j];
            }
        }
    }
}