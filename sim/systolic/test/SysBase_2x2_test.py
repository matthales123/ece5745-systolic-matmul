#=========================================================================
# Systolic test
#=========================================================================

import pytest

from random import randint

from pymtl3 import *
from pymtl3.stdlib.test_utils import mk_test_case_table, run_sim
from pymtl3.stdlib.stream import StreamSourceFL, StreamSinkFL

from systolic.SysBase import SysBase

#-------------------------------------------------------------------------
# TestHarness
#-------------------------------------------------------------------------

class TestHarness( Component ):

  def construct( s, pe ):

    # Instantiate models

    s.srcA0  = StreamSourceFL( Bits33 )
    s.srcB0  = StreamSourceFL( Bits33 ) 
    s.srcA1  = StreamSourceFL( Bits33 )
    s.srcB1  = StreamSourceFL( Bits33 )

    s.sinkA0 = StreamSinkFL  ( Bits33 ) 
    s.sinkB0 = StreamSinkFL  ( Bits33 )
    s.sinkA1 = StreamSinkFL  ( Bits33 ) 
    s.sinkB1 = StreamSinkFL  ( Bits33 )


    s.pe = pe

    # Connect

    s.srcA0.ostream  //= s.pe.istreamA[0]
    s.srcB0.ostream  //= s.pe.istreamB[0]
    s.srcA1.ostream  //= s.pe.istreamA[1]
    s.srcB1.ostream  //= s.pe.istreamB[1]
    # s.srcA2.ostream  //= s.systolic.istreamA2
    # s.srcB2.ostream  //= s.systolic.istreamB2

    s.pe.ostreamA[0]  //= s.sinkA0.istream
    s.pe.ostreamB[0]  //= s.sinkB0.istream
    s.pe.ostreamA[1]  //= s.sinkA1.istream
    s.pe.ostreamB[1]  //= s.sinkB1.istream
    # s.systolic.ostreamA2  //= s.sinkA2.istream
    # s.systolic.ostreamB2  //= s.sinkB2.istream
    
    # s.pe.give_result //= 0


  def done( s ):
    return s.srcA0.done() and s.srcB0.done() and s.srcA1.done() and s.srcB1.done() and s.sinkB0.done() and s.sinkA0.done() and s.sinkB1.done() and s.sinkA1.done()

  def line_trace( s ):
    return s.srcA0.line_trace() + " > " + s.srcB0.line_trace() + " > " + s.srcA1.line_trace() + " > " + s.srcB1.line_trace() + " > " + s.pe.line_trace() + " > " + s.sinkA0.line_trace() + " > " + s.sinkB0.line_trace() + " > " + s.sinkA1.line_trace() + " > " + s.sinkB1.line_trace()

#-------------------------------------------------------------------------
# mk_imsg/mk_omsg
#-------------------------------------------------------------------------

# Make input message, truncate ints to ensure they fit in 32 bits.

def mk_imsg( a, b ):
  return concat( Bits1( a ), Bits32( b, trunc_int=True ) )

# def mk_imsg( b ):
#   return concat( Bits32( b, trunc_int=True ) )


# Make output message, truncate ints to ensure they fit in 32 bits.

def mk_omsg( a, b ):
 return concat( Bits1( a ), Bits32( b, trunc_int=True ) )

#----------------------------------------------------------------------
# Test Case: small positive * positive for 2 PE's
#----------------------------------------------------------------------

small_pos_pos_2x2_1_msgs = [
  # inputs
  #                   A0                                   
  [mk_imsg(0,1),mk_imsg(0,2), mk_imsg(1,0), mk_imsg(1,0)], 
  
  #                       B0_in
  [ mk_imsg(0,10),mk_imsg(0,20), mk_imsg(1,0), mk_imsg(1,0)],

                          #  A1_in                                                                            B_In                                
  [mk_imsg(0,3),mk_imsg(0,4), mk_imsg(1,0), mk_imsg(1,0)],  
  
  #                           B1_in
  [ mk_imsg(0,30),mk_imsg(0,40), mk_imsg(1,0), mk_imsg(1,0)],
  
  # outputs
  #                   A0                                          B0
                          #  A_In                                B_In                                   
  [mk_omsg(0,1),mk_omsg(0,2), mk_omsg(1,0), mk_imsg(1,0)],  [ mk_omsg(0,10),mk_omsg(0,20), mk_omsg(1,110), mk_omsg(1,50)],
  #                   A1                                          B1
                          #  A_In                                B_In                                
  [mk_omsg(0,3),mk_omsg(0,4), mk_imsg(1,0), mk_imsg(1,0)],  [ mk_omsg(0,30),mk_omsg(0,40), mk_imsg(1,250), mk_imsg(1,110)]
  
  
]

