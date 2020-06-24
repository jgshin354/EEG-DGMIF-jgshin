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



