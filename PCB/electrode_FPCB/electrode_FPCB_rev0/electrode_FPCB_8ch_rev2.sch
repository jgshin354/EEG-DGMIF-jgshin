EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr User 5827 4134
encoding utf-8
Sheet 1 1
Title "VR EEG electrode pad / 8 channel / JGSHIN"
Date ""
Rev "2.0"
Comp "DGMIF"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L jgshin_KiCad_lib:electrode_PAD CN1
U 1 1 60FE3EEE
P 1400 850
F 0 "CN1" H 1081 904 50  0000 R CNN
F 1 "electrode_PAD" H 1081 995 50  0000 R CNN
F 2 "jgshin_KiCad_lib:electrode_PAD" H 1450 800 50  0001 C CNN
F 3 "" H 1450 800 50  0001 C CNN
	1    1400 850 
	1    0    0    -1  
$EndComp
$Comp
L jgshin_KiCad_lib:electrode_PAD CN2
U 1 1 60FE5BAB
P 1400 1100
F 0 "CN2" H 1081 1154 50  0000 R CNN
F 1 "electrode_PAD" H 1081 1245 50  0000 R CNN
F 2 "jgshin_KiCad_lib:electrode_PAD" H 1450 1050 50  0001 C CNN
F 3 "" H 1450 1050 50  0001 C CNN
	1    1400 1100
	1    0    0    -1  
$EndComp
$Comp
L jgshin_KiCad_lib:electrode_PAD CN3
U 1 1 60FE5E40
P 1400 1350
F 0 "CN3" H 1081 1404 50  0000 R CNN
F 1 "electrode_PAD" H 1081 1495 50  0000 R CNN
F 2 "jgshin_KiCad_lib:electrode_PAD" H 1450 1300 50  0001 C CNN
F 3 "" H 1450 1300 50  0001 C CNN
	1    1400 1350
	1    0    0    -1  
$EndComp
$Comp
L jgshin_KiCad_lib:electrode_PAD CN6
U 1 1 60FE651A
P 2950 850
F 0 "CN6" H 2631 904 50  0000 R CNN
F 1 "electrode_PAD" H 2631 995 50  0000 R CNN
F 2 "jgshin_KiCad_lib:electrode_PAD" H 3000 800 50  0001 C CNN
F 3 "" H 3000 800 50  0001 C CNN
	1    2950 850 
	1    0    0    -1  
$EndComp
$Comp
L jgshin_KiCad_lib:FFC0.5x10 CN7
U 1 1 60FEB38A
P 4700 2250
F 0 "CN7" H 4928 2876 50  0000 L CNN
F 1 "FFC0.5x10" H 4928 2785 50  0000 L CNN
F 2 "jgshin_KiCad_lib:FFC cable 0.5 x 10" H 4700 2250 50  0001 C CNN
F 3 "" H 4700 2250 50  0001 C CNN
	1    4700 2250
	1    0    0    -1  
$EndComp
$Comp
L jgshin_KiCad_lib:electrode_PAD CN5
U 1 1 60FE631A
P 1400 1850
F 0 "CN5" H 1081 1904 50  0000 R CNN
F 1 "electrode_PAD" H 1081 1995 50  0000 R CNN
F 2 "jgshin_KiCad_lib:electrode_PAD" H 1450 1800 50  0001 C CNN
F 3 "" H 1450 1800 50  0001 C CNN
	1    1400 1850
	1    0    0    -1  
$EndComp
$Comp
L jgshin_KiCad_lib:electrode_PAD CN4
U 1 1 60FE60B4
P 1400 1600
F 0 "CN4" H 1081 1654 50  0000 R CNN
F 1 "electrode_PAD" H 1081 1745 50  0000 R CNN
F 2 "jgshin_KiCad_lib:electrode_PAD" H 1450 1550 50  0001 C CNN
F 3 "" H 1450 1550 50  0001 C CNN
	1    1400 1600
	1    0    0    -1  
$EndComp
$Comp
L jgshin_KiCad_lib:electrode_PAD CN9
U 1 1 60FED536
P 2950 1350
F 0 "CN9" H 2631 1404 50  0000 R CNN
F 1 "electrode_PAD" H 2631 1495 50  0000 R CNN
F 2 "jgshin_KiCad_lib:electrode_PAD" H 3000 1300 50  0001 C CNN
F 3 "" H 3000 1300 50  0001 C CNN
	1    2950 1350
	1    0    0    -1  
