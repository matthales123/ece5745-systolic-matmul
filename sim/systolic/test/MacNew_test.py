#=========================================================================
# IntMulFL_test
#=========================================================================

import pytest

from random import randint

from pymtl3 import *
from pymtl3.stdlib.test_utils import mk_test_case_table, run_sim
from pymtl3.stdlib.stream import StreamSourceFL, StreamSinkFL

# from systolic.MacAlt import MacAlt
from systolic.MacNew import MacNew

#-------------------------------------------------------------------------
# TestHarness
#-------------------------------------------------------------------------

class TestHarness( Component ):

  def construct( s, mac ):

    # Instantiate models
    # s.giveresult = InPort(1)
    s.srcA  = StreamSourceFL( Bits33 )
    s.srcB  = StreamSourceFL( Bits33 )
    # s.sink = StreamSinkFL   ( Bits32 )
    s.sinkA = StreamSinkFL  ( Bits33 ) 
    s.sinkB = StreamSinkFL  ( Bits33 )
    s.mac = mac
    # s.srcResult = StreamSourceFL(Bits1)


    # Connect

    s.srcA.ostream    //= s.mac.istreamA
    s.srcB.ostream    //= s.mac.istreamB
    # s.mac.ostream     //= s.sink.istream
    s.mac.ostreamA    //= s.sinkA.istream
    s.mac.ostreamB    //= s.sinkB.istream
    # s.srcResult.ostream //= s.mac.giveresult
  
 

  def done( s ):
    return s.srcA.done() and s.srcB.done() and s.sinkA.done() and s.sinkB.done()

  def line_trace( s ):
    return s.srcA.line_trace() + " > " + s.srcB.line_trace() + " > " + s.mac.line_trace() + " > " + s.sinkA.line_trace() + " > " + s.sinkB.line_trace() 

#-------------------------------------------------------------------------
# mk_imsg/mk_omsg
#-------------------------------------------------------------------------

# Make input message, truncate ints to ensure they fit in 32 bits.

def mk_imsg( a, b ):
  return concat( Bits1( a ), Bits32( b, trunc_int=True ) )




# Make output message, truncate ints to ensure they fit in 32 bits.

# def mk_omsg( a ):
#   return Bits32( a, trunc_int=True )
def mk_omsg( a, b ):
 return concat( Bits1( a ), Bits32( b, trunc_int=True ) )

#----------------------------------------------------------------------
# Test Case: zero * positive/neg/zero
#----------------------------------------------------------------------


#===============================================================================================================
# 3 Input tests Positive / Zero
#===============================================================================================================

small_pos_pos_3in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,1),mk_imsg(0,2), mk_imsg(0,3),mk_imsg(1,0),mk_imsg(1,0),mk_imsg(1,0)],  
  
  [ mk_imsg(0,4),mk_imsg(0,5), mk_imsg(0,6), mk_imsg(1,17), mk_imsg(1,16), mk_imsg(1,15)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,1),mk_omsg(0,2), mk_omsg(0,3),mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)], 
  
  [ mk_omsg(0,4),mk_omsg(0,5),mk_omsg(0,6),mk_omsg(1,32), mk_omsg(1,17), mk_omsg(1,16)]

]

small_pos_zero_3in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,1),mk_imsg(0,2), mk_imsg(0,3),mk_imsg(1,0),mk_imsg(1,0),mk_imsg(1,0)],  
  
  [ mk_imsg(0,0),mk_imsg(0,0), mk_imsg(0,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,1),mk_omsg(0,2), mk_omsg(0,3),mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)], 
  
  [ mk_omsg(0,0),mk_omsg(0,0),mk_omsg(0,0),mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)]

]

large_pos_pos_3in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,1000),mk_imsg(0,2000), mk_imsg(0,3000),mk_imsg(1,0),mk_imsg(1,0),mk_imsg(1,0)],  
  
  [ mk_imsg(0,4),mk_imsg(0,5), mk_imsg(0,6), mk_imsg(1,17), mk_imsg(1,16), mk_imsg(1,15)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,1000),mk_omsg(0,2000), mk_omsg(0,3000),mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)], 
  
  [ mk_omsg(0,4),mk_omsg(0,5),mk_omsg(0,6),mk_omsg(1,32000), mk_omsg(1,17), mk_omsg(1,16)]

]

large_pos_zero_3in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,1000),mk_imsg(0,2000), mk_imsg(0,3000),mk_imsg(1,0),mk_imsg(1,0),mk_imsg(1,0)],  
  
  [ mk_imsg(0,0),mk_imsg(0,0), mk_imsg(0,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,1000),mk_omsg(0,2000), mk_omsg(0,3000),mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)], 
  
  [ mk_omsg(0,0),mk_omsg(0,0),mk_omsg(0,0),mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)]

]

#===============================================================================================================
# 3 Input tests Negative / Zero
#===============================================================================================================

small_neg_pos_3in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,-1),mk_imsg(0,-2), mk_imsg(0,-3),mk_imsg(1,0),mk_imsg(1,0),mk_imsg(1,0)],  
  
  [ mk_imsg(0,4),mk_imsg(0,5), mk_imsg(0,6), mk_imsg(1,17), mk_imsg(1,16), mk_imsg(1,15)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,-1),mk_omsg(0,-2), mk_omsg(0,-3),mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)], 
  
  [ mk_omsg(0,4),mk_omsg(0,5),mk_omsg(0,6),mk_omsg(1,-32), mk_omsg(1,17), mk_omsg(1,16)]

]

small_neg_zero_3in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,-1),mk_imsg(0,-2), mk_imsg(0,-3),mk_imsg(1,0),mk_imsg(1,0),mk_imsg(1,0)],  
  
  [ mk_imsg(0,0),mk_imsg(0,0), mk_imsg(0,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,-1),mk_omsg(0,-2), mk_omsg(0,-3),mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)], 
  
  [ mk_omsg(0,0),mk_omsg(0,0),mk_omsg(0,0),mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)]

]

large_neg_pos_3in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,-1000),mk_imsg(0,-2000), mk_imsg(0,-3000),mk_imsg(1,0),mk_imsg(1,0),mk_imsg(1,0)],  
  
  [ mk_imsg(0,4),mk_imsg(0,5), mk_imsg(0,6), mk_imsg(1,17), mk_imsg(1,16), mk_imsg(1,15)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,-1000),mk_omsg(0,-2000), mk_omsg(0,-3000),mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)], 
  
  [ mk_omsg(0,4),mk_omsg(0,5),mk_omsg(0,6),mk_omsg(1,-32000), mk_omsg(1,17), mk_omsg(1,16)]

]

large_neg_zero_3in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,-1000),mk_imsg(0,-2000), mk_imsg(0,-3000),mk_imsg(1,0),mk_imsg(1,0),mk_imsg(1,0)],  
  
  [ mk_imsg(0,0),mk_imsg(0,0), mk_imsg(0,0), mk_imsg(1,0), mk_imsg(1,0), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,-1000),mk_omsg(0,-2000), mk_omsg(0,-3000),mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)], 
  
  [ mk_omsg(0,0),mk_omsg(0,0),mk_omsg(0,0),mk_omsg(1,0), mk_omsg(1,0), mk_omsg(1,0)]

]


#===============================================================================================================
# 4 Input tests Positive / Zero
#===============================================================================================================

small_pos_pos_4in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,1),mk_imsg(0,2), mk_imsg(0,3), mk_imsg(0,4), mk_imsg(1,0)],  
  
  [ mk_imsg(0,5),mk_imsg(0,6), mk_imsg(0,7), mk_imsg(0,8), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,1),mk_omsg(0,2), mk_omsg(0,3), mk_omsg(0,4), mk_omsg(1,0)], 
  
  [ mk_omsg(0,5),mk_omsg(0,6),mk_omsg(0,7), mk_omsg(0,8), mk_omsg(1,70)]

]

small_pos_zero_4in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,1),mk_imsg(0,2), mk_imsg(0,3), mk_imsg(0,4), mk_imsg(1,0)],  
  
  [ mk_imsg(0,0),mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,1),mk_omsg(0,2), mk_omsg(0,3), mk_omsg(0,4), mk_omsg(1,0)], 
  
  [ mk_omsg(0,0),mk_omsg(0,0),mk_omsg(0,0), mk_omsg(0,0), mk_omsg(1,0)]

]

