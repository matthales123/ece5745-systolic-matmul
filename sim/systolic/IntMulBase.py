#=========================================================================
# 2 input IntMulBase PyMTL3 Wrapper
#=========================================================================

from pymtl3 import *
from pymtl3.passes.backends.verilog import *
from pymtl3.stdlib.stream.ifcs import IStreamIfc, OStreamIfc

class IntMulBase( VerilogPlaceholder, Component ):
  def construct( s ):
    s.istreamA = IStreamIfc( Bits32 )
    s.istreamB = IStreamIfc( Bits32 )
    s.ostream = OStreamIfc(  Bits32 )

