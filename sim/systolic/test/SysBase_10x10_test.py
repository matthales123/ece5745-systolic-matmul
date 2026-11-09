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
    s.srcA5  = StreamSourceFL( Bits33 )
    s.srcB5  = StreamSourceFL( Bits33 ) 
    s.srcA6  = StreamSourceFL( Bits33 )
    s.srcB6  = StreamSourceFL( Bits33 )
    s.srcA7  = StreamSourceFL( Bits33 )
    s.srcB7  = StreamSourceFL( Bits33 )
    s.srcA8  = StreamSourceFL( Bits33 )
    s.srcB8  = StreamSourceFL( Bits33 )
    s.srcA9  = StreamSourceFL( Bits33 )
    s.srcB9  = StreamSourceFL( Bits33 )

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
    s.sinkA5 = StreamSinkFL  ( Bits33 ) 
    s.sinkB5 = StreamSinkFL  ( Bits33 )
    s.sinkA6 = StreamSinkFL  ( Bits33 ) 
    s.sinkB6 = StreamSinkFL  ( Bits33 )
    s.sinkA7 = StreamSinkFL  ( Bits33 ) 
    s.sinkB7 = StreamSinkFL  ( Bits33 )
    s.sinkA8 = StreamSinkFL  ( Bits33 ) 
    s.sinkB8 = StreamSinkFL  ( Bits33 )
    s.sinkA9 = StreamSinkFL  ( Bits33 ) 
    s.sinkB9 = StreamSinkFL  ( Bits33 )


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
    s.srcA5.ostream  //= s.pe.istreamA[5]
    s.srcB5.ostream  //= s.pe.istreamB[5]
    s.srcA6.ostream  //= s.pe.istreamA[6]
    s.srcB6.ostream  //= s.pe.istreamB[6]
    s.srcA7.ostream  //= s.pe.istreamA[7]
    s.srcB7.ostream  //= s.pe.istreamB[7]
    s.srcA8.ostream  //= s.pe.istreamA[8]
    s.srcB8.ostream  //= s.pe.istreamB[8]
    s.srcA9.ostream  //= s.pe.istreamA[9]
    s.srcB9.ostream  //= s.pe.istreamB[9]

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
    s.pe.ostreamA[5]  //= s.sinkA5.istream
    s.pe.ostreamB[5]  //= s.sinkB5.istream
    s.pe.ostreamA[6]  //= s.sinkA6.istream
    s.pe.ostreamB[6]  //= s.sinkB6.istream
    s.pe.ostreamA[7]  //= s.sinkA7.istream
    s.pe.ostreamB[7]  //= s.sinkB7.istream
    s.pe.ostreamA[8]  //= s.sinkA8.istream
    s.pe.ostreamB[8]  //= s.sinkB8.istream
    s.pe.ostreamA[9]  //= s.sinkA9.istream
    s.pe.ostreamB[9]  //= s.sinkB9.istream
    
    # s.pe.give_result //= 0


  def done( s ):
    return s.srcA0.done() and s.srcB0.done() and s.srcA1.done() and s.srcB1.done() and s.srcA2.done() and s.srcB2.done() and s.srcA3.done() and s.srcB3.done() and s.srcA4.done() and s.srcB4.done() and s.srcA5.done() and s.srcB5.done() and s.srcA6.done() and s.srcB6.done() and s.srcA7.done() and s.srcB7.done() and s.srcA8.done() and s.srcB8.done() and s.srcA9.done() and s.srcB9.done() and s.sinkB0.done() and s.sinkA0.done() and s.sinkB1.done() and s.sinkA1.done() and s.sinkB2.done() and s.sinkA2.done() and s.sinkB3.done() and s.sinkA3.done() and s.sinkB4.done() and s.sinkA4.done() and s.sinkB5.done() and s.sinkA5.done() and s.sinkB6.done() and s.sinkA6.done() and s.sinkB7.done() and s.sinkA7.done() and s.sinkB8.done() and s.sinkA8.done() and s.sinkB9.done() and s.sinkA9.done()

  def line_trace( s ):
    return s.srcA0.line_trace() + " > " + s.srcB0.line_trace() + " > " + s.srcA1.line_trace() + " > " + s.srcB1.line_trace() + " > " + s.srcA2.line_trace() + " > " + s.srcB2.line_trace() + " > " + s.srcA3.line_trace() + " > " + s.srcB3.line_trace() + " > " + s.srcA4.line_trace() + " > " + s.srcB4.line_trace() + " > " + s.srcA5.line_trace() + " > " + s.srcB5.line_trace() + " > " + s.srcA6.line_trace() + " > " + s.srcB6.line_trace()+ " > " + s.srcA7.line_trace() + " > " + s.srcB7.line_trace() + " > " + s.srcA8.line_trace() + " > " + s.srcB8.line_trace() + " > " + s.srcA9.line_trace() + " > " + s.srcB9.line_trace() + " > " + s.pe.line_trace() + " > " + s.sinkA0.line_trace() + " > " + s.sinkB0.line_trace() + " > " + s.sinkA1.line_trace() + " > "  + s.sinkB1.line_trace() + " > " + s.sinkA2.line_trace() + " > " + s.sinkB2.line_trace() + " > " + s.sinkA3.line_trace() + " > " + s.sinkB3.line_trace() + " > " + s.sinkA4.line_trace() + " > " + s.sinkB4.line_trace() + " > " + s.sinkA5.line_trace() + " > " + s.sinkB5.line_trace()  + " > " + s.sinkA6.line_trace() + " > " + s.sinkB6.line_trace()  + " > " + s.sinkA7.line_trace() + " > " + s.sinkB7.line_trace() + " > " + s.sinkA8.line_trace() + " > " + s.sinkB8.line_trace()  + " > " + s.sinkA9.line_trace() + " > " + s.sinkB9.line_trace()

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
# Test Case: small positive * positive for 10 PE's
#----------------------------------------------------------------------


