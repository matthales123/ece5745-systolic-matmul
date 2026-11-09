#=========================================================================
# Multiply Accumulate unit - MAC with input stream queued
#=========================================================================

from pymtl3 import *
from pymtl3.passes.backends.verilog import *
from pymtl3.stdlib.stream.ifcs import IStreamIfc, OStreamIfc

class MacNew( VerilogPlaceholder, Component ):
  def construct( s ):
    s.istreamA = IStreamIfc( Bits33 )
    s.istreamB = IStreamIfc( Bits33 )
    # s.ostream = OStreamIfc(  Bits32 )
    s.ostreamA = OStreamIfc(  Bits33 )
    s.ostreamB = OStreamIfc(  Bits33 )
    # s.giveresult = IStreamIfc (Bits1)
