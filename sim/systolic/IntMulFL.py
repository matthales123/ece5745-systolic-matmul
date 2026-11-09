#=========================================================================
# Integer Multiplier FL Model
#=========================================================================

from pymtl3 import *
from pymtl3.stdlib.stream.ifcs import IStreamIfc, OStreamIfc
from pymtl3.stdlib.stream      import IStreamDeqAdapterFL, OStreamEnqAdapterFL

class IntMulFL( Component ):

  # Constructor

  def construct( s ):

    # Interface

    s.istreamA = IStreamIfc( Bits32 )
    s.istreamB = IStreamIfc( Bits32 )
    s.ostream = OStreamIfc( Bits32 )

    # Queue Adapters

    s.istreamA_q = IStreamDeqAdapterFL( Bits32 )
    s.istreamB_q = IStreamDeqAdapterFL( Bits32 )
    s.ostream_q = OStreamEnqAdapterFL( Bits32 )

    s.istreamA //= s.istreamA_q.istream
    s.istreamB //= s.istreamB_q.istream
    s.ostream //= s.ostream_q.ostream

    # FL block

    @update_once
    def block():
      if s.istreamA_q.deq.rdy() and s.istreamB_q.deq.rdy() and s.ostream_q.enq.rdy():
        msgA = s.istreamA_q.deq()
        msgB = s.istreamB_q.deq()
        s.ostream_q.enq( msgA * msgB )

  # Line tracing

  def line_trace( s ):
    return f"{s.istreamA}(){s.istreamB}(){s.ostream}"

