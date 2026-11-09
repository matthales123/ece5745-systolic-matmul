//========================================================================
// ubmark-mmmult-eval
//========================================================================

#include "ece4750.h"
#include "ubmark-matrix-mult.h"
// #include "ubmark-matrix-mult-test.c"

//------------------------------------------------------------------------
// Compare Result Matrix and Reference Matrix
//------------------------------------------------------------------------
// Helper function that returns 1 if the value at all indices of both matrices 
// are equal 

int compare_matrices(int* A, int* B, int n, int m) {
    int i = 0;

    // Compare each element of matrices "A" and "B"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            // If an element of "A" is not equal to the corresponding element of "B", return false
            if (A[i * m + j] != B[i * m + j]) {
                return 0;
            }
        }
    }

    // If all elements of "A" are equal to the corresponding elements of "B", return true
    return 1;
}

//------------------------------------------------------------------------
// Generates a matrix of random values
//------------------------------------------------------------------------
// n: defines the number of rows
// m: defines the number of columns
// min_val: the minimum possible randomly generated value
// max_val: the maximum possible randomly generated values
void generate_random_matrix(int* A, int n, int m, int min_val, int max_val) {
    // Set the seed for the random number generator
    ece4750_srand(0x0000f1ef);
    int i = 0;

    // Calculate the range of values that can be generated
    int range = max_val - min_val + 1;

    // Generate random values for each element of the matrix
    for (i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            // Generate a random integer between min_val and max_val (inclusive)
            // and assign it to the current element of the matrix
            A[i * m + j] = (ece4750_rand() % range) + min_val;
        }
    }
}


//------------------------------------------------------------------------
// Reference Matrix Multiplication for comparison, ensures multiplication
// is correct
//------------------------------------------------------------------------
// A: input matrix A
// B: input matrix A
// C: ouput matrix
// n: defines the number of rows in matrix A
// m: defines the number of columns in matrix A and number of rows in matrix B
// p: defines the number of columns in matrix B

void matrix_multiply_reference(int* A, int* B, int* C, int n, int m, int p) {
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


void print_matrix(int* A, int n, int m) {
    for (int i = 0; i < n; i++) {
        ece4750_wprintf(L"| ");
        for (int j = 0; j < m; j++) {
            ece4750_wprintf(L"%d ", A[i * m + j]);
        }
        ece4750_wprintf(L"|\n");
    }
}



int main( void )
{
  // Run the evaluation
  //ece4750_stats_on();

  const int n = 5;
  const int m = 5;
  const int p = 5;
  const int min_val = 0;
  const int max_val = 5;
  //int i = 0;

  int* A = ece4750_malloc( (n*m) * (int)sizeof(int) ) ;
  int* B = ece4750_malloc( (m*p) * (int)sizeof(int) ) ;
  int* C = ece4750_malloc( (n*p) * (int)sizeof(int) ) ;
  int* C_ref = ece4750_malloc( (n*p) * (int)sizeof(int) ) ;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < p; j++) {
        C[i] = 0;
        // ece4750_wprintf( L"C[i][j]: %d\n", C[i][j] );
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < p; j++) {
        C_ref[i] = 0;
        // ece4750_wprintf( L"C[i][j]: %d\n", C[i][j] );
    }
  }

  generate_random_matrix(A, n, m, min_val, max_val);
  //print_matrix(A, n, m);
  generate_random_matrix(B, m, p, min_val, max_val);
  //print_matrix(B, n, m);

  ece4750_stats_on();
  matrix_multiply(A, B, C, n, m, p);
  ece4750_stats_off();
  //print_matrix(C, n, m);
  matrix_multiply_reference(A, B, C_ref, n, m, p);
  //print_matrix(C_ref, n, m);

  // Verify the results
  int results = compare_matrices(C, C_ref, n, m); 
  if (results == 1) {
        ece4750_wprintf( L"Matrix multiplication test passed.\n");
  } else {
        ece4750_wprintf( L"Matrix multiplication test failed.\n");
  }

  ece4750_free(A);
  ece4750_free(B);
  ece4750_free(C);
  ece4750_free(C_ref);

  // Check for no memory leaks

  if ( ece4750_get_heap_usage() != 0 ) {
    ece4750_wprintf( L"\n FAILED: memory leak of %d bytes!\n\n",
                     ece4750_get_heap_usage() );
    ece4750_exit(1);
  }

  // Otherwise we passed

  ece4750_wprintf( L"\n **PASSED** \n\n" );

  return 0;
}

