README
------
# REAL-TIME-FIR-FILTER-PYTHON
This repository contains a Python library which implements real time FIR filters. The library was optimized in C++. A demo and a howto are also provided
Elements of the repository:

    'FIR.py': first part of the PYTHON library, implements real time FIR filters
    '_FIR.so': second part of the PYTHON library, shared library function
    'HOWTO.txt': document with the instructions of how to use the library, the demo and general info
    'DOCUMENTATION.txt': compendium of the atributes, constructor and methods of the class FIR contained in the library
    'BASE': folder which contains the original C++ files and the interface for SWIG to convert the library into PYTHON
        *'FIR.cpp'
        *'FIR.h'
        *'FIR.i'
        *'STEPS.txt': describes the process in the terminal of LINUX for using SWIG and generate the PYTHON library
     'DEMO': folder which contains a demo showing an example of filtering with the input and output files
        *'DEMO.py'
        *'ecg.dat'
        *'ecg_filtered.dat'
        *'ecg.pdf'
        *'ecg_filtered.pdf'
        *'single_heartbeat.pdf'
        *'single_heartbeat_filtered.pdf'
        *'FIR.py'
        *'_FIR.so'

The module implements real time FIR filters, which are one of the most widespread digital filters. The module does both the generation of the coefficients of the filter and the filtering operation. In the case of the filtering, the input is not an array but a single scalar value, returning another single scalar value. This means the class works either with a saved signal or in a real time system, in which the computer recieves one single real value at specific instants of time, giving as an output the corresponding filtered real value from passing troughout the filter.

Descriptions of the behaviour, structure and demo are provided in 'HOWTO.txt' and 'DOCUMENTATION.txt'

Have a nice day!

Eduardo