large_pos_pos_4in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,100000),mk_imsg(0,200000), mk_imsg(0,300000), mk_imsg(0,400000), mk_imsg(1,0)],  
  
  [ mk_imsg(0,5),mk_imsg(0,6), mk_imsg(0,7), mk_imsg(0,8), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,100000),mk_omsg(0,200000), mk_omsg(0,300000), mk_omsg(0,400000), mk_omsg(1,0)], 
  
  [ mk_omsg(0,5),mk_omsg(0,6),mk_omsg(0,7), mk_omsg(0,8), mk_omsg(1,7000000)]

]

large_pos_zero_4in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,10000),mk_imsg(0,20000), mk_imsg(0,30000), mk_imsg(0,40000), mk_imsg(1,0)],  
  
  [ mk_imsg(0,0),mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,10000),mk_omsg(0,20000), mk_omsg(0,30000), mk_omsg(0,40000), mk_omsg(1,0)], 
  
  [ mk_omsg(0,0),mk_omsg(0,0),mk_omsg(0,0), mk_omsg(0,0), mk_omsg(1,0)]

]

#===============================================================================================================
# 4 Input tests Negative / Zero
#===============================================================================================================

small_neg_pos_4in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,-1),mk_imsg(0,-2), mk_imsg(0,-3), mk_imsg(0,-4), mk_imsg(1,0)],  
  
  [ mk_imsg(0,5),mk_imsg(0,6), mk_imsg(0,7), mk_imsg(0,8), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,-1),mk_omsg(0,-2), mk_omsg(0,-3), mk_omsg(0,-4), mk_omsg(1,0)], 
  
  [ mk_omsg(0,5),mk_omsg(0,6),mk_omsg(0,7), mk_omsg(0,8), mk_omsg(1,-70)]

]

small_neg_zero_4in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,-1),mk_imsg(0,-2), mk_imsg(0,-3), mk_imsg(0,-4), mk_imsg(1,0)],  
  
  [ mk_imsg(0,0),mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,-1),mk_omsg(0,-2), mk_omsg(0,-3), mk_omsg(0,-4), mk_omsg(1,0)], 
  
  [ mk_omsg(0,0),mk_omsg(0,0),mk_omsg(0,0), mk_omsg(0,0), mk_omsg(1,0)]

]

large_neg_pos_4in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,-100000),mk_imsg(0,-200000), mk_imsg(0,-300000), mk_imsg(0,-400000), mk_imsg(1,0)],  
  
  [ mk_imsg(0,5),mk_imsg(0,6), mk_imsg(0,7), mk_imsg(0,8), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,-100000),mk_omsg(0,-200000), mk_omsg(0,-300000), mk_omsg(0,-400000), mk_omsg(1,0)], 
  
  [ mk_omsg(0,5),mk_omsg(0,6),mk_omsg(0,7), mk_omsg(0,8), mk_omsg(1,-7000000)]

]

large_neg_zero_4in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,-10000),mk_imsg(0,-20000), mk_imsg(0,-30000), mk_imsg(0,-40000), mk_imsg(1,0)],  
  
  [ mk_imsg(0,0),mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,-10000),mk_omsg(0,-20000), mk_omsg(0,-30000), mk_omsg(0,-40000), mk_omsg(1,0)], 
  
  [ mk_omsg(0,0),mk_omsg(0,0),mk_omsg(0,0), mk_omsg(0,0), mk_omsg(1,0)]

]



#===============================================================================================================
# 5 Input tests Postive / Zero
#===============================================================================================================

small_pos_pos_5in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,1),mk_imsg(0,2), mk_imsg(0,3), mk_imsg(0,4), mk_imsg(0,5),mk_imsg(1,0)],  
  
  [ mk_imsg(0,6),mk_imsg(0,7), mk_imsg(0,8), mk_imsg(0,9), mk_imsg(0,10), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,1),mk_omsg(0,2), mk_omsg(0,3), mk_imsg(0,4), mk_imsg(0,5),mk_omsg(1,0)], 
  
  [ mk_omsg(0,6),mk_omsg(0,7),mk_omsg(0,8), mk_imsg(0,9), mk_imsg(0,10), mk_omsg(1,130)]

]

small_pos_zero_5in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,1),mk_imsg(0,2), mk_imsg(0,3), mk_imsg(0,4), mk_imsg(0,5),mk_imsg(1,0)],  
  
  [ mk_imsg(0,0),mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,1),mk_omsg(0,2), mk_omsg(0,3), mk_imsg(0,4), mk_imsg(0,5),mk_omsg(1,0)], 
  
  [mk_omsg(0,0),mk_omsg(0,0),mk_omsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_omsg(1,0)]

]

large_pos_pos_5in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,100000),mk_imsg(0,200000), mk_imsg(0,300000), mk_imsg(0,400000), mk_imsg(0,500000), mk_imsg(1,0)],  
  
  [mk_omsg(0,6),mk_omsg(0,7),mk_omsg(0,8), mk_imsg(0,9), mk_imsg(0,10), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,100000),mk_omsg(0,200000), mk_omsg(0,300000), mk_omsg(0,400000), mk_omsg(0,500000), mk_omsg(1,0)], 
  
  [mk_omsg(0,6),mk_omsg(0,7),mk_omsg(0,8), mk_imsg(0,9), mk_imsg(0,10), mk_omsg(1,13000000)]

]

large_pos_zero_5in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,100000),mk_imsg(0,200000), mk_imsg(0,300000), mk_imsg(0,400000), mk_imsg(0,500000), mk_imsg(1,0)],  
  
  [mk_imsg(0,0),mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,100000),mk_omsg(0,200000), mk_omsg(0,300000), mk_omsg(0,400000), mk_omsg(0,500000), mk_omsg(1,0)], 
  
  [mk_omsg(0,0),mk_omsg(0,0),mk_omsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_omsg(1,0)]

]

#===============================================================================================================
# 5 Input tests Negative / Zero
#===============================================================================================================

small_neg_pos_5in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,-1),mk_imsg(0,-2), mk_imsg(0,-3), mk_imsg(0,-4), mk_imsg(0,-5),mk_imsg(1,0)],  
  
  [ mk_imsg(0,6),mk_imsg(0,7), mk_imsg(0,8), mk_imsg(0,9), mk_imsg(0,10), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,-1),mk_omsg(0,-2), mk_omsg(0,-3), mk_imsg(0,-4), mk_imsg(0,-5),mk_omsg(1,0)], 
  
  [ mk_omsg(0,6),mk_omsg(0,7),mk_omsg(0,8), mk_imsg(0,9), mk_imsg(0,10), mk_omsg(1,-130)]

]

small_neg_zero_5in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,-1),mk_imsg(0,-2), mk_imsg(0,-3), mk_imsg(0,-4), mk_imsg(0,-5),mk_imsg(1,0)],  
  
  [ mk_imsg(0,0),mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,-1),mk_omsg(0,-2), mk_omsg(0,-3), mk_imsg(0,-4), mk_imsg(0,-5),mk_omsg(1,0)], 
  
  [mk_omsg(0,0),mk_omsg(0,0),mk_omsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_omsg(1,0)]

]

large_neg_pos_5in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,-100000),mk_imsg(0,-200000), mk_imsg(0,-300000), mk_imsg(0,-400000), mk_imsg(0,-500000), mk_imsg(1,0)],  
  
  [mk_omsg(0,6),mk_omsg(0,7),mk_omsg(0,8), mk_imsg(0,9), mk_imsg(0,10), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,-100000),mk_omsg(0,-200000), mk_omsg(0,-300000), mk_omsg(0,-400000), mk_omsg(0,-500000), mk_omsg(1,0)], 
  
  [mk_omsg(0,6),mk_omsg(0,7),mk_omsg(0,8), mk_imsg(0,9), mk_imsg(0,10), mk_omsg(1,-13000000)]

]

large_neg_zero_5in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,-100000),mk_imsg(0,-200000), mk_imsg(0,-300000), mk_imsg(0,-400000), mk_imsg(0,-500000), mk_imsg(1,0)],  
  
  [mk_imsg(0,0),mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,-100000),mk_omsg(0,-200000), mk_omsg(0,-300000), mk_omsg(0,-400000), mk_omsg(0,-500000), mk_omsg(1,0)], 
  
  [mk_omsg(0,0),mk_omsg(0,0),mk_omsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_omsg(1,0)]

]

#===============================================================================================================
# 10 Input tests Postive / Zero
#===============================================================================================================

