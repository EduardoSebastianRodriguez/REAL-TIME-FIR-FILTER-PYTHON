//Class which implements real time FIR filters
//by selecting the cut-off frequencies,
//the number of taps,
//and the type of the filter:
//	*High pass
//	*Low pass
//	*Stop band
//	*Pass band
//
//This is the header file
//
//Created by Eduardo Sebastián
//Date: 19/11/2017

#ifndef FIR_H
#define FIR_H

#include "vector"

//Class
class FIR{
	
	//Atributes
	private:
	int                 taps;//number of coefficients of the FIR filter
	std::vector<float> coeff;//coefficients of the FIR filter
	char                type;//type of the FIR filter: 'l' or 'L'= lowpass
		                 //		                  'h' or 'H'= highpass
		      		 //		                  's' or 'S'= stopband
	              		 //			          'p' or 'P'= passband			    
	std::vector<float> freq; //Normalized cut-off frequencies
	std::vector<float> buff; //buffer implementing the M(taps) delays	
	
	//Constructor
	public: FIR(){}

	//Methods
	public:
	int     getTaps();		  	      //Gets the number of taps of the filter
	double  getCoeff(int i);	              //Gets the coefficient of index i
	char    getType();		 	      //Gets the type of the filter
	double  getFreq(int i);		  	      //Gets the cut-off frequency i: if the filter is first order, i=0
	double  getBuffer(int i);	              //Gets the buffered value of index i
	void    setTaps(int M);            	      //Sets the number of taps of the filter
	void    setCoeff(double x, int i); 	      //Sets the coefficient of the position i with the value x
	void    setType(char a);		      //Sets the type of the filter
	void    setFreq(double x, int i);  	      //Sets the cut-off frequency of index i: if the filter is first order, i=0
	void    setBuffer(double x, int i);	      //Sets the value of index i of the buffer to x
	void    lowpass(int M,double f);              //Generates the coefficients of a low pass filter with cut-off frequency f
	void    highpass(int M,double f);             //Generates the coefficients of a high pass filter with cut-off frequency f
	void    stopband(int M, double f1, double f2);//Generates the coefficients of a stop band filter with cut-off frequencies f
	void    passband(int M, double f1, double f2);//Generates the coefficients of a pass band filter with cut-off frequencies f
	double  filter(double x);	  	      //Filters the scalar input x by using the coefficients of the filter and returns a 						              //scalar output
					              //If no coefficient generator method is applied, the coefficients are all zero.
};
	

#endif

