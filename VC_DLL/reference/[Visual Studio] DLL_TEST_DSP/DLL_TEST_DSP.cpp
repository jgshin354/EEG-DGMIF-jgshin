// DLL_TEST_DSP.cpp : DLL 응용 프로그램을 위해 내보낸 함수를 정의합니다.
//
#pragma comment(lib,"ipps.lib")
#include "stdafx.h"
#include <omp.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "ipp.h"
#include "ipps.h"


#include "ippcore.h"
#include "ippvm.h"


// 4096 x 250 rescale, fft, windowing.

//int pts = 4096;
//int ascan = 500;
IppsFFTSpec_C_32f *FFTspecification=NULL;


//extern "C" __declspec(dllexport) void ARRAYfloor1D(float *cal, unsigned short *raw, unsigned char *rslt, float qh, float ql)
extern "C" __declspec(dllexport) void ARRAYfloor1D(float *cal, unsigned short *raw, unsigned char *rslt, float qh, float ql, int pts, int ascan)

{

	//float *Buffer = new float[pts*ascan];
	int *index = new int[pts];
	float *k2LambdaRate = new float[pts];
	int i, j, k;
	float temp1, temp2, temp3, temp4;

	int FFTOrder = log((float)pts) / log((float)2);
	float *win = NULL;
	win = new float[pts];
	ippsSet_32f(1, win, pts);
	ippsWinHann_32f_I(win, pts);

	
	Ipp8u *pMemSpec = 0;
	Ipp8u *pMemInit = 0;
	Ipp8u *pMemBuffer = 0;
	
	int sizeSpec = 0;
	int sizeInit = 0;
	int sizeBuffer = 0;
	int flag = IPP_FFT_NODIV_BY_ANY;
	ippsFFTGetSize_C_32f(FFTOrder, flag, ippAlgHintNone, &sizeSpec, &sizeInit, &sizeBuffer);
	pMemSpec = (Ipp8u*)ippMalloc(sizeSpec);
	
	if (sizeInit > 0)
		pMemInit = (Ipp8u*)ippMalloc(sizeInit);
	if (sizeBuffer > 0)
		pMemBuffer = (Ipp8u*)ippMalloc(sizeBuffer);
	ippsFFTInit_C_32f(&FFTspecification, FFTOrder, flag, ippAlgHintNone, pMemSpec, pMemInit);
	if (sizeInit > 0)
		ippFree(pMemInit);
	


	

	for (int x = 0; x < pts; x++) {
		if (cal[x] < 0)
			index[x] = 0;
		else if (cal[x] > pts-1)
			index[x] = pts - 1;
		else
			index[x] =  cal[x];
	}
	
	for (int x = 0; x<pts; x++) {
		if (cal[x]<0 || cal[x] >pts-1)
			k2LambdaRate[x] = 0;
		else
			k2LambdaRate[x] = cal[x] - index[x];
	}

	
	Ipp32f *data1Re, *data1Im, *data2Re, *data2Im, *spectrumRe, *spectrumIm, *magnitude;
	//ippsConvert_16u32f(raw, Buffer, pts*ascan);		
	
	
#pragma omp parallel private(i, j, k, data1Re, data1Im, data2Re, data2Im,spectrumRe, spectrumIm, magnitude, temp1, temp2, temp3, temp4)//, pOCTAscanSpec)
	{
		
		data1Re = (float*)calloc(pts, sizeof(float));
		data1Im = (float*)calloc(pts, sizeof(float));
		data2Re = (float*)calloc(pts, sizeof(float));
		data2Im = (float*)calloc(pts, sizeof(float));
		spectrumRe = (float*)calloc(pts, sizeof(float));
		spectrumIm = (float*)calloc(pts, sizeof(float));
		magnitude = (float*)calloc(pts, sizeof(float));
		ippsZero_32f(data1Im, pts);
		
		#pragma omp for
		for (i = 0; i < ascan; i++)
		{

			for (j = 0; j<pts; j++)
				data1Re[j] = raw[i*pts + j]-32767;//-(float)OCT_FringeBG[i*iCount+j];
			
								
			for (k = 0; k<pts; k++) //interpolation
			{
				temp1 = data1Re[index[k]];
				temp2 = data1Re[index[k] + 1];
				data2Re[k] = temp1 + (temp2 - temp1)*k2LambdaRate[k];//(klambda[k]-lambda[index[k]])/(lambda[index[k]+1]-lambda[index[k]]);//*cosfDispersion[j];
				temp3 = data1Im[index[k]];
				temp4 = data1Im[index[k] + 1];
				data2Im[k] = temp3 + (temp4 - temp3)*k2LambdaRate[k];//(klambda[k]-lambda[index[k]])/(lambda[index[k]+1]-lambda[index[k]]);//*cosfDispersion[j];
			}

			ippsMul_32f_I(win, data2Re, pts);
			ippsMul_32f_I(win, data2Im, pts);

			ippsFFTFwd_CToC_32f(data2Re, data2Im, spectrumRe, spectrumIm, FFTspecification, pMemBuffer);
			ippsMagnitude_32f(spectrumRe, spectrumIm, magnitude, pts);
			ippsLog10_32f_A11(magnitude, magnitude, pts);
			
			for (j = 0; j < pts; j++)
				rslt[i*pts + j] = (unsigned char) ((((float) magnitude[j] -ql) / (qh-ql)) *255);//-(float)OCT_FringeBG[i*iCount+j];
				
		}

		
		



		free(data1Re);
		free(data1Im);
		free(data2Re);
		free(data2Im);
		free(spectrumRe);
		free(spectrumIm);
		free(magnitude);
		ippFree(pMemBuffer);
		ippFree(pMemSpec);

	} 



	free(index);
	free(k2LambdaRate);

}
