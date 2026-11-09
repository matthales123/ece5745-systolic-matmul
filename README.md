# ECE 5745 — Systolic Matrix Multiplication

Systolic matrix-multiplication coursework from ECE5745 group 14, with processing elements, array variants, PyMTL testbenches, TinyRV2 integration, and ASIC flow descriptions. `sim/systolic/` contains the standalone array; `sim/proc/` includes the processor-facing wrapper.

Requires the course-compatible PyMTL3 environment (`cornell-brg/pymtl3`, branch `ece4750-2022`), its Python dependencies, and compatible Verilator. The original course automation used Python 3.7 and Verilator 4.036; a current-toolchain port has not been validated. Create an isolated compatible environment before running:

```sh
mkdir -p sim/build
cd sim/build
pytest ../systolic/test -v
```

This is the original coursework project. The later [U55C port](https://github.com/matthales123/u55c-systolic-mmul) contains subsequent integration and verification work; its UVM/hardware results are not claimed for this archived course build. The historical `Makefile.verilator` has unresolved library-path/integration assumptions; use the course PyMTL workflow above as the starting point. ASIC flows require the external course ADK and licensed implementation tools. No fresh course regression was run during packaging.

Source comments retain course, instructor, library, and collaborator attribution. This repository does not grant a new license over third-party material. Generated logs, waveforms, debugging captures, and result directories are omitted from this public source edition.
