#=========================================================================
# IntMulBase_test
#=========================================================================

import pytest
import random

from pymtl3 import *
from pymtl3.stdlib.test_utils import run_sim
from systolic.IntMulBase import IntMulBase

#-------------------------------------------------------------------------
# Reuse tests from FL model
#-------------------------------------------------------------------------

from .IntMulFL_test import TestHarness, test_case_table

@pytest.mark.parametrize( **test_case_table )
def test( test_params, cmdline_opts ):

  th = TestHarness( IntMulBase() )

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

