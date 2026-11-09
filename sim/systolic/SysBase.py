#=========================================================================
# Multiply Accumulate unit - MAC
#=========================================================================

from pymtl3 import *
from pymtl3.passes.backends.verilog import *
from pymtl3.stdlib.stream.ifcs import IStreamIfc, OStreamIfc

class SysBase( VerilogPlaceholder, Component ):
  def construct( s, SIZE = 10 ):
    s.istreamA = [IStreamIfc( Bits33 ) for _ in range(int(SIZE))]
    s.istreamB = [IStreamIfc( Bits33 ) for _ in range(int(SIZE))]

    s.ostreamA = [OStreamIfc(  Bits33 ) for _ in range(int(SIZE))]
    s.ostreamB = [OStreamIfc(  Bits33 ) for _ in range(int(SIZE))]
    
    s.set_metadata( VerilogTranslationPass.explicit_module_name,
                    f"SysBase_{SIZE}x{SIZE}" )

    