small_pos_pos_10x10_1_msgs = [
  #=========================================================================
  # inputs
  #=========================================================================
  #                   A0_in                                   
  [mk_imsg(0,1),mk_imsg(0,2), mk_imsg(0,3), mk_imsg(0,4), mk_imsg(0,5), mk_imsg(0,6),mk_imsg(0,7), mk_imsg(0,8), mk_imsg(0,9), mk_imsg(0,10), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
  #                       B0_in
  [mk_imsg(0,1),mk_imsg(0,2), mk_imsg(0,3), mk_imsg(0,4), mk_imsg(0,5), mk_imsg(0,6),mk_imsg(0,7), mk_imsg(0,8), mk_imsg(0,9), mk_imsg(0,10), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
    #                       A1_in
  [mk_imsg(0,11),mk_imsg(0,12), mk_imsg(0,13), mk_imsg(0,14), mk_imsg(0,15), mk_imsg(0,16),mk_imsg(0,17), mk_imsg(0,18), mk_imsg(0,19), mk_imsg(0,20), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
    #                           B1_in
  [mk_imsg(0,11),mk_imsg(0,12), mk_imsg(0,13), mk_imsg(0,14), mk_imsg(0,15), mk_imsg(0,16),mk_imsg(0,17), mk_imsg(0,18), mk_imsg(0,19), mk_imsg(0,20), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
                          #  A2_in                                           
  [mk_imsg(0,21),mk_imsg(0,22), mk_imsg(0,23), mk_imsg(0,24), mk_imsg(0,25), mk_imsg(0,26),mk_imsg(0,27), mk_imsg(0,28), mk_imsg(0,29), mk_imsg(0,30), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
  #                           B2_in
  [mk_imsg(0,21),mk_imsg(0,22), mk_imsg(0,23), mk_imsg(0,24), mk_imsg(0,25), mk_imsg(0,26),mk_imsg(0,27), mk_imsg(0,28), mk_imsg(0,29), mk_imsg(0,30), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
                            #  A3_in                                           
  [mk_imsg(0,31),mk_imsg(0,32), mk_imsg(0,33), mk_imsg(0,34), mk_imsg(0,35), mk_imsg(0,36),mk_imsg(0,37), mk_imsg(0,38), mk_imsg(0,39), mk_imsg(0,40), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
  #                           B3_in
  [mk_imsg(0,31),mk_imsg(0,32), mk_imsg(0,33), mk_imsg(0,34), mk_imsg(0,35), mk_imsg(0,36),mk_imsg(0,37), mk_imsg(0,38), mk_imsg(0,39), mk_imsg(0,40), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
                              #  A4_in                                           
  [mk_imsg(0,41),mk_imsg(0,42), mk_imsg(0,43), mk_imsg(0,44), mk_imsg(0,45), mk_imsg(0,46),mk_imsg(0,47), mk_imsg(0,48), mk_imsg(0,49), mk_imsg(0,50), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
  #                           B4_in
  [mk_imsg(0,41),mk_imsg(0,42), mk_imsg(0,43), mk_imsg(0,44), mk_imsg(0,45), mk_imsg(0,46),mk_imsg(0,47), mk_imsg(0,48), mk_imsg(0,49), mk_imsg(0,50), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
  #                   A5_in                                   
  [mk_imsg(0,51),mk_imsg(0,52), mk_imsg(0,53), mk_imsg(0,54), mk_imsg(0,55), mk_imsg(0,56),mk_imsg(0,57), mk_imsg(0,58), mk_imsg(0,59), mk_imsg(0,60), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
  #                       B5_in
  [mk_imsg(0,51),mk_imsg(0,52), mk_imsg(0,53), mk_imsg(0,54), mk_imsg(0,55), mk_imsg(0,56),mk_imsg(0,57), mk_imsg(0,58), mk_imsg(0,59), mk_imsg(0,60), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
    #                       A6_in
  [mk_imsg(0,61),mk_imsg(0,62), mk_imsg(0,63), mk_imsg(0,64), mk_imsg(0,65), mk_imsg(0,66),mk_imsg(0,67), mk_imsg(0,68), mk_imsg(0,69), mk_imsg(0,70), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
    #                           B6_in
  [mk_imsg(0,61),mk_imsg(0,62), mk_imsg(0,63), mk_imsg(0,64), mk_imsg(0,65), mk_imsg(0,66),mk_imsg(0,67), mk_imsg(0,68), mk_imsg(0,69), mk_imsg(0,70), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
                          #  A7_in                                           
  [mk_imsg(0,71),mk_imsg(0,72), mk_imsg(0,73), mk_imsg(0,74), mk_imsg(0,75), mk_imsg(0,76),mk_imsg(0,77), mk_imsg(0,78), mk_imsg(0,79), mk_imsg(0,80), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
  #                           B7_in
  [mk_imsg(0,71),mk_imsg(0,72), mk_imsg(0,73), mk_imsg(0,74), mk_imsg(0,75), mk_imsg(0,76),mk_imsg(0,77), mk_imsg(0,78), mk_imsg(0,79), mk_imsg(0,80), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
                            #  A8_in                                           
  [mk_imsg(0,81),mk_imsg(0,82), mk_imsg(0,83), mk_imsg(0,84), mk_imsg(0,85), mk_imsg(0,86),mk_imsg(0,87), mk_imsg(0,88), mk_imsg(0,89), mk_imsg(0,90), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
  #                           B8_in
  [mk_imsg(0,81),mk_imsg(0,82), mk_imsg(0,83), mk_imsg(0,84), mk_imsg(0,85), mk_imsg(0,86),mk_imsg(0,87), mk_imsg(0,88), mk_imsg(0,89), mk_imsg(0,90), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
                              #  A9_in                                           
  [mk_imsg(0,91),mk_imsg(0,92), mk_imsg(0,93), mk_imsg(0,94), mk_imsg(0,95), mk_imsg(0,96),mk_imsg(0,97), mk_imsg(0,98), mk_imsg(0,99), mk_imsg(0,100), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
  #                           B9_in
  [mk_imsg(0,91),mk_imsg(0,92), mk_imsg(0,93), mk_imsg(0,94), mk_imsg(0,95), mk_imsg(0,96),mk_imsg(0,97), mk_imsg(0,98), mk_imsg(0,99), mk_imsg(0,100), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0),mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)], 
  
  #=========================================================================
  # outputs
  #=========================================================================
  #                          A0_out                                               
  [mk_omsg(0,1),mk_omsg(0,2), mk_omsg(0,3), mk_omsg(0,4), mk_imsg(0,5), mk_omsg(0,6),mk_omsg(0,7), mk_omsg(0,8), mk_omsg(0,9), mk_imsg(0,10), mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0),mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)],  
  
    #                        B0_out
  [mk_omsg(0,1),mk_omsg(0,2), mk_omsg(0,3), mk_omsg(0,4), mk_imsg(0,5), mk_omsg(0,6),mk_omsg(0,7), mk_omsg(0,8), mk_omsg(0,9), mk_imsg(0,10), mk_imsg(1,5335), mk_omsg(1,4785), mk_omsg(1,4235), mk_omsg(1,3685), mk_omsg(1,3135), mk_imsg(1,2585), mk_omsg(1,2035), mk_omsg(1,1485), mk_omsg(1,935), mk_omsg(1,385)],  

                          #  A1_out                                      
  [mk_omsg(0,11),mk_omsg(0,12), mk_omsg(0,13), mk_omsg(0,14), mk_imsg(0,15), mk_omsg(0,16),mk_omsg(0,17), mk_omsg(0,18), mk_omsg(0,19), mk_imsg(0,20), mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0),mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)],  
  
                            # B1_out     
  [mk_omsg(0,11),mk_omsg(0,12), mk_omsg(0,13), mk_omsg(0,14), mk_imsg(0,15), mk_omsg(0,16),mk_omsg(0,17), mk_omsg(0,18), mk_omsg(0,19), mk_imsg(0,20), mk_imsg(1,14885), mk_omsg(1,13335), mk_omsg(1,11785), mk_omsg(1,10235), mk_omsg(1,8685), mk_imsg(1,7135), mk_omsg(1,5585), mk_omsg(1,4035), mk_omsg(1,2485), mk_omsg(1,935)],  
  
                           #  A2_out                                                 
  [mk_omsg(0,21),mk_omsg(0,22), mk_omsg(0,23), mk_omsg(0,24), mk_imsg(0,25), mk_omsg(0,26),mk_omsg(0,27), mk_omsg(0,28), mk_omsg(0,29), mk_imsg(0,30), mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0),mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)],  
  
  #                           B2_out             
  [mk_omsg(0,21),mk_omsg(0,22), mk_omsg(0,23), mk_omsg(0,24), mk_imsg(0,25), mk_omsg(0,26),mk_omsg(0,27), mk_omsg(0,28), mk_omsg(0,29), mk_imsg(0,30), mk_imsg(1,24435), mk_omsg(1,21885), mk_omsg(1,19335), mk_omsg(1,16785), mk_omsg(1,14235), mk_imsg(1,11685), mk_omsg(1,9135), mk_omsg(1,6585), mk_omsg(1,4035), mk_omsg(1,1485)],    
  
                           #  A3_out                                                 
  [mk_omsg(0,31),mk_omsg(0,32), mk_omsg(0,33), mk_omsg(0,34), mk_imsg(0,35), mk_omsg(0,36),mk_omsg(0,37), mk_omsg(0,38), mk_omsg(0,39), mk_imsg(0,40), mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0),mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)],   
  
  #                           B3_out             
  [mk_omsg(0,31),mk_omsg(0,32), mk_omsg(0,33), mk_omsg(0,34), mk_imsg(0,35), mk_omsg(0,36),mk_omsg(0,37), mk_omsg(0,38), mk_omsg(0,39), mk_imsg(0,40), mk_imsg(1,33985), mk_omsg(1,30435), mk_omsg(1,26885), mk_omsg(1,23335), mk_omsg(1,19785), mk_imsg(1,16235), mk_omsg(1,12685), mk_omsg(1,9135), mk_omsg(1,5585), mk_omsg(1,2035)],   
  
                           #  A4_out                                                 
  [mk_omsg(0,41),mk_omsg(0,42), mk_omsg(0,43), mk_omsg(0,44), mk_imsg(0,45), mk_omsg(0,46),mk_omsg(0,47), mk_omsg(0,48), mk_omsg(0,49), mk_imsg(0,50), mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0),mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)],   
  
  #                           B4_out             
  [mk_omsg(0,41),mk_omsg(0,42), mk_omsg(0,43), mk_omsg(0,44), mk_imsg(0,45), mk_omsg(0,46),mk_omsg(0,47), mk_omsg(0,48), mk_omsg(0,49), mk_imsg(0,50),mk_imsg(1,43535), mk_omsg(1,38985), mk_omsg(1,34435), mk_omsg(1,29885), mk_omsg(1,25335), mk_imsg(1,20785), mk_omsg(1,16235), mk_omsg(1,11685), mk_omsg(1,7135), mk_omsg(1,2585)],   
   
   #                          A0_out                                               
  [mk_omsg(0,51),mk_omsg(0,52), mk_omsg(0,53), mk_omsg(0,54), mk_imsg(0,55), mk_omsg(0,56),mk_omsg(0,57), mk_omsg(0,58), mk_omsg(0,59), mk_imsg(0,60), mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0),mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)],  
  
    #                        B5_out
  [mk_omsg(0,51),mk_omsg(0,52), mk_omsg(0,53), mk_omsg(0,54), mk_imsg(0,55), mk_omsg(0,56),mk_omsg(0,57), mk_omsg(0,58), mk_omsg(0,59), mk_imsg(0,60), mk_imsg(1,53085), mk_omsg(1,47535), mk_omsg(1,41985), mk_omsg(1,36435), mk_omsg(1,30885), mk_imsg(1,25335), mk_omsg(1,19785), mk_omsg(1,14235), mk_omsg(1,8685), mk_omsg(1,3135)],   

                          #  A6_out                                      
  [mk_omsg(0,61),mk_omsg(0,62), mk_omsg(0,63), mk_omsg(0,64), mk_imsg(0,65), mk_omsg(0,66),mk_omsg(0,67), mk_omsg(0,68), mk_omsg(0,69), mk_imsg(0,70), mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0),mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)],  
  
                            # B6_out     
  [mk_omsg(0,61),mk_omsg(0,62), mk_omsg(0,63), mk_omsg(0,64), mk_imsg(0,65), mk_omsg(0,66),mk_omsg(0,67), mk_omsg(0,68), mk_omsg(0,69), mk_imsg(0,70), mk_imsg(1,62635), mk_omsg(1,56085), mk_omsg(1,49535), mk_omsg(1,42985), mk_omsg(1,36435), mk_imsg(1,29885), mk_omsg(1,23335), mk_omsg(1,16785), mk_omsg(1,10235), mk_omsg(1,3685)],  
  
                           #  A7_out                                                 
  [mk_omsg(0,71),mk_omsg(0,72), mk_omsg(0,73), mk_omsg(0,74), mk_imsg(0,75), mk_omsg(0,76),mk_omsg(0,77), mk_omsg(0,78), mk_omsg(0,79), mk_imsg(0,80), mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0),mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)],  
  
  #                           B7_out             
  [mk_omsg(0,71),mk_omsg(0,72), mk_omsg(0,73), mk_omsg(0,74), mk_imsg(0,75), mk_omsg(0,76),mk_omsg(0,77), mk_omsg(0,78), mk_omsg(0,79), mk_imsg(0,80), mk_imsg(1,72185), mk_omsg(1,64635), mk_omsg(1,57085), mk_omsg(1,49535), mk_omsg(1,41985), mk_imsg(1,34435), mk_omsg(1,26885), mk_omsg(1,19335), mk_omsg(1,11785), mk_omsg(1,4235)],   
  
                           #  A8_out                                                 
  [mk_omsg(0,81),mk_omsg(0,82), mk_omsg(0,83), mk_omsg(0,84), mk_imsg(0,85), mk_omsg(0,86),mk_omsg(0,87), mk_omsg(0,88), mk_omsg(0,89), mk_imsg(0,90), mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0),mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)],   
  
  #                           B8_out             
  [mk_omsg(0,81),mk_omsg(0,82), mk_omsg(0,83), mk_omsg(0,84), mk_imsg(0,85), mk_omsg(0,86),mk_omsg(0,87), mk_omsg(0,88), mk_omsg(0,89), mk_imsg(0,90), mk_imsg(1,81735), mk_omsg(1,73185), mk_omsg(1,64635), mk_omsg(1,56085), mk_omsg(1,47535), mk_imsg(1,38985), mk_omsg(1,30435), mk_omsg(1,21885), mk_omsg(1,13335), mk_omsg(1,4785)],    
  
                           #  A9_out                                                 
  [mk_omsg(0,91),mk_omsg(0,92), mk_omsg(0,93), mk_omsg(0,94), mk_imsg(0,95), mk_omsg(0,96),mk_omsg(0,97), mk_omsg(0,98), mk_omsg(0,99), mk_imsg(0,100), mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0),mk_imsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)],   
  
  #                           B9_out             
  [mk_omsg(0,91),mk_omsg(0,92), mk_omsg(0,93), mk_omsg(0,94), mk_imsg(0,95), mk_omsg(0,96),mk_omsg(0,97), mk_omsg(0,98), mk_omsg(0,99), mk_imsg(0,100), mk_imsg(1,91285), mk_omsg(1,81735), mk_omsg(1,72185), mk_omsg(1,62635), mk_omsg(1,53085), mk_imsg(1,43535), mk_omsg(1,33985), mk_omsg(1,24435), mk_omsg(1,14885), mk_omsg(1,5335)],  
]

