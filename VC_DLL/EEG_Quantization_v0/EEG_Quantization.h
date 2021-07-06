#pragma once

#pragma once

#ifdef EEG_QUANTIZATION_EXPORTS
#define EEG_Quantization_API __declspec(dllexport)
#else
#define EEG_Quantization_API __declspec(dllimport)
#endif



/*
    Delta		: 0.5~3Hz
    Theta : 4~7Hz
    Alpha : 8~12
    SMR : 12~15
    Low Beta : 13~18
    Mid Beta : 16~20
    High Beta : 19~30
    Beta : 13~30
    Gamma : 30ÀÌ»ף(30~50)
*/
extern "C" EEG_Quantization_API void prep_freq_div(
    unsigned int* raw, float* delta, float* theta, float* alpha, float* SMR, float* LowBeta, float* MidBeta, float* HighBeta, float* beta, float* gamma, float* spectrum_r);


extern "C" EEG_Quantization_API void prep_freq_div_var(unsigned int n_ch, unsigned int n_pts, unsigned int* raw, float* rslt);
extern "C" EEG_Quantization_API void get_stress_index(unsigned int* raw, float* stress_index);
extern "C" EEG_Quantization_API void get_depression_index(unsigned int* raw, float depression_index);
extern "C" EEG_Quantization_API void get_attention_index(unsigned int* raw, float* attention_index);
extern "C" EEG_Quantization_API void get_quantized_index(unsigned int* raw, float stress_index, float depression_index, float attention_index);
