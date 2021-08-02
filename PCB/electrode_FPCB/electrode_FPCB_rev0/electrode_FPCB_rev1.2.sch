EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr User 5827 4134
encoding utf-8
Sheet 1 1
Title "VR EEG electrode pad / JGSHIN"
Date ""
Rev "1.2"
Comp "DGMIF"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L electrode_FPCB_rev0-rescue:electrode_PAD-jgshin_KiCad_lib CN1
U 1 1 60FE3EEE
P 2050 1000
F 0 "CN1" H 1731 1054 50  0000 R CNN
F 1 "electrode_PAD" H 1731 1145 50  0000 R CNN
F 2 "jgshin_KiCad_lib:electrode_PAD" H 2100 950 50  0001 C CNN
F 3 "" H 2100 950 50  0001 C CNN
	1    2050 1000
	1    0    0    -1  
$EndComp
$Comp
L electrode_FPCB_rev0-rescue:electrode_PAD-jgshin_KiCad_lib CN2
U 1 1 60FE5BAB
P 2050 1250
F 0 "CN2" H 1731 1304 50  0000 R CNN
F 1 "electrode_PAD" H 1731 1395 50  0000 R CNN
F 2 "jgshin_KiCad_lib:electrode_PAD" H 2100 1200 50  0001 C CNN
F 3 "" H 2100 1200 50  0001 C CNN
	1    2050 1250
	1    0    0    -1  
$EndComp
$Comp
L electrode_FPCB_rev0-rescue:electrode_PAD-jgshin_KiCad_lib CN3
U 1 1 60FE5E40
P 2050 1500
F 0 "CN3" H 1731 1554 50  0000 R CNN
F 1 "electrode_PAD" H 1731 1645 50  0000 R CNN
F 2 "jgshin_KiCad_lib:electrode_PAD" H 2100 1450 50  0001 C CNN
F 3 "" H 2100 1450 50  0001 C CNN
	1    2050 1500
	1    0    0    -1  
$EndComp
$Comp
L electrode_FPCB_rev0-rescue:electrode_PAD-jgshin_KiCad_lib CN6
U 1 1 60FE651A
P 2050 2250
F 0 "CN6" H 1731 2304 50  0000 R CNN
F 1 "electrode_PAD" H 1731 2395 50  0000 R CNN
F 2 "jgshin_KiCad_lib:electrode_PAD" H 2100 2200 50  0001 C CNN
F 3 "" H 2100 2200 50  0001 C CNN
	1    2050 2250
	1    0    0    -1  
$EndComp
Text Label 2500 900  0    50   ~ 0
Reference
Wire Wire Line
	2350 900  3000 900 
Wire Wire Line
	2350 1400 3000 1400
Wire Wire Line
	2350 1900 3000 1900
Text Label 2500 1400 0    50   ~ 0
CH1
Text Label 2500 1900 0    50   ~ 0
CH3
Text Label 2500 2150 0    50   ~ 0
CH4
$Comp
L electrode_FPCB_rev0-rescue:FFC0.5x10-jgshin_KiCad_lib CN7
U 1 1 60FEB38A
P 4050 2100
F 0 "CN7" H 4278 2726 50  0000 L CNN
F 1 "FFC0.5x10" H 4278 2635 50  0000 L CNN
F 2 "jgshin_KiCad_lib:FFC cable 0.5 x 10" H 4050 2100 50  0001 C CNN
F 3 "" H 4050 2100 50  0001 C CNN
	1    4050 2100
	1    0    0    -1  
$EndComp
Text Label 3450 1250 0    50   ~ 0
Reference
Wire Wire Line
	3300 1250 3950 1250
Text Label 3450 1350 0    50   ~ 0
Reference
Wire Wire Line
	3300 1350 3950 1350
Text Label 2500 1150 0    50   ~ 0
Ground
Wire Wire Line
	2350 1150 3000 1150
Text Label 3450 1750 0    50   ~ 0
Ground
Wire Wire Line
	3300 1750 3950 1750
Text Label 3450 1650 0    50   ~ 0
Ground
Wire Wire Line
	3300 1650 3950 1650
Text Label 3450 1550 0    50   ~ 0
Ground
Wire Wire Line
	3300 1550 3950 1550
Text Label 3450 1450 0    50   ~ 0
Reference
Wire Wire Line
	3300 1450 3950 1450
Wire Wire Line
	2350 2150 3000 2150
Text Label 2500 1650 0    50   ~ 0
CH2
Wire Wire Line
	2350 1650 3000 1650
$Comp
L electrode_FPCB_rev0-rescue:electrode_PAD-jgshin_KiCad_lib CN5
U 1 1 60FE631A
P 2050 2000
F 0 "CN5" H 1731 2054 50  0000 R CNN
F 1 "electrode_PAD" H 1731 2145 50  0000 R CNN
F 2 "jgshin_KiCad_lib:electrode_PAD" H 2100 1950 50  0001 C CNN
F 3 "" H 2100 1950 50  0001 C CNN
	1    2050 2000
	1    0    0    -1  
$EndComp
$Comp
L electrode_FPCB_rev0-rescue:electrode_PAD-jgshin_KiCad_lib CN4
U 1 1 60FE60B4
P 2050 1750
F 0 "CN4" H 1731 1804 50  0000 R CNN
F 1 "electrode_PAD" H 1731 1895 50  0000 R CNN
F 2 "jgshin_KiCad_lib:electrode_PAD" H 2100 1700 50  0001 C CNN
F 3 "" H 2100 1700 50  0001 C CNN
	1    2050 1750
	1    0    0    -1  
$EndComp
Wire Wire Line
	3300 1150 3950 1150
Text Label 3450 1150 0    50   ~ 0
CH1
Wire Wire Line
	3300 1050 3950 1050
Text Label 3450 1050 0    50   ~ 0
CH3
Text Label 3450 1950 0    50   ~ 0
CH4
Wire Wire Line
	3300 1950 3950 1950
Wire Wire Line
	3300 1850 3950 1850
Text Label 3450 1850 0    50   ~ 0
CH2
$EndSCHEMATC
