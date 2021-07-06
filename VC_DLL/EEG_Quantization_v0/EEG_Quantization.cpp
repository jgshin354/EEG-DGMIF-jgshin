#include "pch.h"
#include <utility>
#include <limits.h>
#include "fftw3.h"
#include "EEG_Quantization.h"


// DLL internal state variables:
static unsigned int n_channel = 4;
static unsigned int n_pts = 256;
static unsigned int s_freq = 256;
/* Delta		: 0.5~3Hz
Theta : 4~7Hz
Alpha : 8~12
SMR : 12~15
Low Beta : 13~18
Mid Beta : 16~20
High Beta : 19~30
Beta : 13~30
Gamma : 30ÀÌ»ף(30~50) */


double freq_sum(double* spectrum, int sample_freq, int number_pts, int freq_st, int freq_end)
{
	double sum_rslt = 0;
	int ind_st, ind_end;
	ind_st = int(freq_st * number_pts / sample_freq);
	ind_end = int(freq_end * number_pts / sample_freq);
	for (int i = ind_st; i < ind_end + 1; i++)
		sum_rslt += spectrum[i];
	return sum_rslt;
}

void get_stress_index(unsigned int* raw, float* stress_index)
{
	float* delta = new float[n_channel];
	float* theta = new float[n_channel];
	float* alpha = new float[n_channel];
	float* SMR = new float[n_channel];
	float* LowBeta = new float[n_channel];
	float* MidBeta = new float[n_channel];
	float* HighBeta = new float[n_channel];
	float* beta = new float[n_channel];
	float* gamma = new float[n_channel];
	float* spectrum_r = new float[n_pts];


	prep_freq_div(raw, delta, theta, alpha, SMR, LowBeta, MidBeta, HighBeta, beta, gamma, spectrum_r);

	for (unsigned int i = 0; i < n_channel; i++)
		stress_index[i] = theta[i] / MidBeta[i];

	free(delta);
	free(theta);
	free(alpha);
	free(SMR);
	free(LowBeta);
	free(MidBeta);
	free(HighBeta);
	free(beta);
	free(gamma);
	free(spectrum_r);

}



void get_depression_index(unsigned int* raw, float depression_index)
{
	float* delta = new float[n_channel];
	float* theta = new float[n_channel];
	float* alpha = new float[n_channel];
	float* SMR = new float[n_channel];
	float* LowBeta = new float[n_channel];
	float* MidBeta = new float[n_channel];
	float* HighBeta = new float[n_channel];
	float* beta = new float[n_channel];
	float* gamma = new float[n_channel];
	float* spectrum_r = new float[n_pts];


	prep_freq_div(raw, delta, theta, alpha, SMR, LowBeta, MidBeta, HighBeta, beta, gamma, spectrum_r);
	
	depression_index = (((alpha[0] + alpha[2]) / 2) - ((alpha[1] + alpha[3]) / 2)) / (((alpha[0] + alpha[2]) / 2) + ((alpha[1] + alpha[3]) / 2));
	
	free(delta);
	free(theta);
	free(alpha);
	free(SMR);
	free(LowBeta);
	free(MidBeta);
	free(HighBeta);
	free(beta);
	free(gamma);
	free(spectrum_r);

}
void get_attention_index(unsigned int* raw, float* attention_index)
{
	float* delta = new float[n_channel];
	float* theta = new float[n_channel];
	float* alpha = new float[n_channel];
	float* SMR = new float[n_channel];
	float* LowBeta = new float[n_channel];
	float* MidBeta = new float[n_channel];
	float* HighBeta = new float[n_channel];
	float* beta = new float[n_channel];
	float* gamma = new float[n_channel];
	float* spectrum_r = new float[n_pts];


	prep_freq_div(raw, delta, theta, alpha, SMR, LowBeta, MidBeta, HighBeta, beta, gamma, spectrum_r);

	for (unsigned int i = 0; i < n_channel; i++)
		attention_index[i] = (SMR[i] + MidBeta[i]) / theta[i];
	


	free(delta);
	free(theta);
	free(alpha);
	free(SMR);
	free(LowBeta);
	free(MidBeta);
	free(HighBeta);
	free(beta);
	free(gamma);
	free(spectrum_r);
}
void get_quantized_index(unsigned int* raw, float stress_index, float depression_index, float attention_index)
{
	float* delta = new float[n_channel];
	float* theta = new float[n_channel];
	float* alpha = new float[n_channel];
	float* SMR = new float[n_channel];
	float* LowBeta = new float[n_channel];
	float* MidBeta = new float[n_channel];
	float* HighBeta = new float[n_channel];
	float* beta = new float[n_channel];
	float* gamma = new float[n_channel];
	float* spectrum_r = new float[n_pts];

	stress_index = 0;
	depression_index = 0;
	attention_index = 0;

	prep_freq_div(raw, delta, theta, alpha, SMR, LowBeta, MidBeta, HighBeta, beta, gamma, spectrum_r);

	for (unsigned int i = 0; i < n_channel; i++)
		stress_index += (theta[i] / MidBeta[i])/n_channel;
	
	depression_index = (((alpha[0] + alpha[2]) / 2) - ((alpha[1] + alpha[3]) / 2)) / (((alpha[0] + alpha[2]) / 2) + ((alpha[1] + alpha[3]) / 2));


	for (unsigned int i = 0; i < n_channel; i++)
		attention_index += ((SMR[i] + MidBeta[i]) / theta[i])/n_channel;

	free(delta);
	free(theta);
	free(alpha);
	free(SMR);
	free(LowBeta);
	free(MidBeta);
	free(HighBeta);
	free(beta);
	free(gamma);
	free(spectrum_r);
}






