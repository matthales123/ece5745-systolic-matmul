//========================================================================
// Multiply accumalate unit
//========================================================================

`ifndef SYSTOLIC_MAC_V
`define SYSTOLIC_MAC_V

`include "vc/trace.v"
`include "vc/muxes.v"
`include "vc/arithmetic.v"
`include "systolic/IntMulBase.v"

module systolic_Mac
(
  input  logic        clk,
  input  logic        reset,

  input  logic        istreamA_val,
  output logic        istreamA_rdy,
  input  logic [31:0] istreamA_msg,

  input  logic        istreamB_val,
  output logic        istreamB_rdy,
  input  logic [31:0] istreamB_msg,

  output  logic        ostreamA_val,
  input   logic        ostreamA_rdy,
  output  logic [31:0] ostreamA_msg,

  output  logic        ostreamB_val,
  input   logic        ostreamB_rdy,
  output  logic [31:0] ostreamB_msg,

  output logic        ostream_val,
  input  logic        ostream_rdy,
  output logic [31:0] ostream_msg
);
  logic [31:0] mul_out;
  logic        mul_val_out;
  logic        mul_rdy_out;
  systolic_IntMulBase imul
  (
    .clk    (clk),
    .reset  (reset),

    .istreamA_val  (  istreamA_val  ),
    .istreamA_rdy  (  istreamA_rdy  ),
    .istreamA_msg  (  istreamA_msg  ),

    .istreamB_val  (   istreamB_val  ),
    .istreamB_rdy  (   istreamB_rdy  ),
    .istreamB_msg  (   istreamB_msg  ),

    .ostream_val   (   mul_val_out   ),
    .ostream_rdy   (   ostream_rdy   ),
    .ostream_msg   (   mul_out       )
  );

  logic [31:0] accumalator_in;
  logic [31:0] accumalator_out;
  logic [31:0] tempA;
  logic [31:0] tempB;
  logic        result_en;
  logic        tempA_val;
  logic        tempB_val;
  
  logic        temp_val;
  logic        temp_rdy;
  logic        temp_result;
  
  

  // assign result_en = mul_val_in && ostream_rdy ;

  // vc_SimpleAdder#(32)  adder (
    // .in0( mul_out        ), 
    // .in1( accumalator_out ), 
    // .out( accumalator_in )
  // );
  
  
  
  // logic mul_val_out;
  // logic mul_rdy_in;
  always_ff @ (posedge clk) 
  begin
    if ( reset ) begin
        accumalator_out <= 32'b0;
        tempA           <= 32'b0;
        tempB           <= 32'b0;
        // tempA_val       <= 1'b0;
        // tempB_val       <= 1'b0;
    end
    else begin
      if (mul_val_out && ostream_rdy) begin 
        accumalator_out  <= accumalator_out + mul_out;

        //temp_val <= mul_val_out;
      end
      if (mul_val_out && ostream_rdy ) begin
        temp_val  <= mul_val_out;

        // temp_rdy  <= ostream_rdy;
      end

      else begin
        temp_val  <= 0;
        // temp_rdy  <= 0;
      end
      if (istreamA_val && istreamB_val && istreamA_rdy && istreamB_rdy ) begin
        tempA     <= istreamA_msg;
        tempB     <= istreamB_msg;
        tempA_val <= istreamA_val;
        tempB_val <= istreamB_val;

        // mul_rdy_out  <= mul_rdy_in;
      end
    end
  end

  //assign temp_result = mul_val_out ?  accumalator_out : 32'b0 ;
  assign ostream_msg = accumalator_out;
  assign ostream_val = temp_val;
  assign ostreamA_val = (mul_val_out && ostream_rdy) ? tempA_val : 1'b0;
  assign ostreamB_val = (mul_val_out && ostream_rdy) ? tempB_val : 1'b0;
  assign ostreamA_msg = (mul_val_out && ostream_rdy) ? tempA     : 32'b0;
  assign ostreamB_msg = (mul_val_out && ostream_rdy) ? tempB     : 32'b0;
  // logic       ostreamA_temp_val_in;
  // logic       ostreamB_temp_val_in;
  // logic [31:0]ostreamA_temp_msg_in;
  // logic [31:0]ostreamB_temp_msg_in;

  // assign ostreamA_temp_val_in = (mul_val_out && ostream_rdy) ? tempA_val : 1'b0;
  // assign ostreamB_temp_val_in = (mul_val_out && ostream_rdy) ? tempB_val : 1'b0;
  // assign ostreamA_temp_msg_in = (mul_val_out && ostream_rdy) ? tempA     : 32'b0;
  // assign ostreamB_temp_msg_in = (mul_val_out && ostream_rdy) ? tempB     : 32'b0;

  // logic       ostreamA_temp_val_out;
  // logic       ostreamB_temp_val_out;
  // logic [31:0]ostreamA_temp_msg_out;
  // logic [31:0]ostreamB_temp_msg_out;

    // always_ff @ (posedge clk) 
  // begin
    // if ( reset ) begin
        // ostreamA_temp_val_out <= 1'b0;
        // ostreamB_temp_val_out <= 1'b0;
        // ostreamA_temp_msg_out <= 32'b0;
        // ostreamB_temp_msg_out <= 32'b0;
    // end
      // else begin
        // ostreamA_temp_val_out <= ostreamA_temp_val_in;        
        // ostreamB_temp_val_out <= ostreamB_temp_val_in;
        // ostreamA_temp_msg_out <= ostreamA_temp_msg_in;
        // ostreamB_temp_msg_out <= ostreamB_temp_msg_in;
// 
// 
// 
// 
// 
    // end
  // end

  
  // assign ostream_val = mul_val_out;
  // assign mul_rdy_in  = ostream_rdy;
  

  //----------------------------------------------------------------------
  // Line Tracing
  //----------------------------------------------------------------------

  `ifndef SYNTHESIS

  logic [`VC_TRACE_NBITS-1:0] str;
  logic [`VC_TRACE_NBITS-1:0] state_str;
  `VC_TRACE_BEGIN
  begin

    vc_trace.append_str( trace_str, "(" );
    $sformat( str, "%x", istreamA_msg );
    vc_trace.append_val_rdy_str( trace_str, istreamA_val, istreamA_rdy, str );
    vc_trace.append_str( trace_str, ")" );
    
    vc_trace.append_str( trace_str, "(" );
    $sformat( str, "%x", istreamB_msg );
    vc_trace.append_val_rdy_str( trace_str, istreamB_val, istreamB_rdy, str );
    vc_trace.append_str( trace_str, ")" );

    vc_trace.append_str( trace_str, "(" );
    $sformat( str, "%x", temp_val );
    vc_trace.append_str( trace_str, str );
    $sformat( str, " %x", mul_val_out );
    vc_trace.append_str( trace_str, str );

    vc_trace.append_str( trace_str, ")" );

    $sformat( str, "%x", ostream_msg );
    vc_trace.append_val_rdy_str( trace_str, ostream_val, ostream_rdy, str );

    $sformat( str, "%x", ostreamA_msg );
    vc_trace.append_val_rdy_str( trace_str, ostreamA_val, ostreamA_rdy, str );

    $sformat( str, "%x", ostreamB_msg );
    vc_trace.append_val_rdy_str( trace_str, ostreamB_val, ostreamB_rdy, str );

  end
  `VC_TRACE_END

  `endif /* SYNTHESIS */

endmodule

`endif /* SYSTOLIC_MAC_V */

