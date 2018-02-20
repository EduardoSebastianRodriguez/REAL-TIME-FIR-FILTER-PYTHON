all:
	swig -python -c++ FIR.i
	g++ -fPIC -c FIR.cpp FIR_wrap.cxx -I/usr/include/python3.5
	g++ -shared FIR.o FIR_wrap.o -o _FIR.so
	cp _FIR.so ..
	cp FIR.py ..

clean:
	rm -f *.so *.o *wrap* rm ../*FIR.*