void prep_freq_div(unsigned int* raw, float* delta, float* theta, float* alpha, float* SMR, float* LowBeta, float* MidBeta, float* HighBeta, float* beta, float* gamma, float* spectrum_r)
{
	double* data1Re = new double[n_pts];
	double* magnitude = new double[n_pts];
	double* temp_spectrum = new double[n_pts];
	fftw_plan fft_p = fftw_plan_r2r_1d(n_pts, data1Re, temp_spectrum, FFTW_R2HC, FFTW_ESTIMATE);
	
	memset(delta, 0, sizeof(float) * n_channel);
	memset(theta, 0, sizeof(float) * n_channel);
	memset(alpha, 0, sizeof(float) * n_channel);
	memset(SMR, 0, sizeof(float) * n_channel);
	memset(LowBeta, 0, sizeof(float) * n_channel);
	memset(MidBeta, 0, sizeof(float) * n_channel);
	memset(HighBeta, 0, sizeof(float) * n_channel);
	memset(beta, 0, sizeof(float) * n_channel);
	memset(gamma, 0, sizeof(float) * n_channel);
	
	for (unsigned int i = 0; i < n_channel; i++) {
		for (unsigned int j = 0; j < n_pts; j++)
			data1Re[j] = (double)raw[i * n_pts + j];
		fftw_execute_r2r(fft_p, data1Re, temp_spectrum);

		magnitude[0] = temp_spectrum[0];

		for (unsigned int pos1 = 1, pos2 = n_pts - 1; pos1 < n_pts/2; pos1++, pos2--) 
			magnitude[pos1] = sqrt(temp_spectrum[pos1] * temp_spectrum[pos1] + temp_spectrum[pos2] * temp_spectrum[pos2]);
		for (unsigned int pos2 = n_pts / 2; pos2 < n_pts; pos2++)
			magnitude[pos2] = 0;
		for (unsigned int j = 0; j < n_pts; j++)
			spectrum_r[i * n_pts + j] = (float)magnitude[j];

		delta[i] = (float) freq_sum(magnitude, s_freq, n_pts, 1, 3);
		theta[i] = (float) freq_sum(magnitude, s_freq, n_pts, 4, 7);
		alpha[i] = (float)freq_sum(magnitude, s_freq, n_pts, 8, 12);
		SMR[i] = (float)freq_sum(magnitude, s_freq, n_pts, 12, 15);
		LowBeta[i] = (float)freq_sum(magnitude, s_freq, n_pts, 13, 18);
		MidBeta[i] = (float)freq_sum(magnitude, s_freq, n_pts, 16, 20);
		HighBeta[i] = (float)freq_sum(magnitude, s_freq, n_pts, 19, 30);
		beta[i] = (float)freq_sum(magnitude, s_freq, n_pts, 13, 30);
		gamma[i] = (float)freq_sum(magnitude, s_freq, n_pts, 30, 50);

	}


	
	free(data1Re);
	free(magnitude);
	free(temp_spectrum);

}



void prep_freq_div_var(unsigned int n_ch, unsigned int n_pts, unsigned int* raw, float* rslt)
{

}