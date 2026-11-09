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
    s.srcA2  = StreamSourceFL( Bits33 )
    s.srcB2  = StreamSourceFL( Bits33 )
    s.srcA3  = StreamSourceFL( Bits33 )
    s.srcB3  = StreamSourceFL( Bits33 )
    s.srcA4  = StreamSourceFL( Bits33 )
    s.srcB4  = StreamSourceFL( Bits33 )

    s.sinkA0 = StreamSinkFL  ( Bits33 ) 
    s.sinkB0 = StreamSinkFL  ( Bits33 )
    s.sinkA1 = StreamSinkFL  ( Bits33 ) 
    s.sinkB1 = StreamSinkFL  ( Bits33 )
    s.sinkA2 = StreamSinkFL  ( Bits33 ) 
    s.sinkB2 = StreamSinkFL  ( Bits33 )
    s.sinkA3 = StreamSinkFL  ( Bits33 ) 
    s.sinkB3 = StreamSinkFL  ( Bits33 )
    s.sinkA4 = StreamSinkFL  ( Bits33 ) 
    s.sinkB4 = StreamSinkFL  ( Bits33 )


    s.pe = pe

    # Connect

    s.srcA0.ostream  //= s.pe.istreamA[0]
    s.srcB0.ostream  //= s.pe.istreamB[0]
    s.srcA1.ostream  //= s.pe.istreamA[1]
    s.srcB1.ostream  //= s.pe.istreamB[1]
    s.srcA2.ostream  //= s.pe.istreamA[2]
    s.srcB2.ostream  //= s.pe.istreamB[2]
    s.srcA3.ostream  //= s.pe.istreamA[3]
    s.srcB3.ostream  //= s.pe.istreamB[3]
    s.srcA4.ostream  //= s.pe.istreamA[4]
    s.srcB4.ostream  //= s.pe.istreamB[4]

    s.pe.ostreamA[0]  //= s.sinkA0.istream
    s.pe.ostreamB[0]  //= s.sinkB0.istream
    s.pe.ostreamA[1]  //= s.sinkA1.istream
    s.pe.ostreamB[1]  //= s.sinkB1.istream
    s.pe.ostreamA[2]  //= s.sinkA2.istream
    s.pe.ostreamB[2]  //= s.sinkB2.istream
    s.pe.ostreamA[3]  //= s.sinkA3.istream
    s.pe.ostreamB[3]  //= s.sinkB3.istream
    s.pe.ostreamA[4]  //= s.sinkA4.istream
    s.pe.ostreamB[4]  //= s.sinkB4.istream
    
    # s.pe.give_result //= 0


  def done( s ):
    return s.srcA0.done() and s.srcB0.done() and s.srcA1.done() and s.srcB1.done() and s.srcA2.done() and s.srcB2.done() and s.srcA3.done() and s.srcB3.done() and s.sinkB0.done() and s.sinkA0.done() and s.sinkB1.done() and s.sinkA1.done() and s.sinkB2.done() and s.sinkA2.done() and s.sinkB3.done() and s.sinkA3.done() and s.sinkB4.done() and s.sinkA4.done()

  def line_trace( s ):
    return s.srcA0.line_trace() + " > " + s.srcB0.line_trace() + " > " + s.srcA1.line_trace() + " > " + s.srcB1.line_trace() + " > " + s.srcA2.line_trace() + " > " + s.srcB2.line_trace() + " > " + s.srcA3.line_trace() + " > " + s.srcB3.line_trace() + " > " + s.srcA4.line_trace() + " > " + s.srcB4.line_trace() + " > " + s.pe.line_trace() + " > " + s.sinkA0.line_trace() + " > " + s.sinkB0.line_trace() + " > " + s.sinkA1.line_trace() + " > "  + s.sinkB1.line_trace() + " > " + s.sinkA2.line_trace() + " > " + s.sinkB2.line_trace() + " > " + s.sinkA3.line_trace() + " > " + s.sinkB3.line_trace() + " > " + s.sinkA4.line_trace() + " > " + s.sinkB4.line_trace()

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


