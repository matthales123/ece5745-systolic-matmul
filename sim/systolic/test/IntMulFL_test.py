#=========================================================================
# IntMulFL_test
#=========================================================================

import pytest

from random import randint

from pymtl3 import *
from pymtl3.stdlib.test_utils import mk_test_case_table, run_sim
from pymtl3.stdlib.stream import StreamSourceFL, StreamSinkFL

from systolic.IntMulFL import IntMulFL

#-------------------------------------------------------------------------
# TestHarness
#-------------------------------------------------------------------------

class TestHarness( Component ):

  def construct( s, imul ):

    # Instantiate models

    s.srcA  = StreamSourceFL( Bits32 )
    s.srcB  = StreamSourceFL( Bits32 )
    s.sink = StreamSinkFL( Bits32 )
    s.imul = imul

    # Connect

    s.srcA.ostream  //= s.imul.istreamA
    s.srcB.ostream  //= s.imul.istreamB
    s.imul.ostream //= s.sink.istream

  def done( s ):
    return s.srcA.done() and s.srcB.done() and s.sink.done()

  def line_trace( s ):
    return s.srcA.line_trace() + " > " + s.srcB.line_trace() + " > " + s.imul.line_trace() + " > " + s.sink.line_trace()

#-------------------------------------------------------------------------
# mk_imsg/mk_omsg
#-------------------------------------------------------------------------

# Make input message, truncate ints to ensure they fit in 32 bits.

def mk_imsg( a ):
  return concat( Bits32( a, trunc_int=True ))

def mk_imsg( b ):
  return concat( Bits32( b, trunc_int=True ) )


# Make output message, truncate ints to ensure they fit in 32 bits.

def mk_omsg( a ):
  return Bits32( a, trunc_int=True )

#----------------------------------------------------------------------
# Test Case: zero * positive/neg/zero
#----------------------------------------------------------------------

zero_num_msgs = [
  mk_imsg(  0), mk_imsg( -3 ), mk_omsg(   0 ),
  mk_imsg(  0), mk_imsg( -5 ), mk_omsg(  0 ),
  mk_imsg(  0), mk_imsg( -4 ), mk_omsg(  0 ),
  mk_imsg( 0 ), mk_imsg(13 ), mk_omsg( 0 ),
  mk_imsg(  0), mk_imsg(0 ), mk_omsg(  0 ),
]

#----------------------------------------------------------------------
# Test Case: small positive * positive
#----------------------------------------------------------------------

small_pos_pos_msgs = [
  
  mk_imsg(  1 ), mk_imsg(  3 ), mk_omsg( 3 ),
  mk_imsg(  3 ), mk_imsg(  9 ), mk_omsg( 27 ),
  # mk_imsg(  8 ), mk_imsg(  7 ), mk_omsg( 56 ),
  # mk_imsg(  6 ), mk_imsg(  5 ), mk_omsg( 30 ),
  # mk_imsg(  4 ), mk_imsg(  2 ), mk_omsg( 8 ),
]

# #----------------------------------------------------------------------
# # Test Case: small positive * negative
# #----------------------------------------------------------------------

small_pos_neg_msgs =  [
  
  mk_imsg(  1 ), mk_imsg(  -3 ), mk_omsg( -3 ),
  mk_imsg(  3 ), mk_imsg(  -9 ), mk_omsg( -27 ),
  mk_imsg(  8 ), mk_imsg(  -7 ), mk_omsg( -56 ),
  mk_imsg(  6 ), mk_imsg(  -5 ), mk_omsg( -30 ),
  mk_imsg(  4 ), mk_imsg(  -2 ), mk_omsg( -8 ),
]

# #----------------------------------------------------------------------
# # Test Case: small negative * positive
# #----------------------------------------------------------------------

small_neg_pos_msgs = [
  
  mk_imsg(  -1 ), mk_imsg(  3 ), mk_omsg( -3 ),
  mk_imsg(  -3 ), mk_imsg(  9 ), mk_omsg( -27 ),
  mk_imsg(  -8 ), mk_imsg(  7 ), mk_omsg( -56 ),
  mk_imsg(  -6 ), mk_imsg(  5 ), mk_omsg( -30 ),
  mk_imsg(  -4 ), mk_imsg(  2 ), mk_omsg( -8 ),
]

# #----------------------------------------------------------------------
# # Test Case: small negative * negative
# #----------------------------------------------------------------------

small_neg_neg_msgs = [
  
  mk_imsg(  -1 ), mk_imsg(  -3 ), mk_omsg( 3 ),
  mk_imsg(  -3 ), mk_imsg(  -9 ), mk_omsg( 27 ),
  mk_imsg(  -8 ), mk_imsg(  -7 ), mk_omsg( 56 ),
  mk_imsg(  -6 ), mk_imsg(  -5 ), mk_omsg( 30 ),
  mk_imsg(  -4 ), mk_imsg(  -2 ), mk_omsg( 8 ),
]

# #----------------------------------------------------------------------
# # Test Case: large positive * positive
# #----------------------------------------------------------------------