small_pos_pos_2x2_2_msgs = [
  # inputs
  #                   A0                                   
  [mk_imsg(0,1),mk_imsg(0,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
  #                       B0_in
  [ mk_imsg(0,5),mk_imsg(0,0), mk_imsg(1,0), mk_imsg(1,0)],

                          #  A1_in                                                                            B_In                                
  [mk_imsg(0,3),mk_imsg(0,0), mk_imsg(1,0), mk_imsg(1,0)],  
  
  #                           B1_in
  [ mk_imsg(0,7),mk_imsg(0,0), mk_imsg(1,0), mk_imsg(1,0)],
  
  # outputs
  #                   A0                                          B0
                          #  A_In                                B_In                                   
  [mk_omsg(0,1),mk_omsg(0,0), mk_omsg(1,0), mk_imsg(1,0)],  [ mk_omsg(0,5),mk_omsg(0,0), mk_omsg(1,15), mk_omsg(1,5)],
  #                   A1                                          B1
                          #  A_In                                B_In                                
  [mk_omsg(0,3),mk_omsg(0,0), mk_imsg(1,0), mk_imsg(1,0)],  [ mk_omsg(0,7),mk_omsg(0,0), mk_imsg(1,21), mk_imsg(1,7)]
]



#-------------------------------------------------------------------------
# Test Case Table
#-------------------------------------------------------------------------

test_case_table = mk_test_case_table([
  (                               "msgs             src_delay sink_delay"),
  [ "small_pos_pos_2x2_1",       small_pos_pos_2x2_1_msgs,   0,        0        ],
  [ "small_pos_pos_2x2_2",       small_pos_pos_2x2_2_msgs,   0,        0        ]
])

#-------------------------------------------------------------------------
# TestHarness
#-------------------------------------------------------------------------

@pytest.mark.parametrize( **test_case_table )
def test( test_params, cmdline_opts ):

  th = TestHarness( SysBase( SIZE = 2 ) )

  th.set_param("top.srcA0.construct",
    msgs=test_params.msgs[0],
    # initial_delay=test_params.src_delay+3,
    interval_delay=0 )
  
  th.set_param("top.srcB0.construct",
    msgs=test_params.msgs[1],
    # initial_delay=test_params.src_delay+3,
    interval_delay=0 )
  
  th.set_param("top.srcA1.construct",
    msgs=test_params.msgs[2],
    # initial_delay=test_params.src_delay+3,
    interval_delay=0 )
  
  th.set_param("top.srcB1.construct",
    msgs=test_params.msgs[3],
    interval_delay=0 )

  
  th.set_param("top.sinkA0.construct",
    msgs=test_params.msgs[4],
    # initial_delay=test_params.sink_delay+3,
    interval_delay=test_params.sink_delay )
  
  th.set_param("top.sinkB0.construct",
    msgs=test_params.msgs[5],
    # initial_delay=test_params.sink_delay+3,
    interval_delay=test_params.sink_delay )
  
  th.set_param("top.sinkA1.construct",
    msgs=test_params.msgs[6],
    # initial_delay=test_params.sink_delay+3,
    interval_delay=test_params.sink_delay )
  
  th.set_param("top.sinkB1.construct",
    msgs=test_params.msgs[7],
    # initial_delay=test_params.sink_delay+3,
    interval_delay=test_params.sink_delay )
  run_sim( th, cmdline_opts, duts=['pe'] )