small_pos_pos_5x5_1_msgs = [
  #=========================================================================
  # inputs
  #=========================================================================
  #                   A0_in                                   
  [mk_imsg(0,1),mk_imsg(0,2), mk_imsg(0,3), mk_imsg(0,4), mk_imsg(0,5), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
  #                       B0_in
  [ mk_imsg(0,1),mk_imsg(0,2), mk_imsg(0,3), mk_imsg(0,4), mk_imsg(0,5), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)],
  
    #                       A1_in
  [ mk_imsg(0,6),mk_imsg(0,7), mk_imsg(0,8), mk_imsg(0,9), mk_imsg(0,10), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)],
  
    #                           B1_in
  [ mk_imsg(0,6),mk_imsg(0,7), mk_imsg(0,8), mk_imsg(0,9), mk_imsg(0,10), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)],
  
                          #  A2_in                                           
  [mk_imsg(0,11),mk_imsg(0,12), mk_imsg(0,13), mk_imsg(0,14), mk_imsg(0,15), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)],  
  
  #                           B2_in
  [mk_imsg(0,11),mk_imsg(0,12), mk_imsg(0,13), mk_imsg(0,14), mk_imsg(0,15), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)],  
  
                            #  A3_in                                           
  [mk_imsg(0,16),mk_imsg(0,17), mk_imsg(0,18), mk_imsg(0,19), mk_imsg(0,20), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)],  
  
  #                           B3_in
  [mk_imsg(0,16),mk_imsg(0,17), mk_imsg(0,18), mk_imsg(0,19), mk_imsg(0,20), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)],  
  
                              #  A4_in                                           
  [mk_imsg(0,21),mk_imsg(0,22), mk_imsg(0,23), mk_imsg(0,24), mk_imsg(0,25), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)],  
  
  #                           B4_in
  [mk_imsg(0,21),mk_imsg(0,22), mk_imsg(0,23), mk_imsg(0,24), mk_imsg(0,25), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)],  
  
  #=========================================================================
  # outputs
  #=========================================================================
  #                          A0_out                                               
  [mk_omsg(0,1),mk_omsg(0,2), mk_omsg(0,3), mk_omsg(0,4), mk_imsg(0,5), mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)],  
  
    #                        B0_out
  [mk_omsg(0,1),mk_omsg(0,2), mk_omsg(0,3), mk_omsg(0,4), mk_imsg(0,5), mk_imsg(1,355), mk_omsg(1,280), mk_omsg(1,205), mk_omsg(1,130), mk_omsg(1,55)],  

                          #  A1_out                                      
  [mk_omsg(0,6),mk_omsg(0,7), mk_omsg(0,8), mk_omsg(0,9), mk_imsg(0,10), mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)], 
  
                            # B1_out     
  [mk_omsg(0,6),mk_omsg(0,7), mk_omsg(0,8), mk_omsg(0,9), mk_imsg(0,10), mk_imsg(1,930), mk_omsg(1,730), mk_omsg(1,530), mk_omsg(1,330), mk_omsg(1,130)], 
  
                           #  A2_out                                                 
  [mk_omsg(0,11),mk_omsg(0,12), mk_omsg(0,13), mk_omsg(0,14), mk_imsg(0,15), mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)],  
  
  #                           B2_out             
  [mk_omsg(0,11),mk_omsg(0,12), mk_omsg(0,13), mk_omsg(0,14), mk_imsg(0,15), mk_imsg(1,1505), mk_omsg(1,1180), mk_omsg(1,855), mk_omsg(1,530), mk_omsg(1,205)],  
  
                           #  A3_out                                                 
  [mk_omsg(0,16),mk_omsg(0,17), mk_omsg(0,18), mk_omsg(0,19), mk_imsg(0,20), mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)],  
  
  #                           B3_out             
  [mk_omsg(0,16),mk_omsg(0,17), mk_omsg(0,18), mk_omsg(0,19), mk_imsg(0,20), mk_imsg(1,2080), mk_omsg(1,1630), mk_omsg(1,1180), mk_omsg(1,730), mk_omsg(1,280)],  
  
                           #  A4_out                                                 
  [mk_omsg(0,21),mk_omsg(0,22), mk_omsg(0,23), mk_omsg(0,24), mk_imsg(0,25), mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)],  
  
  #                           B4_out             
  [mk_omsg(0,21),mk_omsg(0,22), mk_omsg(0,23), mk_omsg(0,24), mk_imsg(0,25), mk_imsg(1,2655), mk_omsg(1,2080), mk_omsg(1,1505), mk_omsg(1,930), mk_omsg(1,355)],  
]

#-------------------------------------------------------------------------
# Test Case Table
#-------------------------------------------------------------------------