large_pos_pos_msgs = [
  mk_imsg(  234567890), mk_imsg( 234567890 ), mk_omsg(   3429403716 ),
  mk_imsg(  2147483647),mk_imsg(  2147483647 ), mk_omsg(  1 ),
  mk_imsg(  1234567),mk_imsg(  1234567 ), mk_omsg(  3737254705 ),
]

# #----------------------------------------------------------------------
# # Test Case: large positive * negative
# #----------------------------------------------------------------------

large_pos_neg_msgs = [
  mk_imsg(  234567890), mk_imsg( -234567890 ), mk_omsg(   -3429403716 ),
  mk_imsg(  2147483647),mk_imsg(  -2147483647 ), mk_omsg(  -1 ),
  mk_imsg(  1234567),mk_imsg(  -1234567 ), mk_omsg(  -3737254705 ),
]

# #----------------------------------------------------------------------
# # Test Case: large neg * positive
# #----------------------------------------------------------------------

large_neg_pos_msgs = [
  mk_imsg(  -234567890),  mk_imsg(234567890 ), mk_omsg(   -3429403716 ),
  mk_imsg(  -2147483647),  mk_imsg(2147483647 ), mk_omsg(  -1 ),
  mk_imsg(  -1234567),  mk_imsg(1234567 ), mk_omsg(  -3737254705 ),
]

# #----------------------------------------------------------------------
# # Test Case: large negative * negative
# #----------------------------------------------------------------------

large_neg_neg_msgs = [
  mk_imsg(  -234567890) ,  mk_imsg(-234567890 ), mk_omsg(   3429403716 ),
  mk_imsg(  -2147483647),  mk_imsg(-2147483647 ), mk_omsg(  1 ),
  mk_imsg(  -1234567)   ,  mk_imsg(-1234567 ), mk_omsg(  3737254705 ),
]

# #----------------------------------------------------------------------
# # Test Case: edge cases with zero sequences
# #----------------------------------------------------------------------

seq_zeroes = [
  mk_imsg(int('01100000', 2)), mk_imsg(int('00000100100', 2)), mk_omsg(3456), 
  mk_imsg(int('0000100001000011', 2)), mk_imsg(int('100000100100', 2)), mk_omsg(4407660),
  mk_imsg(int('0000000111111', 2)), mk_imsg(int('00000111111', 2)), mk_omsg(3969),
  mk_imsg(int('1010101010101', 2)), mk_imsg(int('1010101010101111', 2)), mk_omsg(238618395),
  mk_imsg(int('10000000000', 2)), mk_imsg(int('0000000001', 2)), mk_omsg(1024),

] 

#-------------------------------------------------------------------------
# Test Case Table
#-------------------------------------------------------------------------

test_case_table = mk_test_case_table([
  (                      "msgs                 src_delay sink_delay"),
  [ "small_pos_pos",            small_pos_pos_msgs,   0,        0          ],
  [ "small_pos_neg",           small_pos_neg_msgs,   0,        0          ],
  [ "small_neg_pos",           small_neg_pos_msgs,   0,        0          ],
  [ "small_neg_neg",           small_neg_neg_msgs,   0,        0          ],
  [ "large_pos_pos",           large_pos_pos_msgs,   0,        0          ],
  [ "large_pos_neg",           large_pos_neg_msgs,   0,        0          ],
  [ "large_neg_pos",           large_neg_pos_msgs,   0,        0          ],
  [ "large_neg_neg",           large_neg_neg_msgs,   0,        0          ],
  [ "zero_num",                zero_num_msgs,        0,        0          ], 
  ["seq_zeroes",               seq_zeroes,           0,       0          ], 
   [ "small_pos_pos_delay",    small_pos_pos_msgs,   20,       100          ],
  [ "small_pos_neg_delay",     small_pos_neg_msgs,   30,       40          ],
  [ "small_neg_pos_delay",     small_neg_pos_msgs,   50,       50          ],
  [ "small_neg_neg_delay",     small_neg_neg_msgs,   3,        10          ],
  [ "large_pos_pos_delay",     large_pos_pos_msgs,   24,       2          ],
  [ "large_pos_neg_delay",     large_pos_neg_msgs,   324,      12          ],
  [ "large_neg_pos_delay",     large_neg_pos_msgs,   14,       12          ],
  [ "large_neg_neg_delay",     large_neg_neg_msgs,   23,       123          ],
  [ "zero_num_delay",          zero_num_msgs,        34,       234          ], 
  [ "seq_zeroes_delay",        seq_zeroes,          2,       23         ], 


])

#-------------------------------------------------------------------------
# TestHarness
#-------------------------------------------------------------------------

@pytest.mark.parametrize( **test_case_table )
def test( test_params, cmdline_opts ):

  th = TestHarness( IntMulFL() )

  th.set_param("top.srcA.construct",
    msgs=test_params.msgs[::3],
    initial_delay=test_params.src_delay+3,
    interval_delay=test_params.src_delay )
  
  th.set_param("top.srcB.construct",
    msgs=test_params.msgs[1::3],
    initial_delay=test_params.src_delay+3,
    interval_delay=test_params.src_delay )

  th.set_param("top.sink.construct",
    msgs=test_params.msgs[2::3],
    initial_delay=test_params.sink_delay+3,
    interval_delay=test_params.sink_delay )

  run_sim( th, cmdline_opts, duts=['imul'] )