#-------------------------------------------------------------------------
# Test Case Table
#-------------------------------------------------------------------------

test_case_table = mk_test_case_table([
  (                               "msgs                     src_delay  sinkA0_delay  sinkB0_delay   sinkA1_delay   sinkB1_delay  sinkA2_delay  sinkB2_delay sinkA3_delay  sinkB3_delay  sinkA4_delay  sinkB4_delay   sinkA5_delay  sinkB5_delay   sinkA6_delay   sinkB6_delay  sinkA7_delay  sinkB7_delay sinkA8_delay  sinkB8_delay  sinkA9_delay  sinkB9_delay     "),
  [ "small_pos_pos_10x10_1",        small_pos_pos_10x10_1_msgs,      0,         0,           0,          0,             0,              0,           0,             0,           0,              0,           0,           0,           0,              0,             0,              0,           0,             0,           0,              0,           0        ],
  [ "small_pos_pos_10x10_1_delay1", small_pos_pos_10x10_1_msgs,      0,         1,           0,          0,             0,              0,           0,             0,           0,              0,           0,           1,           0,              0,             0,              0,           0,             0,           0,              0,           0        ],
  [ "small_pos_pos_10x10_1_delay2", small_pos_pos_10x10_1_msgs,      0,         0,           1,          0,             0,              0,           0,             0,           0,              0,           0,           0,           1,              0,             0,              0,           0,             0,           0,              0,           0        ],
  [ "small_pos_pos_10x10_1_delay3", small_pos_pos_10x10_1_msgs,      0,         0,           0,          1,             0,              0,           0,             0,           0,              0,           0,           0,           0,              1,             0,              0,           0,             0,           0,              0,           0        ],
  [ "small_pos_pos_10x10_1_delay4", small_pos_pos_10x10_1_msgs,      0,         0,           0,          0,             1,              0,           0,             0,           0,              0,           0,           0,           0,              0,             1,              0,           0,             0,           0,              0,           0        ],
  [ "small_pos_pos_10x10_1_delay5", small_pos_pos_10x10_1_msgs,      0,         0,           0,          0,             0,              1,           0,             0,           0,              0,           0,           0,           0,              0,             0,              1,           0,             0,           0,              0,           0        ],
  [ "small_pos_pos_10x10_1_delay6", small_pos_pos_10x10_1_msgs,      0,         0,           0,          0,             0,              0,           1,             0,           0,              0,           0,           0,           0,              0,             0,              0,           1,             0,           0,              0,           0        ],
  [ "small_pos_pos_10x10_1_delay7", small_pos_pos_10x10_1_msgs,      0,         4,           2,          0,             0,              0,           0,             0,           0,              0,           0,           4,           2,              0,             0,              0,           0,             0,           0,              0,           0        ],
  [ "small_pos_pos_10x10_1_delay8", small_pos_pos_10x10_1_msgs,      0,         0,           0,          4,             2,              0,           0,             0,           0,              0,           0,           0,           0,              4,             2,              0,           0,             0,           0,              0,           0        ],
  [ "small_pos_pos_10x10_1_delay9", small_pos_pos_10x10_1_msgs,      0,         0,           0,          0,             0,              4,           2,             0,           0,              0,           0,           0,           0,              0,             0,              4,           2,             0,           0,              0,           0        ],
])