test_case_table = mk_test_case_table([
  (                               "msgs                     src_delay  sinkA0_delay  sinkB0_delay   sinkA1_delay   sinkB1_delay  sinkA2_delay  sinkB2_delay sinkA3_delay  sinkB3_delay  sinkA4_delay  sinkB4_delay           "),
  [ "small_pos_pos_5x5_1",        small_pos_pos_5x5_1_msgs,      0,         0,           0,              0,             0,              0,           0,             0,           0,              0,           0               ],
  [ "small_pos_pos_5x5_1_delay1", small_pos_pos_5x5_1_msgs,      0,         1,           0,              0,             0,              0,           0,             0,           0,              0,           0               ],
  [ "small_pos_pos_5x5_1_delay2", small_pos_pos_5x5_1_msgs,      0,         0,           1,              0,             0,              0,           0,             0,           0,              0,           0               ],
  [ "small_pos_pos_5x5_1_delay3", small_pos_pos_5x5_1_msgs,      0,         0,           0,              1,             0,              0,           0,             0,           0,              0,           0               ],
  [ "small_pos_pos_5x5_1_delay4", small_pos_pos_5x5_1_msgs,      0,         0,           0,              0,             1,              0,           0,             0,           0,              0,           0               ],
  [ "small_pos_pos_5x5_1_delay5", small_pos_pos_5x5_1_msgs,      0,         0,           0,              0,             0,              1,           0,             0,           0,              0,           0               ],
  [ "small_pos_pos_5x5_1_delay6", small_pos_pos_5x5_1_msgs,      0,         0,           0,              0,             0,              0,           1,             0,           0,              0,           0               ],
  [ "small_pos_pos_5x5_1_delay7", small_pos_pos_5x5_1_msgs,      0,         4,           2,              0,             0,              0,           0,             0,           0,              0,           0               ],
  [ "small_pos_pos_5x5_1_delay8", small_pos_pos_5x5_1_msgs,      0,         0,           0,              4,             2,              0,           0,             0,           0,              0,           0               ],
  [ "small_pos_pos_5x5_1_delay9", small_pos_pos_5x5_1_msgs,      0,         0,           0,              0,             0,              4,           2,             0,           0,              0,           0               ],
])

#-------------------------------------------------------------------------
# TestHarness
#-------------------------------------------------------------------------

@pytest.mark.parametrize( **test_case_table )
def test( test_params, cmdline_opts ):

  th = TestHarness( SysBase( SIZE = 5 ) )

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
  
  th.set_param("top.srcA2.construct",
    msgs=test_params.msgs[4],
    # initial_delay=test_params.src_delay+3,
    interval_delay=0 )
  
  th.set_param("top.srcB2.construct",
    msgs=test_params.msgs[5],
    interval_delay=0 )
  
  th.set_param("top.srcA3.construct",
    msgs=test_params.msgs[6],
    interval_delay=0 )
    
  th.set_param("top.srcB3.construct",
    msgs=test_params.msgs[7],
    interval_delay=0 )
  
  th.set_param("top.srcA4.construct",
    msgs=test_params.msgs[8],
    interval_delay=0 )
    
  th.set_param("top.srcB4.construct",
    msgs=test_params.msgs[9],
    interval_delay=0 )

  
  th.set_param("top.sinkA0.construct",
    msgs=test_params.msgs[10],
    initial_delay=test_params.sinkA0_delay+3,
    interval_delay=test_params.sinkA0_delay )
  
  th.set_param("top.sinkB0.construct",
    msgs=test_params.msgs[11],
    initial_delay=test_params.sinkB0_delay+3,
    interval_delay=test_params.sinkB0_delay )
  
  th.set_param("top.sinkA1.construct",
    msgs=test_params.msgs[12],
    initial_delay=test_params.sinkA1_delay+3,
    interval_delay=test_params.sinkA1_delay )
  
  th.set_param("top.sinkB1.construct",
    msgs=test_params.msgs[13],
    initial_delay=test_params.sinkB1_delay+3,
    interval_delay=test_params.sinkB1_delay )
  
  th.set_param("top.sinkA2.construct",
    msgs=test_params.msgs[14],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  th.set_param("top.sinkB2.construct",
    msgs=test_params.msgs[15],
    initial_delay=test_params.sinkB2_delay+3,
    interval_delay=test_params.sinkB2_delay )
  
  th.set_param("top.sinkA3.construct",
    msgs=test_params.msgs[16],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  th.set_param("top.sinkB3.construct",
    msgs=test_params.msgs[17],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  th.set_param("top.sinkA4.construct",
    msgs=test_params.msgs[18],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  th.set_param("top.sinkB4.construct",
    msgs=test_params.msgs[19],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  
  run_sim( th, cmdline_opts, duts=['pe'] )

