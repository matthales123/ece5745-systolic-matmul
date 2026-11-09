//========================================================================
// Unit tests for ubmark matrix multiplication
//========================================================================

#include "ece4750.h"
#include "ubmark-matrix-mult.h"
#include "ubmark-matrix-mult.dat"

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
            A[i * m + j] = ece4750_rand() % range + min_val;
        }
    }
}

//------------------------------------------------------------------------
// Matrix - Matrix Multiply Reference Function
//------------------------------------------------------------------------
// Helper function that computes the matrix - matrix multiplication and returns
// the resulting matrix C

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


//------------------------------------------------------------------------
// Directed Tests
//------------------------------------------------------------------------

//------------------------------------------------------------------------
// Directed Test - A and B 1x1
//------------------------------------------------------------------------
void test_case_1_mult_A11_B11()
{
    ECE4750_CHECK( L"test_case_1_mult_A11_B11" );
    const int n = 1;
    const int m = 1;
    const int p = 1;
    // const int min_val = 0;
    // const int max_val = 5;
    int i;

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


    A = (int []){2};
    B = (int []){3};
    //print_matrix(B, n, m);

    matrix_multiply(A, B, C, n, m, p);
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

    // ece4750_free(A);
    // ece4750_free(B);
    // ece4750_free(C);
    // ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // // ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// Directed Tests - A and B 1x1 zeros
//------------------------------------------------------------------------
void test_case_2_mult_A11_B11_zero()
{
ECE4750_CHECK( L"test_case_2_mult_A11_B11_zero" );
    const int n = 1;
    const int m = 1;
    const int p = 1;
    // const int min_val = 0;
    // const int max_val = 5;
    int i;

    int* A = ece4750_malloc( (n*m) * (int)sizeof(int) ) ;
    int* B = ece4750_malloc( (m*p) * (int)sizeof(int) ) ;
    int* C = ece4750_malloc( (n*p) * (int)sizeof(int) ) ;
    int* C_ref = ece4750_malloc( (n*p) * (int)sizeof(int) ) ;

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    //print_matrix(B, n, m);

    matrix_multiply(A, B, C, n, m, p);
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

    // ece4750_free(A);
    // ece4750_free(B);
    // ece4750_free(C);
    // ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// // ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}


//------------------------------------------------------------------------
// Directed Tests - A and B 2x2
//------------------------------------------------------------------------
void test_case_3_mult_A22_B22()
{
ECE4750_CHECK( L"test_case_3_mult_A22_B22" );
    const int n = 2;
    const int m = 2;
    const int p = 2;
    int i;

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

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    A = (int []){
        1, 2,
        3, 4
    };

    B = (int []){
        5, 6,
        7, 8
    };

    //print_matrix(B, n, m);

    matrix_multiply(A, B, C, n, m, p);
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

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// Directed Tests - A and B 2x2 zeros
//------------------------------------------------------------------------
void test_case_4_mult_A22_B22_zero()
{
ECE4750_CHECK( L"test_case_4_mult_A22_B22_zero" );
    const int n = 2;
    const int m = 2;
    const int p = 2;
    int i;

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

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    //print_matrix(B, n, m);

    matrix_multiply(A, B, C, n, m, p);
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

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}


//------------------------------------------------------------------------
// Directed Tests - A and B 3x3
//------------------------------------------------------------------------
void test_case_5_mult_A33_B33()
{
    ECE4750_CHECK( L"test_case_5_mult_A33_B33" );
    const int n = 3;
    const int m = 3;
    const int p = 3;
    int i;

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

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    A = (int []){
        1, 2, 3,
        4, 5, 6,
        7, 8, 9
    };

    B = (int []){
        9, 8, 7,
        6, 5, 4,
        3, 2, 1
    };


    //print_matrix(B, n, m);

    matrix_multiply(A, B, C, n, m, p);
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

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// Directed Tests - A and B 3x3 zeros
//------------------------------------------------------------------------
void test_case_6_mult_A33_B33_zero()
{
    ECE4750_CHECK( L"test_case_6_mult_A33_B33_zero" );
    const int n = 3;
    const int m = 3;
    const int p = 3;

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

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }


    //print_matrix(B, n, m);

    matrix_multiply(A, B, C, n, m, p);
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

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}


//------------------------------------------------------------------------
// Directed Tests - A and B 4x4
//------------------------------------------------------------------------
void test_case_7_mult_A44_B44()
{
    ECE4750_CHECK( L"test_case_7_mult_A44_B44" );
    const int n = 4;
    const int m = 4;
    const int p = 4;
    int i;

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

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    A = (int []){
        1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12,
        13, 14, 15, 16
    };

    B = (int []){
        16, 15, 14, 13,
        12, 11, 10, 9,
        8, 7, 6, 5,
        4, 3, 2, 1
    };


    //print_matrix(B, n, m);

    matrix_multiply(A, B, C, n, m, p);
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

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// Directed Tests - A and B 4x4 zeros
//------------------------------------------------------------------------
void test_case_8_mult_A44_B44_zero()
{
    ECE4750_CHECK( L"test_case_8_mult_A44_B44_zero" );
    const int n = 4;
    const int m = 4;
    const int p = 4;
    int i;

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

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    // A = (int []){
    //     0, 0, 0, 0,
    //     0, 0, 0, 0,
    //     0, 0, 0, 0,
    //     0, 0, 0, 0
    // };

    // B = (int []){
    //     0, 0, 0, 0,
    //     0, 0, 0, 0,
    //     0, 0, 0, 0,
    //     0, 0, 0, 0
    // };


    //print_matrix(B, n, m);

    matrix_multiply(A, B, C, n, m, p);
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

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// Directed Tests - A and B 5x5
//------------------------------------------------------------------------
void test_case_9_mult_A55_B55()
{
ECE4750_CHECK( L"test_case_9_mult_A55_B55" );
    const int n = 5;
    const int m = 5;
    const int p = 5;
    int i;

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

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    A = (int []){
        1,  2,  3,  4,  5,
        6,  7,  8,  9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20,
        21, 22, 23, 24, 25
    };

    B = (int []){
        25, 24, 23, 22, 21,
        20, 19, 18, 17, 16,
        15, 14, 13, 12, 11,
        10,  9,  8,  7,  6,
        5,  4,  3,  2,  1
    };


    //print_matrix(B, n, m);

    matrix_multiply(A, B, C, n, m, p);
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

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// Directed Tests - A and B 5x5 zeros
//------------------------------------------------------------------------
void test_case_10_mult_A55_B55_zero()
{
ECE4750_CHECK( L"test_case_10_mult_A55_B55_zero" );
    const int n = 5;
    const int m = 5;
    const int p = 5;
    int i;

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

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    // A = (int []){
    //     0,  0,  0,  0,  0,
    //     0,  0,  0,  0,  0,
    //     0,  0,  0,  0,  0,
    //     0,  0,  0,  0,  0,
    //     0,  0,  0,  0,  0
    // };

    // B = (int []){
    //     0,  0,  0,  0,  0,
    //     0,  0,  0,  0,  0,
    //     0,  0,  0,  0,  0,
    //     0,  0,  0,  0,  0,
    //     0,  0,  0,  0,  0
    // };


    //print_matrix(B, n, m);

    matrix_multiply(A, B, C, n, m, p);
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

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// Directed Tests - A 2x3 and B 3x2
//------------------------------------------------------------------------
void test_case_11_mult_A23_B32()
{
ECE4750_CHECK( L"test_case_11_mult_A23_B32" );
    const int n = 2;
    const int m = 3;
    const int p = 2;
    int i;

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

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    A = (int []){
        1,  2,  3,
        4,  5,  6
    };

    B = (int []){
        1,  2,
        3,  4,
        5,  6
    };


    //print_matrix(B, m, p);

    matrix_multiply(A, B, C, n, m, p);
    //print_matrix(C, n, p);
    matrix_multiply_reference(A, B, C_ref, n, m, p);
    //print_matrix(C_ref, n, p);

    // Verify the results
    int results = compare_matrices(C, C_ref, n, p); 
    if (results == 1) {
            ece4750_wprintf( L"Matrix multiplication test passed.\n");
    } else {
            ece4750_wprintf( L"Matrix multiplication test failed.\n");
    }

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// Directed Tests - A 2x3 and B 3x2 zeros
//------------------------------------------------------------------------
void test_case_12_mult_A23_B32_zero()
{
ECE4750_CHECK( L"test_case_12_mult_A23_B32_zero" );
    const int n = 2;
    const int m = 3;
    const int p = 2;
    int i;

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

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    // A = (int []){
    //     0,  0,  0,
    //     0,  0,  0
    // };

    // B = (int []){
    //     0,  0,
    //     0,  0,
    //     0,  0
    // };


    //print_matrix(B, m, p);

    matrix_multiply(A, B, C, n, m, p);
    //print_matrix(C, n, p);
    matrix_multiply_reference(A, B, C_ref, n, m, p);
    //print_matrix(C_ref, n, p);

    // Verify the results
    int results = compare_matrices(C, C_ref, n, p); 
    if (results == 1) {
            ece4750_wprintf( L"Matrix multiplication test passed.\n");
    } else {
            ece4750_wprintf( L"Matrix multiplication test failed.\n");
    }

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// Directed Tests - A 3x3 and B 3x2
//------------------------------------------------------------------------
void test_case_13_mult_A33_B32()
{
ECE4750_CHECK( L"test_case_13_mult_A33_B32" );
    const int n = 3;
    const int m = 3;
    const int p = 2;
    int i;

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

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    A = (int []){
        1,  2,  3,
        4,  5,  6,
        7,  8,  9
    };

    B = (int []){
        1,  2,
        3,  4,
        5,  6
    };


    //print_matrix(B, m, p);

    matrix_multiply(A, B, C, n, m, p);
    //print_matrix(C, n, p);
    matrix_multiply_reference(A, B, C_ref, n, m, p);
    //print_matrix(C_ref, n, p);

    // Verify the results
    int results = compare_matrices(C, C_ref, n, p); 
    if (results == 1) {
            ece4750_wprintf( L"Matrix multiplication test passed.\n");
    } else {
            ece4750_wprintf( L"Matrix multiplication test failed.\n");
    }

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// Directed Tests - A 3x3 and B 3x2 zeros
//------------------------------------------------------------------------
void test_case_14_mult_A33_B32_zero()
{
ECE4750_CHECK( L"test_case_14_mult_A33_B32_zero" );
    const int n = 3;
    const int m = 3;
    const int p = 2;
    int i;

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

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    // A = (int []){
    //     0,  0,  0,
    //     0,  0,  0,
    //     0,  0,  0
    // };

    // B = (int []){
    //     0,  0,
    //     0,  0,
    //     0,  0
    // };


    //print_matrix(B, m, p);

    matrix_multiply(A, B, C, n, m, p);
    //print_matrix(C, n, p);
    matrix_multiply_reference(A, B, C_ref, n, m, p);
    //print_matrix(C_ref, n, p);

    // Verify the results
    int results = compare_matrices(C, C_ref, n, p); 
    if (results == 1) {
            ece4750_wprintf( L"Matrix multiplication test passed.\n");
    } else {
            ece4750_wprintf( L"Matrix multiplication test failed.\n");
    }

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// Directed Tests - A 4x3 and B 3x5
//------------------------------------------------------------------------
void test_case_15_mult_A43_B35()
{
ECE4750_CHECK( L"test_case_15_mult_A43_B35" );
    const int n = 4;
    const int m = 3;
    const int p = 5;
    int i;

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

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    A = (int []){
        1,  2,  3,
        4,  5,  6,
        7,  8,  9,
        10, 11, 12
    };

    B = (int []){
        1,  2,  3,  4,  5,
        6,  7,  8,  9, 10,
        11, 12, 13, 14, 15
    };


    //print_matrix(B, m, p);

    matrix_multiply(A, B, C, n, m, p);
    //print_matrix(C, n, p);
    matrix_multiply_reference(A, B, C_ref, n, m, p);
    //print_matrix(C_ref, n, p);

    // Verify the results
    int results = compare_matrices(C, C_ref, n, p); 
    if (results == 1) {
            ece4750_wprintf( L"Matrix multiplication test passed.\n");
    } else {
            ece4750_wprintf( L"Matrix multiplication test failed.\n");
    }

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}


//------------------------------------------------------------------------
// Directed Tests - A 4x3 and B 4x5 zeros
//------------------------------------------------------------------------
void test_case_16_mult_A43_B35_zero()
{
ECE4750_CHECK( L"test_case_16_mult_A43_B35_zero" );
    const int n = 4;
    const int m = 3;
    const int p = 5;
    int i;

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

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    // A = (int []){
    //     0,  0,  0,
    //     0,  0,  0,
    //     0,  0,  0,
    //     0,  0,  0
    // };

    // B = (int []){
    //     0,  0,  0,  0,  0,
    //     0,  0,  0,  0,  0,
    //     0,  0,  0,  0,  0
    // };


    //print_matrix(B, m, p);

    matrix_multiply(A, B, C, n, m, p);
    //print_matrix(C, n, p);
    matrix_multiply_reference(A, B, C_ref, n, m, p);
    //print_matrix(C_ref, n, p);

    // Verify the results
    int results = compare_matrices(C, C_ref, n, p); 
    if (results == 1) {
            ece4750_wprintf( L"Matrix multiplication test passed.\n");
    } else {
            ece4750_wprintf( L"Matrix multiplication test failed.\n");
    }

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// Directed Tests - A 4x3 and B 4x5
//------------------------------------------------------------------------
void test_case_17_mult_A43_B35()
{
ECE4750_CHECK( L"test_case_17_mult_A43_B35" );
    const int n = 4;
    const int m = 3;
    const int p = 5;
    int i;

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

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    A = (int []){
        1,  2,  3,
        4,  5,  6,
        7,  8,  9,
        10, 11, 12
    };

    B = (int []){
        1,  2,  3,  4,  5,
        6,  7,  8,  9, 10,
        11, 12, 13, 14, 15
    };


    //print_matrix(B, m, p);

    matrix_multiply(A, B, C, n, m, p);
    //print_matrix(C, n, p);
    matrix_multiply_reference(A, B, C_ref, n, m, p);
    //print_matrix(C_ref, n, p);

    // Verify the results
    int results = compare_matrices(C, C_ref, n, p); 
    if (results == 1) {
            ece4750_wprintf( L"Matrix multiplication test passed.\n");
    } else {
            ece4750_wprintf( L"Matrix multiplication test failed.\n");
    }

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// Directed Tests - A 4x3 and B 4x5 zeros
//------------------------------------------------------------------------
void test_case_18_mult_A43_B35_zeros()
{
ECE4750_CHECK( L"test_case_18_mult_A43_B35_zeros" );
    const int n = 4;
    const int m = 3;
    const int p = 5;
    int i;

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

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    // A = (int []){
    //     0,  0,  0,
    //     0,  0,  0,
    //     0,  0,  0,
    //     0,  0,  0
    // };

    // B = (int []){
    //     0,  0,  0,  0,  0,
    //     0,  0,  0,  0,  0,
    //     0,  0,  0,  0,  0
    // };


    //print_matrix(B, m, p);

    matrix_multiply(A, B, C, n, m, p);
    //print_matrix(C, n, p);
    matrix_multiply_reference(A, B, C_ref, n, m, p);
    //print_matrix(C_ref, n, p);

    // Verify the results
    int results = compare_matrices(C, C_ref, n, p); 
    if (results == 1) {
            ece4750_wprintf( L"Matrix multiplication test passed.\n");
    } else {
            ece4750_wprintf( L"Matrix multiplication test failed.\n");
    }

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}


//------------------------------------------------------------------------
// Directed Tests - A 5x1 and B 1x5
//------------------------------------------------------------------------
void test_case_19_mult_A51_B15()
{
ECE4750_CHECK( L"test_case_19_mult_A51_B15" );
    const int n = 5;
    const int m = 1;
    const int p = 5;
    int i;

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

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    A = (int []){
        1,
        2,
        3,
        4,
        5
    };

    B = (int []){
        1,  2,  3,  4,  5
    };


    //print_matrix(B, m, p);

    matrix_multiply(A, B, C, n, m, p);
    //print_matrix(C, n, p);
    matrix_multiply_reference(A, B, C_ref, n, m, p);
    //print_matrix(C_ref, n, p);

    // Verify the results
    int results = compare_matrices(C, C_ref, n, p); 
    if (results == 1) {
            ece4750_wprintf( L"Matrix multiplication test passed.\n");
    } else {
            ece4750_wprintf( L"Matrix multiplication test failed.\n");
    }

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// Directed Tests - A 5x1 and B 1x5 zeros
//------------------------------------------------------------------------
void test_case_20_mult_A51_B15_zero()
{
ECE4750_CHECK( L"test_case_20_mult_A51_B15_zero" );
    const int n = 5;
    const int m = 1;
    const int p = 5;
    int i;

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
    
    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    // A = (int []){
    //     0,
    //     0,
    //     0,
    //     0,
    //     0
    // };

    // B = (int []){
    //     0,  0,  0,  0,  0
    // };


    //print_matrix(B, m, p);

    matrix_multiply(A, B, C, n, m, p);
    //print_matrix(C, n, p);
    matrix_multiply_reference(A, B, C_ref, n, m, p);
    //print_matrix(C_ref, n, p);

    // Verify the results
    int results = compare_matrices(C, C_ref, n, p); 
    if (results == 1) {
            ece4750_wprintf( L"Matrix multiplication test passed.\n");
    } else {
            ece4750_wprintf( L"Matrix multiplication test failed.\n");
    }

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// Directed Tests - A 5x3 and B 3x1
//------------------------------------------------------------------------
void test_case_21_mult_A53_B31()
{
ECE4750_CHECK( L"test_case_21_mult_A53_B31" );
    const int n = 5;
    const int m = 3;
    const int p = 1;
    int i;

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

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    A = (int []){
        1,  2,  3,
        4,  5,  6,
        7,  8,  9,
        10, 11, 12,
        13, 14, 15
    };

    B = (int []){
        1,
        2,
        3
    };


    //print_matrix(B, m, p);

    matrix_multiply(A, B, C, n, m, p);
    //print_matrix(C, n, p);
    matrix_multiply_reference(A, B, C_ref, n, m, p);
    //print_matrix(C_ref, n, p);

    // Verify the results
    int results = compare_matrices(C, C_ref, n, p); 
    if (results == 1) {
            ece4750_wprintf( L"Matrix multiplication test passed.\n");
    } else {
            ece4750_wprintf( L"Matrix multiplication test failed.\n");
    }

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}


//------------------------------------------------------------------------
// Directed Tests - A 5x3 and B 3x1 zeros
//------------------------------------------------------------------------
void test_case_22_mult_A53_B31_zero()
{
ECE4750_CHECK( L"test_case_22_mult_A53_B31_zero" );
    const int n = 5;
    const int m = 3;
    const int p = 1;
    int i;

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

    // Initialize matrix A with zeros
    for (int i = 0; i < n * m; i++) {
        A[i] = 0;
    }

    // Initialize matrix B with zeros
    for (int i = 0; i < m * p; i++) {
        B[i] = 0;
    }

    // A = (int []){
    //     0,  0,  0,
    //     0,  0,  0,
    //     0,  0,  0,
    //     0,  0,  0,
    //     0,  0,  0
    // };

    // B = (int []){
    //     0,
    //     0,
    //     0
    // };


    //print_matrix(B, m, p);

    matrix_multiply(A, B, C, n, m, p);
    //print_matrix(C, n, p);
    matrix_multiply_reference(A, B, C_ref, n, m, p);
    //print_matrix(C_ref, n, p);

    // Verify the results
    int results = compare_matrices(C, C_ref, n, p); 
    if (results == 1) {
            ece4750_wprintf( L"Matrix multiplication test passed.\n");
    } else {
            ece4750_wprintf( L"Matrix multiplication test failed.\n");
    }

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}


//------------------------------------------------------------------------
// Random Tests
//------------------------------------------------------------------------
void test_case_23_mult_basic()
{
ECE4750_CHECK( L"test_case_23_mult_basic" );
    const int n = 3;
    const int m = 3;
    const int p = 3;
    const int min_val = 0;
    const int max_val = 5;
    int i;

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

    matrix_multiply(A, B, C, n, m, p);
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

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//''' LAB TASK '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
// Add many more test cases for helper functions and sort function
//''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\/

//------------------------------------------------------------------------
// test_case_2_mult_five_elements 
//------------------------------------------------------------------------
// A simple test case that tests sorting 5 numbers

void test_case_24_mult_five_element()
{
    ECE4750_CHECK( L"test_case_24_mult_five_element" );
    const int n = 5;
    const int m = 5;
    const int p = 5;
    const int min_val = 0;
    const int max_val = 5;
    int i = 0;

    // Allocate memory for the input matrices
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

    matrix_multiply(A, B, C, n, m, p);
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

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

// // ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );

    // ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// test_case_3_mult_small_zeros
//------------------------------------------------------------------------
// A simple test case that tests sorting an empty array. Just make sure
// it doesn't segfault or crash or anything.

void test_case_25_mult_small_zeros()
{
    ECE4750_CHECK( L"test_case_25_mult_five_element" );
    const int n = 3;
    const int m = 3;
    const int p = 3;
    const int min_val = 0;
    const int max_val = 0;
    int i = 0;

    // Allocate memory for the input matrices
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

    matrix_multiply(A, B, C, n, m, p);
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

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// test_case_4_mult_one_element
//------------------------------------------------------------------------
// A simple test case that tests sorting a one-element array.

void test_case_26_mult_one_element()
{
    ECE4750_CHECK( L"test_case_26_mult_one_element" );
    const int n = 1;
    const int m = 1;
    const int p = 1;
    const int min_val = 0;
    const int max_val = 5;
    int i = 0;

    // Allocate memory for the input matrices
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

    matrix_multiply(A, B, C, n, m, p);
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

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    //// ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
    // ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// test_case_5_mult_two_elements
//------------------------------------------------------------------------

void test_case_27_mult_two_elements()
{
    ECE4750_CHECK( L"test_case_27_mult_two_elements" );
    const int n = 2;
    const int m = 2;
    const int p = 2;
    const int min_val = 0;
    const int max_val = 5;
    int i = 0;

    // Allocate memory for the input matrices
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

    matrix_multiply(A, B, C, n, m, p);
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

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// test_case_6_mult_larger_matrix
//------------------------------------------------------------------------

void test_case_28_mult_larger_matrix()
{
    ECE4750_CHECK( L"test_case_28_mult_larger_matrix" );

    const int n = 10;
    const int m = 10;
    const int p = 10;
    const int min_val = 0;
    const int max_val = 5;
    int i = 0;

    // Allocate memory for the input matrices
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

    matrix_multiply(A, B, C, n, m, p);
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

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// test_case_7_mult_larger_matrix_larger_values
//------------------------------------------------------------------------

void test_case_29_mult_larger_matrix_larger_values()
{
    ECE4750_CHECK( L"test_case_29_mult_larger_matrix_larger_values" );

    const int n = 25;
    const int m = 25;
    const int p = 25;
    const int min_val = 0;
    const int max_val = 100;
    int i = 0;

    // Allocate memory for the input matrices
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

    matrix_multiply(A, B, C, n, m, p);
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

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// test_case_8_mult_max_size_small_values
//------------------------------------------------------------------------

void test_case_30_mult_max_size_small_values()
{
    ECE4750_CHECK( L"test_case_30_mult_max_size_small_values" );

    const int n = 32;
    const int m = 32;
    const int p = 32;
    const int min_val = 0;
    const int max_val = 5;
    int i = 0;

    // Allocate memory for the input matrices
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

    matrix_multiply(A, B, C, n, m, p);
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

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// test_case_9_few_unique
//------------------------------------------------------------------------

void test_case_31_mult_max_size_medium_values()
{
    ECE4750_CHECK( L"test_case_31_mult_max_size_medium_values" );

    const int n = 32;
    const int m = 32;
    const int p = 32;
    const int min_val = 0;
    const int max_val = 100;
    int i = 0;

    // Allocate memory for the input matrices
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

    matrix_multiply(A, B, C, n, m, p);
    //print_matrix(C, n, m);
    matrix_multiply(A, B, C_ref, n, m, p);
    //print_matrix(C_ref, n, m);

    // Verify the results
    int results = compare_matrices(C, C_ref, n, m); 
    if (results == 1) {
            ece4750_wprintf( L"Matrix multiplication test passed.\n");
    } else {
            ece4750_wprintf( L"Matrix multiplication test failed.\n");
    }

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// test_case_10_mult_max_size_large_values
//------------------------------------------------------------------------

void test_case_32_mult_max_size_large_values()
{
    ECE4750_CHECK( L"test_case_32_mult_max_size_large_values" );

    const int n = 32;
    const int m = 32;
    const int p = 32;
    const int min_val = 0;
    const int max_val = 1000;
    int i = 0;

    // Allocate memory for the input matrices
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

    matrix_multiply(A, B, C, n, m, p);
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

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// test_case_11_mult_max_size_very_large_values
//------------------------------------------------------------------------

void test_case_33_mult_max_size_very_large_values()
{
    ECE4750_CHECK( L"test_case_33_mult_max_size_very_large_values" );

    const int n = 32;
    const int m = 32;
    const int p = 32;
    const int min_val = 0;
    const int max_val = 100000;
    int i = 0;

    // Allocate memory for the input matrices
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

    matrix_multiply(A, B, C, n, m, p);
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

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}

//------------------------------------------------------------------------
// test_case_11_mult_max_size_even_larger_values
//------------------------------------------------------------------------

void test_case_34_mult_max_size_even_larger_values()
{
    ECE4750_CHECK( L"test_case_34_mult_max_size_even_larger_values" );

    const int n = 32;
    const int m = 32;
    const int p = 32;
    const int min_val = 0;
    const int max_val = 100000000;
    int i = 0;

    // Allocate memory for the input matrices
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

    matrix_multiply(A, B, C, n, m, p);
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

 //   ece4750_free(A);
 //   ece4750_free(B);
 //   ece4750_free(C);
 //   ece4750_free(C_ref);

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // Compare each element of matrices "C" and "C_ref"
    for (i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            // If an element of "C" is not equal to the corresponding element of "C_ref", return false
            ECE4750_CHECK_INT_EQ( C[i] , C_ref[i] );
        }
    }

    // ECE4750_CHECK_INT_EQ( ece4750_get_heap_usage(), 0 );
}


//''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''/

//------------------------------------------------------------------------
// main
//------------------------------------------------------------------------

int main( int argc, char** argv )
{
    __n = ( argc == 1 ) ? 0 : ece4750_atoi( argv[1] );

    //''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    // Directed Tests
    //'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    if ( (__n <= 0) || (__n == 1  ) ) test_case_1_mult_A11_B11();
    if ( (__n <= 0) || (__n == 2  ) ) test_case_2_mult_A11_B11_zero();
    if ( (__n <= 0) || (__n == 3  ) ) test_case_3_mult_A22_B22();
    if ( (__n <= 0) || (__n == 4  ) ) test_case_4_mult_A22_B22_zero();
    if ( (__n <= 0) || (__n == 5  ) ) test_case_5_mult_A33_B33();
    if ( (__n <= 0) || (__n == 6  ) ) test_case_6_mult_A33_B33_zero();
    if ( (__n <= 0) || (__n == 7  ) ) test_case_7_mult_A44_B44();
    if ( (__n <= 0) || (__n == 8  ) ) test_case_8_mult_A44_B44_zero();
    if ( (__n <= 0) || (__n == 9  ) ) test_case_9_mult_A55_B55();
    if ( (__n <= 0) || (__n == 10 ) ) test_case_10_mult_A55_B55_zero();
    if ( (__n <= 0) || (__n == 11 ) ) test_case_11_mult_A23_B32();
    if ( (__n <= 0) || (__n == 12 ) ) test_case_12_mult_A23_B32_zero();
    if ( (__n <= 0) || (__n == 13 ) ) test_case_13_mult_A33_B32();
    if ( (__n <= 0) || (__n == 14 ) ) test_case_14_mult_A33_B32_zero();
    if ( (__n <= 0) || (__n == 15 ) ) test_case_15_mult_A43_B35();
    if ( (__n <= 0) || (__n == 16 ) ) test_case_16_mult_A43_B35_zero();
    if ( (__n <= 0) || (__n == 17 ) ) test_case_17_mult_A43_B35();
    if ( (__n <= 0) || (__n == 18 ) ) test_case_18_mult_A43_B35_zeros();
    if ( (__n <= 0) || (__n == 19 ) ) test_case_19_mult_A51_B15();
    if ( (__n <= 0) || (__n == 20 ) ) test_case_20_mult_A51_B15_zero();
    if ( (__n <= 0) || (__n == 21 ) ) test_case_21_mult_A53_B31();
    if ( (__n <= 0) || (__n == 22 ) ) test_case_22_mult_A53_B31_zero();

    //''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    // Randomly Generated Matrix Values
    //''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    if ( (__n <= 0) || (__n == 23 ) ) test_case_23_mult_basic();
    if ( (__n <= 0) || (__n == 24 ) ) test_case_24_mult_five_element();
    if ( (__n <= 0) || (__n == 25 ) ) test_case_25_mult_small_zeros();
    if ( (__n <= 0) || (__n == 26 ) ) test_case_26_mult_one_element();
    if ( (__n <= 0) || (__n == 27 ) ) test_case_27_mult_two_elements();
    if ( (__n <= 0) || (__n == 28 ) ) test_case_28_mult_larger_matrix();
    if ( (__n <= 0) || (__n == 29 ) ) test_case_29_mult_larger_matrix_larger_values();
    if ( (__n <= 0) || (__n == 30 ) ) test_case_30_mult_max_size_small_values();
    if ( (__n <= 0) || (__n == 31 ) ) test_case_31_mult_max_size_medium_values();
    if ( (__n <= 0) || (__n == 32 ) ) test_case_32_mult_max_size_large_values();
    if ( (__n <= 0) || (__n == 33 ) ) test_case_33_mult_max_size_very_large_values();
    if ( (__n <= 0) || (__n == 34 ) ) test_case_34_mult_max_size_even_larger_values();

    //''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''//

    ece4750_wprintf( L"\n\n" );
    return ece4750_check_status;
}