#-------------------------------------------------------------------------
# TestHarness
#-------------------------------------------------------------------------

@pytest.mark.parametrize( **test_case_table )
def test( test_params, cmdline_opts ):

  th = TestHarness( SysBase( SIZE = 10 ) )

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
  
  th.set_param("top.srcA5.construct",
    msgs=test_params.msgs[10],
    interval_delay=0 )
    
  th.set_param("top.srcB5.construct",
    msgs=test_params.msgs[11],
    interval_delay=0 )
  
  th.set_param("top.srcA6.construct",
    msgs=test_params.msgs[12],
    interval_delay=0 )
    
  th.set_param("top.srcB6.construct",
    msgs=test_params.msgs[13],
    interval_delay=0 )
  
  th.set_param("top.srcA7.construct",
    msgs=test_params.msgs[14],
    interval_delay=0 )
    
  th.set_param("top.srcB7.construct",
    msgs=test_params.msgs[15],
    interval_delay=0 )
  
  th.set_param("top.srcA8.construct",
    msgs=test_params.msgs[16],
    interval_delay=0 )
    
  th.set_param("top.srcB8.construct",
    msgs=test_params.msgs[17],
    interval_delay=0 )
  
  th.set_param("top.srcA9.construct",
    msgs=test_params.msgs[18],
    interval_delay=0 )
    
  th.set_param("top.srcB9.construct",
    msgs=test_params.msgs[19],
    interval_delay=0 )

  
  th.set_param("top.sinkA0.construct",
    msgs=test_params.msgs[20],
    initial_delay=test_params.sinkA0_delay+3,
    interval_delay=test_params.sinkA0_delay )
  
  th.set_param("top.sinkB0.construct",
    msgs=test_params.msgs[21],
    initial_delay=test_params.sinkB0_delay+3,
    interval_delay=test_params.sinkB0_delay )
  
  th.set_param("top.sinkA1.construct",
    msgs=test_params.msgs[22],
    initial_delay=test_params.sinkA1_delay+3,
    interval_delay=test_params.sinkA1_delay )
  
  th.set_param("top.sinkB1.construct",
    msgs=test_params.msgs[23],
    initial_delay=test_params.sinkB1_delay+3,
    interval_delay=test_params.sinkB1_delay )
  
  th.set_param("top.sinkA2.construct",
    msgs=test_params.msgs[24],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  th.set_param("top.sinkB2.construct",
    msgs=test_params.msgs[25],
    initial_delay=test_params.sinkB2_delay+3,
    interval_delay=test_params.sinkB2_delay )
  
  th.set_param("top.sinkA3.construct",
    msgs=test_params.msgs[26],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  th.set_param("top.sinkB3.construct",
    msgs=test_params.msgs[27],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  th.set_param("top.sinkA4.construct",
    msgs=test_params.msgs[28],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  th.set_param("top.sinkB4.construct",
    msgs=test_params.msgs[29],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  th.set_param("top.sinkA5.construct",
    msgs=test_params.msgs[30],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  th.set_param("top.sinkB5.construct",
    msgs=test_params.msgs[31],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  th.set_param("top.sinkA6.construct",
    msgs=test_params.msgs[32],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  th.set_param("top.sinkB6.construct",
    msgs=test_params.msgs[33],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  th.set_param("top.sinkA7.construct",
    msgs=test_params.msgs[34],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  th.set_param("top.sinkB7.construct",
    msgs=test_params.msgs[35],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  th.set_param("top.sinkA8.construct",
    msgs=test_params.msgs[36],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  th.set_param("top.sinkB8.construct",
    msgs=test_params.msgs[37],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  th.set_param("top.sinkA9.construct",
    msgs=test_params.msgs[38],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  th.set_param("top.sinkB9.construct",
    msgs=test_params.msgs[39],
    initial_delay=test_params.sinkA2_delay+3,
    interval_delay=test_params.sinkA2_delay )
  
  
  run_sim( th, cmdline_opts, duts=['pe'] )

