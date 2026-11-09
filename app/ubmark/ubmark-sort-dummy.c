//========================================================================
// ubmark-sort-eval
//========================================================================

#include "ece4750.h"
#include "ubmark-sort.h"
#include "ubmark-sort.dat"

int main( void )
{
  // Run the evaluation

  ece4750_stats_on();
  // dummy to estimate energy outside function
  ece4750_stats_off();

  // Verify the results ... well not really because we know it won't
  // work, so we just count the number of mismatching elements and then
  // dislpay this count to avoid the compiler from optimizing away the
  // loop.

  int count = 0;
  for ( int i = 0; i < eval_size; i++ ) {
    if ( eval_src[i] != eval_ref[i] )
      count += 1;
  }

  // Check for no memory leaks

  if ( ece4750_get_heap_usage() != 0 ) {

    // We put the output here so that we don't _actually_ display the
    // count since that would result in a bunch of extra work that is not
    // in the baseline ...

    ece4750_wprintf( L"\n count = %d ", count );

    ece4750_wprintf( L"\n FAILED: memory leak of %d bytes!\n\n",
                     ece4750_get_heap_usage() );
    ece4750_exit(1);
  }

  // Otherwise we passed

  ece4750_wprintf( L"\n **PASSED** \n\n" );

  return 0;
}

