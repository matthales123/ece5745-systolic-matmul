#=========================================================================
# Multiply Accumulate unit - MAC
#=========================================================================

from pymtl3 import *
from pymtl3.passes.backends.verilog import *
from pymtl3.stdlib.stream.ifcs import IStreamIfc, OStreamIfc

class MacAlt( VerilogPlaceholder, Component ):
  def construct( s ):
    s.istreamA = IStreamIfc( Bits32 )
    s.istreamB = IStreamIfc( Bits32 )
    # s.ostream = OStreamIfc(  Bits32 )
    s.ostreamA = OStreamIfc(  Bits32 )
    s.ostreamB = OStreamIfc(  Bits32 )
    s.giveresult = IStreamIfc (Bits1)