small_pos_pos_10in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,1), mk_imsg(0,2), mk_imsg(0,3), mk_imsg(0,4), mk_imsg(0,5), mk_imsg(0,6), mk_imsg(0,7), mk_imsg(0,8), mk_imsg(0,9), mk_imsg(0,10),mk_imsg(1,0)],  
  
  [mk_imsg(0,11), mk_imsg(0,12), mk_imsg(0,13), mk_imsg(0,14), mk_imsg(0,15), mk_imsg(0,16), mk_imsg(0,17), mk_imsg(0,18), mk_imsg(0,19), mk_imsg(0,20), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,1), mk_omsg(0,2), mk_omsg(0,3), mk_omsg(0,4), mk_omsg(0,5), mk_omsg(0,6), mk_omsg(0,7), mk_omsg(0,8), mk_omsg(0,9), mk_omsg(0,10), mk_omsg(1,0)], 
  
  [mk_omsg(0,11), mk_omsg(0,12), mk_omsg(0,13), mk_omsg(0,14), mk_omsg(0,15), mk_omsg(0,16), mk_omsg(0,17), mk_omsg(0,18), mk_omsg(0,19), mk_omsg(0,20), mk_omsg(1,935)]

]

small_pos_zero_10in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,1), mk_imsg(0,2), mk_imsg(0,3), mk_imsg(0,4), mk_imsg(0,5), mk_imsg(0,6), mk_imsg(0,7), mk_imsg(0,8), mk_imsg(0,9), mk_imsg(0,10),mk_imsg(1,0)],  
  
  [mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,1), mk_omsg(0,2), mk_omsg(0,3), mk_omsg(0,4), mk_omsg(0,5), mk_omsg(0,6), mk_omsg(0,7), mk_omsg(0,8), mk_omsg(0,9), mk_omsg(0,10), mk_omsg(1,0)], 
  
  [mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(1,0)]

]

large_pos_pos_10in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,10000), mk_imsg(0,20000), mk_imsg(0,30000), mk_imsg(0,40000), mk_imsg(0,50000), mk_imsg(0,60000), mk_imsg(0,70000), mk_imsg(0,80000), mk_imsg(0,90000), mk_imsg(0,100000),mk_imsg(1,0)],  
  
  [mk_imsg(0,11), mk_imsg(0,12), mk_imsg(0,13), mk_imsg(0,14), mk_imsg(0,15), mk_imsg(0,16), mk_imsg(0,17), mk_imsg(0,18), mk_imsg(0,19), mk_imsg(0,20), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,10000), mk_omsg(0,20000), mk_omsg(0,30000), mk_omsg(0,40000), mk_omsg(0,50000), mk_omsg(0,60000), mk_omsg(0,70000), mk_omsg(0,80000), mk_omsg(0,90000), mk_omsg(0,100000), mk_omsg(1,0)], 
  
  [mk_omsg(0,11), mk_omsg(0,12), mk_omsg(0,13), mk_omsg(0,14), mk_omsg(0,15), mk_omsg(0,16), mk_omsg(0,17), mk_omsg(0,18), mk_omsg(0,19), mk_omsg(0,20), mk_omsg(1,9350000)]

]

large_pos_zero_10in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,10000), mk_imsg(0,20000), mk_imsg(0,30000), mk_imsg(0,40000), mk_imsg(0,50000), mk_imsg(0,60000), mk_imsg(0,70000), mk_imsg(0,80000), mk_imsg(0,90000), mk_imsg(0,100000),mk_imsg(1,0)],  
  
  [mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,10000), mk_omsg(0,20000), mk_omsg(0,30000), mk_omsg(0,40000), mk_omsg(0,50000), mk_omsg(0,60000), mk_omsg(0,70000), mk_omsg(0,80000), mk_omsg(0,90000), mk_omsg(0,100000), mk_omsg(1,0)], 
  
  [mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(1,0)]

]

#===============================================================================================================
# 10 Input tests Negative / Zero
#===============================================================================================================

small_neg_pos_10in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,-1), mk_imsg(0,-2), mk_imsg(0,-3), mk_imsg(0,-4), mk_imsg(0,-5), mk_imsg(0,-6), mk_imsg(0,-7), mk_imsg(0,-8), mk_imsg(0,-9), mk_imsg(0,-10),mk_imsg(1,0)],  
  
  [mk_imsg(0,11), mk_imsg(0,12), mk_imsg(0,13), mk_imsg(0,14), mk_imsg(0,15), mk_imsg(0,16), mk_imsg(0,17), mk_imsg(0,18), mk_imsg(0,19), mk_imsg(0,20), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,-1), mk_omsg(0,-2), mk_omsg(0,-3), mk_omsg(0,-4), mk_omsg(0,-5), mk_omsg(0,-6), mk_omsg(0,-7), mk_omsg(0,-8), mk_omsg(0,-9), mk_omsg(0,-10), mk_omsg(1,0)], 
  
  [mk_omsg(0,11), mk_omsg(0,12), mk_omsg(0,13), mk_omsg(0,14), mk_omsg(0,15), mk_omsg(0,16), mk_omsg(0,17), mk_omsg(0,18), mk_omsg(0,19), mk_omsg(0,20), mk_omsg(1,-935)]

]

small_neg_zero_10in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,-1), mk_imsg(0,-2), mk_imsg(0,-3), mk_imsg(0,-4), mk_imsg(0,-5), mk_imsg(0,-6), mk_imsg(0,-7), mk_imsg(0,-8), mk_imsg(0,-9), mk_imsg(0,-10),mk_imsg(1,0)],  
  
  [mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,-1), mk_omsg(0,-2), mk_omsg(0,-3), mk_omsg(0,-4), mk_omsg(0,-5), mk_omsg(0,-6), mk_omsg(0,-7), mk_omsg(0,-8), mk_omsg(0,-9), mk_omsg(0,-10), mk_omsg(1,0)], 
  
  [mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(1,0)]

]

large_neg_pos_10in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,-10000), mk_imsg(0,-20000), mk_imsg(0,-30000), mk_imsg(0,-40000), mk_imsg(0,-50000), mk_imsg(0,-60000), mk_imsg(0,-70000), mk_imsg(0,-80000), mk_imsg(0,-90000), mk_imsg(0,-100000),mk_imsg(1,0)],  
  
  [mk_imsg(0,11), mk_imsg(0,12), mk_imsg(0,13), mk_imsg(0,14), mk_imsg(0,15), mk_imsg(0,16), mk_imsg(0,17), mk_imsg(0,18), mk_imsg(0,19), mk_imsg(0,20), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,-10000), mk_omsg(0,-20000), mk_omsg(0,-30000), mk_omsg(0,-40000), mk_omsg(0,-50000), mk_omsg(0,-60000), mk_omsg(0,-70000), mk_omsg(0,-80000), mk_omsg(0,-90000), mk_omsg(0,-100000), mk_omsg(1,0)], 
  
  [mk_omsg(0,11), mk_omsg(0,12), mk_omsg(0,13), mk_omsg(0,14), mk_omsg(0,15), mk_omsg(0,16), mk_omsg(0,17), mk_omsg(0,18), mk_omsg(0,19), mk_omsg(0,20), mk_omsg(1,-9350000)]

]

large_neg_zero_10in_msgs = [
                          #  A_In                                                            B_In                                   Give_Result
  [mk_imsg(0,-10000), mk_imsg(0,-20000), mk_imsg(0,-30000), mk_imsg(0,-40000), mk_imsg(0,-50000), mk_imsg(0,-60000), mk_imsg(0,-70000), mk_imsg(0,-80000), mk_imsg(0,-90000), mk_imsg(0,-100000),mk_imsg(1,0)],  
  
  [mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(0,0), mk_imsg(1,0)],

                          #  A_Out                                                           B_Out
  [mk_omsg(0,-10000), mk_omsg(0,-20000), mk_omsg(0,-30000), mk_omsg(0,-40000), mk_omsg(0,-50000), mk_omsg(0,-60000), mk_omsg(0,-70000), mk_omsg(0,-80000), mk_omsg(0,-90000), mk_omsg(0,-100000), mk_omsg(1,0)], 
  
  [mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(0,0), mk_omsg(1,0)]

]