$EndComp
$Comp
L jgshin_KiCad_lib:electrode_PAD CN8
U 1 1 60FED53C
P 2950 1100
F 0 "CN8" H 2631 1154 50  0000 R CNN
F 1 "electrode_PAD" H 2631 1245 50  0000 R CNN
F 2 "jgshin_KiCad_lib:electrode_PAD" H 3000 1050 50  0001 C CNN
F 3 "" H 3000 1050 50  0001 C CNN
	1    2950 1100
	1    0    0    -1  
$EndComp
Wire Wire Line
	1700 750  1950 750 
Text Label 1750 750  0    50   ~ 0
Ref
Wire Wire Line
	1700 1000 1950 1000
Text Label 1750 1000 0    50   ~ 0
Gnd
Wire Wire Line
	1700 1250 1950 1250
Text Label 1750 1250 0    50   ~ 0
Ch1
Wire Wire Line
	1700 1500 1950 1500
Text Label 1750 1500 0    50   ~ 0
Ch2
Wire Wire Line
	1700 1750 1950 1750
Text Label 1750 1750 0    50   ~ 0
Ch3
Wire Wire Line
	3250 750  3500 750 
Text Label 3300 750  0    50   ~ 0
Ch4
Wire Wire Line
	3250 1000 3500 1000
Text Label 3300 1000 0    50   ~ 0
Ch5
Wire Wire Line
	3250 1250 3500 1250
Text Label 3300 1250 0    50   ~ 0
Ch6
$Comp
L jgshin_KiCad_lib:electrode_PAD CN11
U 1 1 60FF11E4
P 2950 1850
F 0 "CN11" H 2631 1904 50  0000 R CNN
F 1 "electrode_PAD" H 2631 1995 50  0000 R CNN
F 2 "jgshin_KiCad_lib:electrode_PAD" H 3000 1800 50  0001 C CNN
F 3 "" H 3000 1800 50  0001 C CNN
	1    2950 1850
	1    0    0    -1  
$EndComp
$Comp
L jgshin_KiCad_lib:electrode_PAD CN10
U 1 1 60FF11EA
P 2950 1600
F 0 "CN10" H 2631 1654 50  0000 R CNN
F 1 "electrode_PAD" H 2631 1745 50  0000 R CNN
F 2 "jgshin_KiCad_lib:electrode_PAD" H 3000 1550 50  0001 C CNN
F 3 "" H 3000 1550 50  0001 C CNN
	1    2950 1600
	1    0    0    -1  
$EndComp
Wire Wire Line
	3250 1500 3500 1500
Text Label 3300 1500 0    50   ~ 0
Ch7
Wire Wire Line
	3250 1750 3500 1750
Text Label 3300 1750 0    50   ~ 0
Ch8
Wire Wire Line
	4350 1600 4600 1600
Text Label 4400 1600 0    50   ~ 0
Ref
Wire Wire Line
	4350 1700 4600 1700
Text Label 4400 1700 0    50   ~ 0
Gnd
Wire Wire Line
	4600 1900 4350 1900
Text Label 4550 1900 2    50   ~ 0
Ch4
Wire Wire Line
	4600 1300 4350 1300
Text Label 4550 1300 2    50   ~ 0
Ch5
Wire Wire Line
	4600 2000 4350 2000
Text Label 4550 2000 2    50   ~ 0
Ch6
Wire Wire Line
	4600 1200 4350 1200
Text Label 4550 1200 2    50   ~ 0
Ch7
Wire Wire Line
	4600 2100 4350 2100
Text Label 4550 2100 2    50   ~ 0
Ch8
Text Label 4550 1400 2    50   ~ 0
Ch3
Wire Wire Line
	4600 1400 4350 1400
Text Label 4550 1800 2    50   ~ 0
Ch2
Wire Wire Line
	4600 1800 4350 1800
Text Label 4550 1500 2    50   ~ 0
Ch1
Wire Wire Line
	4600 1500 4350 1500
$EndSCHEMATC
