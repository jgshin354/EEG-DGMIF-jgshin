# Arduino LED control code for EEG signal acquisition

## 20190622-RGBLED

1. Color selection using button
2. 40Hz fixed light modulation

![](https://github.com/jgshin354/EEG-DGMIF-jgshin/blob/master/Arduino/repo/OP_20190622-RGBLED.PNG?raw=true)

### `int state_n `

- 0: Green, 1: Red, 2: Blue

### `TDTPIN(2 downto 0)`

- 0h: LED off 
- 1h: green PW, 2h: green CW 
- 3h: red PW,   4h: red CW 
- 5h: blue PW,  6h: blue CW 

## 20190624-RGBLED-freq_mod

1. Color selection using button / GRB
2. Frequency selection using button / 40Hz,  19Hz, 9Hz, 6Hz



## 20190624-RGBLED_seq_freq

1. Color selection using button / GRB
2. Sequential frequency variation /  40Hz,  19Hz, 9Hz, 6Hz

```Arduino C
void operationCode(){  //frequency, 40Hz, 19Hz, 9Hz, 6Hz
	frequency = 40; //Unit: Hz, it should be over 1 Hz.
	period = (1000/frequency); // (1sec / frequency)  
	pwOp();
	resting();

	frequency = 19; //Unit: Hz, it should be over 1 Hz.
	period = (1000/frequency); // (1sec / frequency)  
	pwOp();
	resting();

	frequency = 9; //Unit: Hz, it should be over 1 Hz.
	period = (1000/frequency); // (1sec / frequency)  
	pwOp();
	resting(); 

	frequency = 6; //Unit: Hz, it should be over 1 Hz.
	period = (1000/frequency); // (1sec / frequency)  
	pwOp();
	resting();    

	cwOp();
	resting();
	endRef();
}
```



## 20190713-RGBLED_seq_freq

1. **EEG Signal Acquisition Program**
2. iterate 60 times PW-Rest (20min) 





## 20210714-RGBLED-freq_mod-adv_freq

1. **Photobiomodulation only, no EEG Acquisition**
2. RED PW only
3. iterate 360 times 10 second PW (60min) 

  