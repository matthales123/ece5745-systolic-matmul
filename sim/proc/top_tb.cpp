// top_tb.cpp: Verilator testbench for mmulXcel accelerator
#include <verilated.h>
#include "VmmulXcel.h"
#include "verilated_vcd_c.h"
#include <vector>
#include <cstdint>
#include <iostream>

int main(int argc, char **argv) {
    Verilated::commandArgs(argc, argv);
    VmmulXcel* dut = new VmmulXcel;
    VerilatedVcdC* tfp = new VerilatedVcdC;
    dut->trace(tfp, 5);
    tfp->open("wave.vcd");

    // Simple memory model: 1K words
    const int MEM_SIZE = 1024;
    std::vector<uint32_t> mem(MEM_SIZE, 0);

    // Example: 2×2 matrices
    // A = [1 2; 3 4] at word addresses 0-3
    // B = [5 6; 7 8] at word addresses 4-7
    // We'll store C at word addresses 8-11
    mem[0] = 1; mem[1] = 2;
    mem[2] = 3; mem[3] = 4;
    mem[4] = 5; mem[5] = 6;
    mem[6] = 7; mem[7] = 8;

    // Clock & reset
    dut->clk = 0; dut->reset = 1;
    for (int i = 0; i < 5; i++) {
        dut->clk = !dut->clk; dut->eval(); tfp->dump(i);
    }
    dut->reset = 0;

    // Default handshake
    dut->xcelreq_rdy = 1;
    dut->memresp_rdy = 1;

    // Drive CSRs once after reset
    // CSR map:
    //  - CSR1 ([31:28]=1): A_base
    //  - CSR2 ([31:28]=2): B_base
    //  - CSR3 ([31:28]=3): C_base
    //  - CSR4 ([31:28]=4): dim
    //  - CSR0 ([31:28]=0): GO/STATUS

    // Write A_base=0, B_base=4*4=16, C_base=8*4=32, dim=2, GO=1
    auto write_csr = [&](uint8_t idx, uint32_t data) {
        while (!dut->xcelreq_rdy) {
            dut->clk = !dut->clk; dut->eval();
        }
        dut->xcelreq_val  = 1;
        dut->xcelreq_data = (idx << 28) | data;
        dut->clk = !dut->clk; dut->eval();
        dut->xcelreq_val  = 0;
    };

    write_csr(1, 0);      // A_base = address 0
    write_csr(2, 16);     // B_base = address 16
    write_csr(3, 32);     // C_base = address 32
    write_csr(4, 2);      // dim = 2
    write_csr(0, 1);      // GO = 1

    // Simulation time
    const int MAX_CYCLES = 200;
    for (int cycle = 0; cycle < MAX_CYCLES; cycle++) {
        // Drive clock
        dut->clk = !dut->clk;
        dut->eval();
        tfp->dump(2*cycle + (dut->clk?1:0));

        // Memory interface handling
        if (dut->memreq_val && dut->memreq_rdy) {
            uint32_t word_addr = dut->memreq_addr >> 2;
            if (dut->memreq_rw) {
                // Write result
                mem[word_addr] = dut->memreq_data;
                dut->memresp_val = 1;
            } else {
                // Read operand
                dut->memresp_data = mem[word_addr];
                dut->memresp_val = 1;
            }
        } else {
            dut->memresp_val = 0;
        }

        // Poll for completion via STATUS CSR0
        if (dut->xcelresp_val) {
            uint32_t resp = dut->xcelresp_data;
            if (resp & 0x1) {
                std::cout << "Matrix C results:\n";
                std::cout << "C[0]=" << mem[8]  << " \n";
                std::cout << "C[1]=" << mem[9]  << " \n";
                std::cout << "C[2]=" << mem[10] << " \n";
                std::cout << "C[3]=" << mem[11] << " \n";
                break;
            }
        }
    }

    tfp->close();
    delete dut;
    delete tfp;
    return 0;
}