#-------------------------------------------------------------------------
# Test Case Table
#-------------------------------------------------------------------------
## add tests for all possible delays
test_case_table = mk_test_case_table([
  (                               "msgs                 srcA_delay srcB_delay  sinkA_delay sinkB_delay "),
  
  #===============================================================================================================
  # 3 Input tests Positive / zero inputs
  #===============================================================================================================
  [ "small_pos_pos_3in",           small_pos_pos_3in_msgs,      0,        0,             0,         0,          ],
  [ "small_pos_pos_3in_delay1",    small_pos_pos_3in_msgs,      0,        0,             0,         1,          ],
  [ "small_pos_pos_3in_delay2",    small_pos_pos_3in_msgs,      0,        0,             2,         0,          ],
  [ "small_pos_pos_3in_delay3",    small_pos_pos_3in_msgs,      0,        0,             3,         4,          ],
  [ "small_pos_pos_3in_delay4",    small_pos_pos_3in_msgs,      0,        0,             1,         10,         ],
  [ "small_pos_pos_3in_delay5",    small_pos_pos_3in_msgs,      0,        0,             10,        1,          ],
  [ "small_pos_pos_3in_delay6",    small_pos_pos_3in_msgs,      0,        1,             0,         0,          ],
  [ "small_pos_pos_3in_delay7",    small_pos_pos_3in_msgs,      3,        4,             0,         0,          ],
  [ "small_pos_pos_3in_delay8",    small_pos_pos_3in_msgs,      20,       10,            0,         0,          ],
  [ "small_pos_pos_3in_delay9",    small_pos_pos_3in_msgs,      10,       4,             0,         0,          ], 
  
  [ "small_pos_zero_3in",           small_pos_zero_3in_msgs,      0,        0,             0,         0,          ],
  [ "small_pos_zero_3in_delay1",    small_pos_zero_3in_msgs,      0,        0,             0,         1,          ],
  [ "small_pos_zero_3in_delay2",    small_pos_zero_3in_msgs,      0,        0,             2,         0,          ],
  [ "small_pos_zero_3in_delay3",    small_pos_zero_3in_msgs,      0,        0,             3,         4,          ],
  [ "small_pos_zero_3in_delay4",    small_pos_zero_3in_msgs,      0,        0,             1,         10,         ],
  [ "small_pos_zero_3in_delay5",    small_pos_zero_3in_msgs,      0,        0,             10,        1,          ],
  [ "small_pos_zero_3in_delay6",    small_pos_zero_3in_msgs,      0,        1,             0,         0,          ],
  [ "small_pos_zero_3in_delay7",    small_pos_zero_3in_msgs,      3,        4,             0,         0,          ],
  [ "small_pos_zero_3in_delay8",    small_pos_zero_3in_msgs,      20,       10,            0,         0,          ],
  [ "small_pos_zero_3in_delay9",    small_pos_zero_3in_msgs,      10,       4,             0,         0,          ], 
  
  [ "large_pos_pos_3in",           large_pos_pos_3in_msgs,      0,        0,             0,         0,          ],
  [ "large_pos_pos_3in_delay1",    large_pos_pos_3in_msgs,      0,        0,             0,         1,          ],
  [ "large_pos_pos_3in_delay2",    large_pos_pos_3in_msgs,      0,        0,             2,         0,          ],
  [ "large_pos_pos_3in_delay3",    large_pos_pos_3in_msgs,      0,        0,             3,         4,          ],
  [ "large_pos_pos_3in_delay4",    large_pos_pos_3in_msgs,      0,        0,             1,         10,         ],
  [ "large_pos_pos_3in_delay5",    large_pos_pos_3in_msgs,      0,        0,             10,        1,          ],
  [ "large_pos_pos_3in_delay6",    large_pos_pos_3in_msgs,      0,        1,             0,         0,          ],
  [ "large_pos_pos_3in_delay7",    large_pos_pos_3in_msgs,      3,        4,             0,         0,          ],
  [ "large_pos_pos_3in_delay8",    large_pos_pos_3in_msgs,      20,       10,            0,         0,          ],
  [ "large_pos_pos_3in_delay9",    large_pos_pos_3in_msgs,      10,       4,             0,         0,          ], 
  
  [ "large_pos_zero_3in",           large_pos_zero_3in_msgs,      0,        0,             0,         0,          ],
  [ "large_pos_zero_3in_delay1",    large_pos_zero_3in_msgs,      0,        0,             0,         1,          ],
  [ "large_pos_zero_3in_delay2",    large_pos_zero_3in_msgs,      0,        0,             2,         0,          ],
  [ "large_pos_zero_3in_delay3",    large_pos_zero_3in_msgs,      0,        0,             3,         4,          ],
  [ "large_pos_zero_3in_delay4",    large_pos_zero_3in_msgs,      0,        0,             1,         10,         ],
  [ "large_pos_zero_3in_delay5",    large_pos_zero_3in_msgs,      0,        0,             10,        1,          ],
  [ "large_pos_zero_3in_delay6",    large_pos_zero_3in_msgs,      0,        1,             0,         0,          ],
  [ "large_pos_zero_3in_delay7",    large_pos_zero_3in_msgs,      3,        4,             0,         0,          ],
  [ "large_pos_zero_3in_delay8",    large_pos_zero_3in_msgs,      20,       10,            0,         0,          ],
  [ "large_pos_zero_3in_delay9",    large_pos_zero_3in_msgs,      10,       4,             0,         0,          ], 
  
  #===============================================================================================================
  # 3 Input tests negative / zero inputs
  #===============================================================================================================
  [ "small_neg_pos_3in",           small_neg_pos_3in_msgs,      0,        0,             0,         0,          ],
  [ "small_neg_pos_3in_delay1",    small_neg_pos_3in_msgs,      0,        0,             0,         1,          ],
  [ "small_neg_pos_3in_delay2",    small_neg_pos_3in_msgs,      0,        0,             2,         0,          ],
  [ "small_neg_pos_3in_delay3",    small_neg_pos_3in_msgs,      0,        0,             3,         4,          ],
  [ "small_neg_pos_3in_delay4",    small_neg_pos_3in_msgs,      0,        0,             1,         10,         ],
  [ "small_neg_pos_3in_delay5",    small_neg_pos_3in_msgs,      0,        0,             10,        1,          ],
  [ "small_neg_pos_3in_delay6",    small_neg_pos_3in_msgs,      0,        1,             0,         0,          ],
  [ "small_neg_pos_3in_delay7",    small_neg_pos_3in_msgs,      3,        4,             0,         0,          ],
  [ "small_neg_pos_3in_delay8",    small_neg_pos_3in_msgs,      20,       10,            0,         0,          ],
  [ "small_neg_pos_3in_delay9",    small_neg_pos_3in_msgs,      10,       4,             0,         0,          ], 
  
  [ "small_neg_zero_3in",           small_neg_zero_3in_msgs,      0,        0,             0,         0,          ],
  [ "small_neg_zero_3in_delay1",    small_neg_zero_3in_msgs,      0,        0,             0,         1,          ],
  [ "small_neg_zero_3in_delay2",    small_neg_zero_3in_msgs,      0,        0,             2,         0,          ],
  [ "small_neg_zero_3in_delay3",    small_neg_zero_3in_msgs,      0,        0,             3,         4,          ],
  [ "small_neg_zero_3in_delay4",    small_neg_zero_3in_msgs,      0,        0,             1,         10,         ],
  [ "small_neg_zero_3in_delay5",    small_neg_zero_3in_msgs,      0,        0,             10,        1,          ],
  [ "small_neg_zero_3in_delay6",    small_neg_zero_3in_msgs,      0,        1,             0,         0,          ],
  [ "small_neg_zero_3in_delay7",    small_neg_zero_3in_msgs,      3,        4,             0,         0,          ],
  [ "small_neg_zero_3in_delay8",    small_neg_zero_3in_msgs,      20,       10,            0,         0,          ],
  [ "small_neg_zero_3in_delay9",    small_neg_zero_3in_msgs,      10,       4,             0,         0,          ], 
  
  [ "large_neg_pos_3in",           large_neg_pos_3in_msgs,      0,        0,             0,         0,          ],
  [ "large_neg_pos_3in_delay1",    large_neg_pos_3in_msgs,      0,        0,             0,         1,          ],
  [ "large_neg_pos_3in_delay2",    large_neg_pos_3in_msgs,      0,        0,             2,         0,          ],
  [ "large_neg_pos_3in_delay3",    large_neg_pos_3in_msgs,      0,        0,             3,         4,          ],
  [ "large_neg_pos_3in_delay4",    large_neg_pos_3in_msgs,      0,        0,             1,         10,         ],
  [ "large_neg_pos_3in_delay5",    large_neg_pos_3in_msgs,      0,        0,             10,        1,          ],
  [ "large_neg_pos_3in_delay6",    large_neg_pos_3in_msgs,      0,        1,             0,         0,          ],
  [ "large_neg_pos_3in_delay7",    large_neg_pos_3in_msgs,      3,        4,             0,         0,          ],
  [ "large_neg_pos_3in_delay8",    large_neg_pos_3in_msgs,      20,       10,            0,         0,          ],
  [ "large_neg_pos_3in_delay9",    large_neg_pos_3in_msgs,      10,       4,             0,         0,          ], 
  
  [ "large_neg_zero_3in",           large_neg_zero_3in_msgs,      0,        0,             0,         0,          ],
  [ "large_neg_zero_3in_delay1",    large_neg_zero_3in_msgs,      0,        0,             0,         1,          ],
  [ "large_neg_zero_3in_delay2",    large_neg_zero_3in_msgs,      0,        0,             2,         0,          ],
  [ "large_neg_zero_3in_delay3",    large_neg_zero_3in_msgs,      0,        0,             3,         4,          ],
  [ "large_neg_zero_3in_delay4",    large_neg_zero_3in_msgs,      0,        0,             1,         10,         ],
  [ "large_neg_zero_3in_delay5",    large_neg_zero_3in_msgs,      0,        0,             10,        1,          ],
  [ "large_neg_zero_3in_delay6",    large_neg_zero_3in_msgs,      0,        1,             0,         0,          ],
  [ "large_neg_zero_3in_delay7",    large_neg_zero_3in_msgs,      3,        4,             0,         0,          ],
  [ "large_neg_zero_3in_delay8",    large_neg_zero_3in_msgs,      20,       10,            0,         0,          ],
  [ "large_neg_zero_3in_delay9",    large_neg_zero_3in_msgs,      10,       4,             0,         0,          ], 
  
  #===============================================================================================================
  # 4 Input tests Positive / Zero
  #===============================================================================================================
  [ "small_pos_pos_4in",           small_pos_pos_4in_msgs,      0,        0,             0,         0,          ],
  [ "small_pos_pos_4in_delay1",    small_pos_pos_4in_msgs,      0,        0,             0,         1,          ],
  [ "small_pos_pos_4in_delay2",    small_pos_pos_4in_msgs,      0,        0,             2,         0,          ],
  [ "small_pos_pos_4in_delay3",    small_pos_pos_4in_msgs,      0,        0,             3,         4,          ],
  [ "small_pos_pos_4in_delay4",    small_pos_pos_4in_msgs,      0,        0,             1,         10,         ],
  [ "small_pos_pos_4in_delay5",    small_pos_pos_4in_msgs,      0,        0,             10,        1,          ],
  [ "small_pos_pos_4in_delay6",    small_pos_pos_4in_msgs,      0,        1,             0,         0,          ],
  [ "small_pos_pos_4in_delay7",    small_pos_pos_4in_msgs,      3,        4,             0,         0,          ],
  [ "small_pos_pos_4in_delay8",    small_pos_pos_4in_msgs,      20,       10,            0,         0,          ],
  [ "small_pos_pos_4in_delay9",    small_pos_pos_4in_msgs,      10,       4,             0,         0,          ], 
  
  [ "small_pos_zero_4in",           small_pos_zero_4in_msgs,      0,        0,             0,         0,          ],
  [ "small_pos_zero_4in_delay1",    small_pos_zero_4in_msgs,      0,        0,             0,         1,          ],
  [ "small_pos_zero_4in_delay2",    small_pos_zero_4in_msgs,      0,        0,             2,         0,          ],
  [ "small_pos_zero_4in_delay3",    small_pos_zero_4in_msgs,      0,        0,             3,         4,          ],
  [ "small_pos_zero_4in_delay4",    small_pos_zero_4in_msgs,      0,        0,             1,         10,         ],
  [ "small_pos_zero_4in_delay5",    small_pos_zero_4in_msgs,      0,        0,             10,        1,          ],
  [ "small_pos_zero_4in_delay6",    small_pos_zero_4in_msgs,      0,        1,             0,         0,          ],
  [ "small_pos_zero_4in_delay7",    small_pos_zero_4in_msgs,      3,        4,             0,         0,          ],
  [ "small_pos_zero_4in_delay8",    small_pos_zero_4in_msgs,      20,       10,            0,         0,          ],
  [ "small_pos_zero_4in_delay9",    small_pos_zero_4in_msgs,      10,       4,             0,         0,          ], 
  
  [ "large_pos_pos_4in",           large_pos_pos_4in_msgs,      0,        0,             0,         0,          ],
  [ "large_pos_pos_4in_delay1",    large_pos_pos_4in_msgs,      0,        0,             0,         1,          ],
  [ "large_pos_pos_4in_delay2",    large_pos_pos_4in_msgs,      0,        0,             2,         0,          ],
  [ "large_pos_pos_4in_delay3",    large_pos_pos_4in_msgs,      0,        0,             3,         4,          ],
  [ "large_pos_pos_4in_delay4",    large_pos_pos_4in_msgs,      0,        0,             1,         10,         ],
  [ "large_pos_pos_4in_delay5",    large_pos_pos_4in_msgs,      0,        0,             10,        1,          ],
  [ "large_pos_pos_4in_delay6",    large_pos_pos_4in_msgs,      0,        1,             0,         0,          ],
  [ "large_pos_pos_4in_delay7",    large_pos_pos_4in_msgs,      3,        4,             0,         0,          ],
  [ "large_pos_pos_4in_delay8",    large_pos_pos_4in_msgs,      20,       10,            0,         0,          ],
  [ "large_pos_pos_4in_delay9",    large_pos_pos_4in_msgs,      10,       4,             0,         0,          ], 
  
  [ "large_pos_zero_4in",           large_pos_zero_4in_msgs,      0,        0,             0,         0,          ],
  [ "large_pos_zero_4in_delay1",    large_pos_zero_4in_msgs,      0,        0,             0,         1,          ],
  [ "large_pos_zero_4in_delay2",    large_pos_zero_4in_msgs,      0,        0,             2,         0,          ],
  [ "large_pos_zero_4in_delay3",    large_pos_zero_4in_msgs,      0,        0,             3,         4,          ],
  [ "large_pos_zero_4in_delay4",    large_pos_zero_4in_msgs,      0,        0,             1,         10,         ],
  [ "large_pos_zero_4in_delay5",    large_pos_zero_4in_msgs,      0,        0,             10,        1,          ],
  [ "large_pos_zero_4in_delay6",    large_pos_zero_4in_msgs,      0,        1,             0,         0,          ],
  [ "large_pos_zero_4in_delay7",    large_pos_zero_4in_msgs,      3,        4,             0,         0,          ],
  [ "large_pos_zero_4in_delay8",    large_pos_zero_4in_msgs,      20,       10,            0,         0,          ],
  [ "large_pos_zero_4in_delay9",    large_pos_zero_4in_msgs,      10,       4,             0,         0,          ], 
  
  #===============================================================================================================
  # 4 Input tests Negative / Zero
  #===============================================================================================================
  [ "small_neg_pos_4in",           small_neg_pos_4in_msgs,      0,        0,             0,         0,          ],
  [ "small_neg_pos_4in_delay1",    small_neg_pos_4in_msgs,      0,        0,             0,         1,          ],
  [ "small_neg_pos_4in_delay2",    small_neg_pos_4in_msgs,      0,        0,             2,         0,          ],
  [ "small_neg_pos_4in_delay3",    small_neg_pos_4in_msgs,      0,        0,             3,         4,          ],
  [ "small_neg_pos_4in_delay4",    small_neg_pos_4in_msgs,      0,        0,             1,         10,         ],
  [ "small_neg_pos_4in_delay5",    small_neg_pos_4in_msgs,      0,        0,             10,        1,          ],
  [ "small_neg_pos_4in_delay6",    small_neg_pos_4in_msgs,      0,        1,             0,         0,          ],
  [ "small_neg_pos_4in_delay7",    small_neg_pos_4in_msgs,      3,        4,             0,         0,          ],
  [ "small_neg_pos_4in_delay8",    small_neg_pos_4in_msgs,      20,       10,            0,         0,          ],
  [ "small_neg_pos_4in_delay9",    small_neg_pos_4in_msgs,      10,       4,             0,         0,          ], 
  
  [ "small_neg_zero_4in",           small_neg_zero_4in_msgs,      0,        0,             0,         0,          ],
  [ "small_neg_zero_4in_delay1",    small_neg_zero_4in_msgs,      0,        0,             0,         1,          ],
  [ "small_neg_zero_4in_delay2",    small_neg_zero_4in_msgs,      0,        0,             2,         0,          ],
  [ "small_neg_zero_4in_delay3",    small_neg_zero_4in_msgs,      0,        0,             3,         4,          ],
  [ "small_neg_zero_4in_delay4",    small_neg_zero_4in_msgs,      0,        0,             1,         10,         ],
  [ "small_neg_zero_4in_delay5",    small_neg_zero_4in_msgs,      0,        0,             10,        1,          ],
  [ "small_neg_zero_4in_delay6",    small_neg_zero_4in_msgs,      0,        1,             0,         0,          ],
  [ "small_neg_zero_4in_delay7",    small_neg_zero_4in_msgs,      3,        4,             0,         0,          ],
  [ "small_neg_zero_4in_delay8",    small_neg_zero_4in_msgs,      20,       10,            0,         0,          ],
  [ "small_neg_zero_4in_delay9",    small_neg_zero_4in_msgs,      10,       4,             0,         0,          ], 
  
  [ "large_neg_pos_4in",           large_neg_pos_4in_msgs,      0,        0,             0,         0,          ],
  [ "large_neg_pos_4in_delay1",    large_neg_pos_4in_msgs,      0,        0,             0,         1,          ],
  [ "large_neg_pos_4in_delay2",    large_neg_pos_4in_msgs,      0,        0,             2,         0,          ],
  [ "large_neg_pos_4in_delay3",    large_neg_pos_4in_msgs,      0,        0,             3,         4,          ],
  [ "large_neg_pos_4in_delay4",    large_neg_pos_4in_msgs,      0,        0,             1,         10,         ],
  [ "large_neg_pos_4in_delay5",    large_neg_pos_4in_msgs,      0,        0,             10,        1,          ],
  [ "large_neg_pos_4in_delay6",    large_neg_pos_4in_msgs,      0,        1,             0,         0,          ],
  [ "large_neg_pos_4in_delay7",    large_neg_pos_4in_msgs,      3,        4,             0,         0,          ],
  [ "large_neg_pos_4in_delay8",    large_neg_pos_4in_msgs,      20,       10,            0,         0,          ],
  [ "large_neg_pos_4in_delay9",    large_neg_pos_4in_msgs,      10,       4,             0,         0,          ], 
  
  [ "large_neg_zero_4in",           large_neg_zero_4in_msgs,      0,        0,             0,         0,          ],
  [ "large_neg_zero_4in_delay1",    large_neg_zero_4in_msgs,      0,        0,             0,         1,          ],
  [ "large_neg_zero_4in_delay2",    large_neg_zero_4in_msgs,      0,        0,             2,         0,          ],
  [ "large_neg_zero_4in_delay3",    large_neg_zero_4in_msgs,      0,        0,             3,         4,          ],
  [ "large_neg_zero_4in_delay4",    large_neg_zero_4in_msgs,      0,        0,             1,         10,         ],
  [ "large_neg_zero_4in_delay5",    large_neg_zero_4in_msgs,      0,        0,             10,        1,          ],
  [ "large_neg_zero_4in_delay6",    large_neg_zero_4in_msgs,      0,        1,             0,         0,          ],
  [ "large_neg_zero_4in_delay7",    large_neg_zero_4in_msgs,      3,        4,             0,         0,          ],
  [ "large_neg_zero_4in_delay8",    large_neg_zero_4in_msgs,      20,       10,            0,         0,          ],
  [ "large_neg_zero_4in_delay9",    large_neg_zero_4in_msgs,      10,       4,             0,         0,          ], 
  
  #===============================================================================================================
  # 5 Input tests Postive / Zero
  #===============================================================================================================
  [ "small_pos_pos_5in",           small_pos_pos_5in_msgs,      0,        0,             0,         0,          ],
  [ "small_pos_pos_5in_delay1",    small_pos_pos_5in_msgs,      0,        0,             0,         1,          ],
  [ "small_pos_pos_5in_delay2",    small_pos_pos_5in_msgs,      0,        0,             2,         0,          ],
  [ "small_pos_pos_5in_delay3",    small_pos_pos_5in_msgs,      0,        0,             3,         4,          ],
  [ "small_pos_pos_5in_delay4",    small_pos_pos_5in_msgs,      0,        0,             1,         10,         ],
  [ "small_pos_pos_5in_delay5",    small_pos_pos_5in_msgs,      0,        0,             10,        1,          ],
  [ "small_pos_pos_5in_delay6",    small_pos_pos_5in_msgs,      0,        1,             0,         0,          ],
  [ "small_pos_pos_5in_delay7",    small_pos_pos_5in_msgs,      3,        4,             0,         0,          ],
  [ "small_pos_pos_5in_delay8",    small_pos_pos_5in_msgs,      20,       10,            0,         0,          ],
  [ "small_pos_pos_5in_delay9",    small_pos_pos_5in_msgs,      10,       4,             0,         0,          ], 
  
  [ "small_pos_zero_5in",           small_pos_zero_5in_msgs,      0,        0,             0,         0,          ],
  [ "small_pos_zero_5in_delay1",    small_pos_zero_5in_msgs,      0,        0,             0,         1,          ],
  [ "small_pos_zero_5in_delay2",    small_pos_zero_5in_msgs,      0,        0,             2,         0,          ],
  [ "small_pos_zero_5in_delay3",    small_pos_zero_5in_msgs,      0,        0,             3,         4,          ],
  [ "small_pos_zero_5in_delay4",    small_pos_zero_5in_msgs,      0,        0,             1,         10,         ],
  [ "small_pos_zero_5in_delay5",    small_pos_zero_5in_msgs,      0,        0,             10,        1,          ],
  [ "small_pos_zero_5in_delay6",    small_pos_zero_5in_msgs,      0,        1,             0,         0,          ],
  [ "small_pos_zero_5in_delay7",    small_pos_zero_5in_msgs,      3,        4,             0,         0,          ],
  [ "small_pos_zero_5in_delay8",    small_pos_zero_5in_msgs,      20,       10,            0,         0,          ],
  [ "small_pos_zero_5in_delay9",    small_pos_zero_5in_msgs,      10,       4,             0,         0,          ], 
  
  [ "large_pos_pos_5in",           large_pos_pos_5in_msgs,      0,        0,             0,         0,          ],
  [ "large_pos_pos_5in_delay1",    large_pos_pos_5in_msgs,      0,        0,             0,         1,          ],
  [ "large_pos_pos_5in_delay2",    large_pos_pos_5in_msgs,      0,        0,             2,         0,          ],
  [ "large_pos_pos_5in_delay3",    large_pos_pos_5in_msgs,      0,        0,             3,         4,          ],
  [ "large_pos_pos_5in_delay4",    large_pos_pos_5in_msgs,      0,        0,             1,         10,         ],
  [ "large_pos_pos_5in_delay5",    large_pos_pos_5in_msgs,      0,        0,             10,        1,          ],
  [ "large_pos_pos_5in_delay6",    large_pos_pos_5in_msgs,      0,        1,             0,         0,          ],
  [ "large_pos_pos_5in_delay7",    large_pos_pos_5in_msgs,      3,        4,             0,         0,          ],
  [ "large_pos_pos_5in_delay8",    large_pos_pos_5in_msgs,      20,       10,            0,         0,          ],
  [ "large_pos_pos_5in_delay9",    large_pos_pos_5in_msgs,      10,       4,             0,         0,          ], 
  
  [ "large_pos_zero_5in",           large_pos_zero_5in_msgs,      0,        0,             0,         0,          ],
  [ "large_pos_zero_5in_delay1",    large_pos_zero_5in_msgs,      0,        0,             0,         1,          ],
  [ "large_pos_zero_5in_delay2",    large_pos_zero_5in_msgs,      0,        0,             2,         0,          ],
  [ "large_pos_zero_5in_delay3",    large_pos_zero_5in_msgs,      0,        0,             3,         4,          ],
  [ "large_pos_zero_5in_delay4",    large_pos_zero_5in_msgs,      0,        0,             1,         10,         ],
  [ "large_pos_zero_5in_delay5",    large_pos_zero_5in_msgs,      0,        0,             10,        1,          ],
  [ "large_pos_zero_5in_delay6",    large_pos_zero_5in_msgs,      0,        1,             0,         0,          ],
  [ "large_pos_zero_5in_delay7",    large_pos_zero_5in_msgs,      3,        4,             0,         0,          ],
  [ "large_pos_zero_5in_delay8",    large_pos_zero_5in_msgs,      20,       10,            0,         0,          ],
  [ "large_pos_zero_5in_delay9",    large_pos_zero_5in_msgs,      10,       4,             0,         0,          ], 
  
  #===============================================================================================================
  # 5 Input tests Negative / Zero
  #===============================================================================================================
  [ "small_neg_pos_5in",           small_neg_pos_5in_msgs,      0,        0,             0,         0,          ],
  [ "small_neg_pos_5in_delay1",    small_neg_pos_5in_msgs,      0,        0,             0,         1,          ],
  [ "small_neg_pos_5in_delay2",    small_neg_pos_5in_msgs,      0,        0,             2,         0,          ],
  [ "small_neg_pos_5in_delay3",    small_neg_pos_5in_msgs,      0,        0,             3,         4,          ],
  [ "small_neg_pos_5in_delay4",    small_neg_pos_5in_msgs,      0,        0,             1,         10,         ],
  [ "small_neg_pos_5in_delay5",    small_neg_pos_5in_msgs,      0,        0,             10,        1,          ],
  [ "small_neg_pos_5in_delay6",    small_neg_pos_5in_msgs,      0,        1,             0,         0,          ],
  [ "small_neg_pos_5in_delay7",    small_neg_pos_5in_msgs,      3,        4,             0,         0,          ],
  [ "small_neg_pos_5in_delay8",    small_neg_pos_5in_msgs,      20,       10,            0,         0,          ],
  [ "small_neg_pos_5in_delay9",    small_neg_pos_5in_msgs,      10,       4,             0,         0,          ], 
  
  [ "small_neg_zero_5in",           small_neg_zero_5in_msgs,      0,        0,             0,         0,          ],
  [ "small_neg_zero_5in_delay1",    small_neg_zero_5in_msgs,      0,        0,             0,         1,          ],
  [ "small_neg_zero_5in_delay2",    small_neg_zero_5in_msgs,      0,        0,             2,         0,          ],
  [ "small_neg_zero_5in_delay3",    small_neg_zero_5in_msgs,      0,        0,             3,         4,          ],
  [ "small_neg_zero_5in_delay4",    small_neg_zero_5in_msgs,      0,        0,             1,         10,         ],
  [ "small_neg_zero_5in_delay5",    small_neg_zero_5in_msgs,      0,        0,             10,        1,          ],
  [ "small_neg_zero_5in_delay6",    small_neg_zero_5in_msgs,      0,        1,             0,         0,          ],
  [ "small_neg_zero_5in_delay7",    small_neg_zero_5in_msgs,      3,        4,             0,         0,          ],
  [ "small_neg_zero_5in_delay8",    small_neg_zero_5in_msgs,      20,       10,            0,         0,          ],
  [ "small_neg_zero_5in_delay9",    small_neg_zero_5in_msgs,      10,       4,             0,         0,          ], 
  
  [ "large_neg_pos_5in",           large_neg_pos_5in_msgs,      0,        0,             0,         0,          ],
  [ "large_neg_pos_5in_delay1",    large_neg_pos_5in_msgs,      0,        0,             0,         1,          ],
  [ "large_neg_pos_5in_delay2",    large_neg_pos_5in_msgs,      0,        0,             2,         0,          ],
  [ "large_neg_pos_5in_delay3",    large_neg_pos_5in_msgs,      0,        0,             3,         4,          ],
  [ "large_neg_pos_5in_delay4",    large_neg_pos_5in_msgs,      0,        0,             1,         10,         ],
  [ "large_neg_pos_5in_delay5",    large_neg_pos_5in_msgs,      0,        0,             10,        1,          ],
  [ "large_neg_pos_5in_delay6",    large_neg_pos_5in_msgs,      0,        1,             0,         0,          ],
  [ "large_neg_pos_5in_delay7",    large_neg_pos_5in_msgs,      3,        4,             0,         0,          ],
  [ "large_neg_pos_5in_delay8",    large_neg_pos_5in_msgs,      20,       10,            0,         0,          ],
  [ "large_neg_pos_5in_delay9",    large_neg_pos_5in_msgs,      10,       4,             0,         0,          ], 
  
  [ "large_neg_zero_5in",           large_neg_zero_5in_msgs,      0,        0,             0,         0,          ],
  [ "large_neg_zero_5in_delay1",    large_neg_zero_5in_msgs,      0,        0,             0,         1,          ],
  [ "large_neg_zero_5in_delay2",    large_neg_zero_5in_msgs,      0,        0,             2,         0,          ],
  [ "large_neg_zero_5in_delay3",    large_neg_zero_5in_msgs,      0,        0,             3,         4,          ],
  [ "large_neg_zero_5in_delay4",    large_neg_zero_5in_msgs,      0,        0,             1,         10,         ],
  [ "large_neg_zero_5in_delay5",    large_neg_zero_5in_msgs,      0,        0,             10,        1,          ],
  [ "large_neg_zero_5in_delay6",    large_neg_zero_5in_msgs,      0,        1,             0,         0,          ],
  [ "large_neg_zero_5in_delay7",    large_neg_zero_5in_msgs,      3,        4,             0,         0,          ],
  [ "large_neg_zero_5in_delay8",    large_neg_zero_5in_msgs,      20,       10,            0,         0,          ],
  [ "large_neg_zero_5in_delay9",    large_neg_zero_5in_msgs,      10,       4,             0,         0,          ], 
  
  
  #===============================================================================================================
  # 10 Input tests Postive / Zero
  #===============================================================================================================
  [ "small_pos_pos_10in",           small_pos_pos_10in_msgs,      0,        0,             0,         0,          ],
  [ "small_pos_pos_10in_delay1",    small_pos_pos_10in_msgs,      0,        0,             0,         1,          ],
  [ "small_pos_pos_10in_delay2",    small_pos_pos_10in_msgs,      0,        0,             2,         0,          ],
  [ "small_pos_pos_10in_delay3",    small_pos_pos_10in_msgs,      0,        0,             3,         4,          ],
  [ "small_pos_pos_10in_delay4",    small_pos_pos_10in_msgs,      0,        0,             1,         10,         ],
  [ "small_pos_pos_10in_delay5",    small_pos_pos_10in_msgs,      0,        0,             10,        1,          ],
  [ "small_pos_pos_10in_delay6",    small_pos_pos_10in_msgs,      0,        1,             0,         0,          ],
  [ "small_pos_pos_10in_delay7",    small_pos_pos_10in_msgs,      3,        4,             0,         0,          ],
  [ "small_pos_pos_10in_delay8",    small_pos_pos_10in_msgs,      20,       10,            0,         0,          ],
  [ "small_pos_pos_10in_delay9",    small_pos_pos_10in_msgs,      10,       4,             0,         0,          ], 
  
  [ "small_pos_zero_10in",           small_pos_zero_10in_msgs,      0,        0,             0,         0,          ],
  [ "small_pos_zero_10in_delay1",    small_pos_zero_10in_msgs,      0,        0,             0,         1,          ],
  [ "small_pos_zero_10in_delay2",    small_pos_zero_10in_msgs,      0,        0,             2,         0,          ],
  [ "small_pos_zero_10in_delay3",    small_pos_zero_10in_msgs,      0,        0,             3,         4,          ],
  [ "small_pos_zero_10in_delay4",    small_pos_zero_10in_msgs,      0,        0,             1,         10,         ],
  [ "small_pos_zero_10in_delay5",    small_pos_zero_10in_msgs,      0,        0,             10,        1,          ],
  [ "small_pos_zero_10in_delay6",    small_pos_zero_10in_msgs,      0,        1,             0,         0,          ],
  [ "small_pos_zero_10in_delay7",    small_pos_zero_10in_msgs,      3,        4,             0,         0,          ],
  [ "small_pos_zero_10in_delay8",    small_pos_zero_10in_msgs,      20,       10,            0,         0,          ],
  [ "small_pos_zero_10in_delay9",    small_pos_zero_10in_msgs,      10,       4,             0,         0,          ], 
  
  [ "large_pos_pos_10in",           large_pos_pos_10in_msgs,      0,        0,             0,         0,          ],
  [ "large_pos_pos_10in_delay1",    large_pos_pos_10in_msgs,      0,        0,             0,         1,          ],
  [ "large_pos_pos_10in_delay2",    large_pos_pos_10in_msgs,      0,        0,             2,         0,          ],
  [ "large_pos_pos_10in_delay3",    large_pos_pos_10in_msgs,      0,        0,             3,         4,          ],
  [ "large_pos_pos_10in_delay4",    large_pos_pos_10in_msgs,      0,        0,             1,         10,         ],
  [ "large_pos_pos_10in_delay5",    large_pos_pos_10in_msgs,      0,        0,             10,        1,          ],
  [ "large_pos_pos_10in_delay6",    large_pos_pos_10in_msgs,      0,        1,             0,         0,          ],
  [ "large_pos_pos_10in_delay7",    large_pos_pos_10in_msgs,      3,        4,             0,         0,          ],
  [ "large_pos_pos_10in_delay8",    large_pos_pos_10in_msgs,      20,       10,            0,         0,          ],
  [ "large_pos_pos_10in_delay9",    large_pos_pos_10in_msgs,      10,       4,             0,         0,          ], 
  
  [ "large_pos_zero_10in",           large_pos_zero_10in_msgs,      0,        0,             0,         0,          ],
  [ "large_pos_zero_10in_delay1",    large_pos_zero_10in_msgs,      0,        0,             0,         1,          ],
  [ "large_pos_zero_10in_delay2",    large_pos_zero_10in_msgs,      0,        0,             2,         0,          ],
  [ "large_pos_zero_10in_delay3",    large_pos_zero_10in_msgs,      0,        0,             3,         4,          ],
  [ "large_pos_zero_10in_delay4",    large_pos_zero_10in_msgs,      0,        0,             1,         10,         ],
  [ "large_pos_zero_10in_delay5",    large_pos_zero_10in_msgs,      0,        0,             10,        1,          ],
  [ "large_pos_zero_10in_delay6",    large_pos_zero_10in_msgs,      0,        1,             0,         0,          ],
  [ "large_pos_zero_10in_delay7",    large_pos_zero_10in_msgs,      3,        4,             0,         0,          ],
  [ "large_pos_zero_10in_delay8",    large_pos_zero_10in_msgs,      20,       10,            0,         0,          ],
  [ "large_pos_zero_10in_delay9",    large_pos_zero_10in_msgs,      10,       4,             0,         0,          ],
  
  #===============================================================================================================
  # 10 Input tests Negative / Zero
  #===============================================================================================================
  [ "small_neg_pos_10in",           small_neg_pos_10in_msgs,      0,        0,             0,         0,          ],
  [ "small_neg_pos_10in_delay1",    small_neg_pos_10in_msgs,      0,        0,             0,         1,          ],
  [ "small_neg_pos_10in_delay2",    small_neg_pos_10in_msgs,      0,        0,             2,         0,          ],
  [ "small_neg_pos_10in_delay3",    small_neg_pos_10in_msgs,      0,        0,             3,         4,          ],
  [ "small_neg_pos_10in_delay4",    small_neg_pos_10in_msgs,      0,        0,             1,         10,         ],
  [ "small_neg_pos_10in_delay5",    small_neg_pos_10in_msgs,      0,        0,             10,        1,          ],
  [ "small_neg_pos_10in_delay6",    small_neg_pos_10in_msgs,      0,        1,             0,         0,          ],
  [ "small_neg_pos_10in_delay7",    small_neg_pos_10in_msgs,      3,        4,             0,         0,          ],
  [ "small_neg_pos_10in_delay8",    small_neg_pos_10in_msgs,      20,       10,            0,         0,          ],
  [ "small_neg_pos_10in_delay9",    small_neg_pos_10in_msgs,      10,       4,             0,         0,          ], 
  
  [ "small_neg_zero_10in",           small_neg_zero_10in_msgs,      0,        0,             0,         0,          ],
  [ "small_neg_zero_10in_delay1",    small_neg_zero_10in_msgs,      0,        0,             0,         1,          ],
  [ "small_neg_zero_10in_delay2",    small_neg_zero_10in_msgs,      0,        0,             2,         0,          ],
  [ "small_neg_zero_10in_delay3",    small_neg_zero_10in_msgs,      0,        0,             3,         4,          ],
  [ "small_neg_zero_10in_delay4",    small_neg_zero_10in_msgs,      0,        0,             1,         10,         ],
  [ "small_neg_zero_10in_delay5",    small_neg_zero_10in_msgs,      0,        0,             10,        1,          ],
  [ "small_neg_zero_10in_delay6",    small_neg_zero_10in_msgs,      0,        1,             0,         0,          ],
  [ "small_neg_zero_10in_delay7",    small_neg_zero_10in_msgs,      3,        4,             0,         0,          ],
  [ "small_neg_zero_10in_delay8",    small_neg_zero_10in_msgs,      20,       10,            0,         0,          ],
  [ "small_neg_zero_10in_delay9",    small_neg_zero_10in_msgs,      10,       4,             0,         0,          ], 
  
  [ "large_neg_pos_10in",           large_neg_pos_10in_msgs,      0,        0,             0,         0,          ],
  [ "large_neg_pos_10in_delay1",    large_neg_pos_10in_msgs,      0,        0,             0,         1,          ],
  [ "large_neg_pos_10in_delay2",    large_neg_pos_10in_msgs,      0,        0,             2,         0,          ],
  [ "large_neg_pos_10in_delay3",    large_neg_pos_10in_msgs,      0,        0,             3,         4,          ],
  [ "large_neg_pos_10in_delay4",    large_neg_pos_10in_msgs,      0,        0,             1,         10,         ],
  [ "large_neg_pos_10in_delay5",    large_neg_pos_10in_msgs,      0,        0,             10,        1,          ],
  [ "large_neg_pos_10in_delay6",    large_neg_pos_10in_msgs,      0,        1,             0,         0,          ],
  [ "large_neg_pos_10in_delay7",    large_neg_pos_10in_msgs,      3,        4,             0,         0,          ],
  [ "large_neg_pos_10in_delay8",    large_neg_pos_10in_msgs,      20,       10,            0,         0,          ],
  [ "large_neg_pos_10in_delay9",    large_neg_pos_10in_msgs,      10,       4,             0,         0,          ], 
  
  [ "large_neg_zero_10in",           large_neg_zero_10in_msgs,      0,        0,             0,         0,          ],
  [ "large_neg_zero_10in_delay1",    large_neg_zero_10in_msgs,      0,        0,             0,         1,          ],
  [ "large_neg_zero_10in_delay2",    large_neg_zero_10in_msgs,      0,        0,             2,         0,          ],
  [ "large_neg_zero_10in_delay3",    large_neg_zero_10in_msgs,      0,        0,             3,         4,          ],
  [ "large_neg_zero_10in_delay4",    large_neg_zero_10in_msgs,      0,        0,             1,         10,         ],
  [ "large_neg_zero_10in_delay5",    large_neg_zero_10in_msgs,      0,        0,             10,        1,          ],
  [ "large_neg_zero_10in_delay6",    large_neg_zero_10in_msgs,      0,        1,             0,         0,          ],
  [ "large_neg_zero_10in_delay7",    large_neg_zero_10in_msgs,      3,        4,             0,         0,          ],
  [ "large_neg_zero_10in_delay8",    large_neg_zero_10in_msgs,      20,       10,            0,         0,          ],
  [ "large_neg_zero_10in_delay9",    large_neg_zero_10in_msgs,      10,       4,             0,         0,          ] 
 


])

#-------------------------------------------------------------------------
# TestHarness
#-------------------------------------------------------------------------

@pytest.mark.parametrize( **test_case_table )
def test( test_params, cmdline_opts ):

  th = TestHarness( MacNew() )
  th.set_param("top.srcA.construct",
    msgs=test_params.msgs[0],
    # initial_delay=test_params.srcA_delay+3,
    interval_delay=test_params.srcA_delay )
  
  th.set_param("top.srcB.construct",
    msgs=test_params.msgs[1],
    # initial_delay=test_params.srcB_delay+3,
    interval_delay=test_params.srcB_delay )

  # th.set_param("top.sink.construct",
  #   msgs=test_params.msgs[2::5],
  #   initial_delay=test_params.result_sink_delay+3,
  #   interval_delay=test_params.result_sink_delay )
  
  th.set_param("top.sinkA.construct",
    msgs=test_params.msgs[2],
    # initial_delay=test_params.sinkA_delay+3,
    interval_delay=test_params.sinkA_delay )
  
  th.set_param("top.sinkB.construct",
    msgs=test_params.msgs[3],
    # initial_delay=test_params.sinkB_delay+3,
    interval_delay=test_params.sinkB_delay )
  
  # th.set_param("top.srcResult.construct",
  #   msgs=test_params.msgs[2],
  #   initial_delay=test_params.srcB_delay+3,
  #   interval_delay=test_params.srcB_delay)
   
     
  # th.top.giveresult = [0,0, 0,1]

  run_sim( th, cmdline_opts, duts=['mac'] )

