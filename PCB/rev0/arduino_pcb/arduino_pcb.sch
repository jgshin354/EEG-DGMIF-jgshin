EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:Jack-DC J?
U 1 1 5F23E5E7
P 2250 4800
F 0 "J?" H 2307 5125 50  0000 C CNN
F 1 "Jack-DC" H 2307 5034 50  0000 C CNN
F 2 "" H 2300 4760 50  0001 C CNN
F 3 "~" H 2300 4760 50  0001 C CNN
	1    2250 4800
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5F2401AA
P 2550 4900
F 0 "#PWR?" H 2550 4650 50  0001 C CNN
F 1 "GND" H 2555 4727 50  0000 C CNN
F 2 "" H 2550 4900 50  0001 C CNN
F 3 "" H 2550 4900 50  0001 C CNN
	1    2550 4900
	1    0    0    -1  
$EndComp
$Comp
L power:+12V #PWR?
U 1 1 5F241F1D
P 2550 4700
F 0 "#PWR?" H 2550 4550 50  0001 C CNN
F 1 "+12V" H 2565 4873 50  0000 C CNN
F 2 "" H 2550 4700 50  0001 C CNN
F 3 "" H 2550 4700 50  0001 C CNN
	1    2550 4700
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 5F242E7B
P 5400 1750
F 0 "#PWR?" H 5400 1600 50  0001 C CNN
F 1 "+5V" H 5415 1923 50  0000 C CNN
F 2 "" H 5400 1750 50  0001 C CNN
F 3 "" H 5400 1750 50  0001 C CNN
	1    5400 1750
	1    0    0    -1  
$EndComp
$Comp
L power:+12V #PWR?
U 1 1 5F2416B9
P 4950 1750
F 0 "#PWR?" H 4950 1600 50  0001 C CNN
F 1 "+12V" H 4965 1923 50  0000 C CNN
F 2 "" H 4950 1750 50  0001 C CNN
F 3 "" H 4950 1750 50  0001 C CNN
	1    4950 1750
	1    0    0    -1  
$EndComp
NoConn ~ 5550 2250
NoConn ~ 5550 2150
Wire Wire Line
	5250 1750 5400 1750
NoConn ~ 5550 3450
NoConn ~ 5550 3350
NoConn ~ 5550 3250
NoConn ~ 5550 3150
NoConn ~ 5550 3050
NoConn ~ 5550 2950
NoConn ~ 5550 2850
NoConn ~ 5550 2750
NoConn ~ 5550 2550
$Comp
L power:+3.3V #PWR?
U 1 1 5F2426A7
P 5150 1750
F 0 "#PWR?" H 5150 1600 50  0001 C CNN
F 1 "+3.3V" H 5165 1923 50  0000 C CNN
F 2 "" H 5150 1750 50  0001 C CNN
F 3 "" H 5150 1750 50  0001 C CNN
	1    5150 1750
	1    0    0    -1  
$EndComp
$Comp
L MCU_Module:Arduino_Nano_v3.x A?
U 1 1 5F23CF65
P 5050 2750
F 0 "A?" H 5050 1661 50  0000 C CNN
F 1 "Arduino_Nano_v3.x" H 5050 1570 50  0000 C CNN
F 2 "Module:Arduino_Nano" H 5050 2750 50  0001 C CIN
F 3 "http://www.mouser.com/pdfdocs/Gravitech_Arduino_Nano3_0.pdf" H 5050 2750 50  0001 C CNN
	1    5050 2750
	1    0    0    -1  
$EndComp
Wire Wire Line
	4550 3450 4200 3450
Wire Wire Line
	4550 3350 4200 3350
Wire Wire Line
	4550 3250 4200 3250
Wire Wire Line
	4550 3150 4200 3150
Wire Wire Line
	4550 3050 4200 3050
Wire Wire Line
	4550 2950 4200 2950
Wire Wire Line
	4550 2850 4200 2850
Wire Wire Line
	4550 2750 4200 2750
Wire Wire Line
	4550 2650 4200 2650
Wire Wire Line
	4550 2550 4200 2550
Wire Wire Line
	4550 2450 4200 2450
Wire Wire Line
	4550 2350 4200 2350
Wire Wire Line
	4550 2250 4200 2250
Wire Wire Line
	4550 2150 4200 2150
Text Label 4200 3250 0    50   ~ 0
TDTPIN2
Text Label 4200 3150 0    50   ~ 0
TDTPIN1
Text Label 4200 3050 0    50   ~ 0
TDTPIN0
Text Label 4200 2850 0    50   ~ 0
STATE
Text Label 4200 2450 0    50   ~ 0
BLUEPIN
Text Label 4200 3350 0    50   ~ 0
OPERATE
Text Label 4200 2750 0    50   ~ 0
GREENPIN
Text Label 4200 2650 0    50   ~ 0
REDPIN
NoConn ~ 4200 2150
NoConn ~ 4200 2250
NoConn ~ 4200 2350
NoConn ~ 4200 2550
NoConn ~ 4200 2950
NoConn ~ 4200 3450
$Comp
L Connector:Conn_Coaxial J?
U 1 1 5F248850
P 3600 4700
F 0 "J?" H 3700 4675 50  0000 L CNN
F 1 "Conn_Coaxial" H 3700 4584 50  0000 L CNN
F 2 "" H 3600 4700 50  0001 C CNN
F 3 " ~" H 3600 4700 50  0001 C CNN
	1    3600 4700
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_Coaxial J?
U 1 1 5F249569
P 4800 4700
F 0 "J?" H 4900 4675 50  0000 L CNN
F 1 "Conn_Coaxial" H 4900 4584 50  0000 L CNN
F 2 "" H 4800 4700 50  0001 C CNN
F 3 " ~" H 4800 4700 50  0001 C CNN
	1    4800 4700
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_Coaxial J?
U 1 1 5F24A38C
P 6050 4700
F 0 "J?" H 6150 4675 50  0000 L CNN
F 1 "Conn_Coaxial" H 6150 4584 50  0000 L CNN
F 2 "" H 6050 4700 50  0001 C CNN
F 3 " ~" H 6050 4700 50  0001 C CNN
	1    6050 4700
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5F24B010
P 3600 4900
F 0 "#PWR?" H 3600 4650 50  0001 C CNN
F 1 "GND" H 3605 4727 50  0000 C CNN
F 2 "" H 3600 4900 50  0001 C CNN
F 3 "" H 3600 4900 50  0001 C CNN
	1    3600 4900
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5F24B557
P 4800 4900
F 0 "#PWR?" H 4800 4650 50  0001 C CNN
F 1 "GND" H 4805 4727 50  0000 C CNN
F 2 "" H 4800 4900 50  0001 C CNN
F 3 "" H 4800 4900 50  0001 C CNN
	1    4800 4900
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5F24BBCB
P 6050 4900
F 0 "#PWR?" H 6050 4650 50  0001 C CNN
F 1 "GND" H 6055 4727 50  0000 C CNN
F 2 "" H 6050 4900 50  0001 C CNN
F 3 "" H 6050 4900 50  0001 C CNN
	1    6050 4900
	1    0    0    -1  
$EndComp
Wire Wire Line
	4600 4700 4250 4700
Wire Wire Line
	3400 4700 3050 4700
Text Label 4250 4700 0    50   ~ 0
TDTPIN1
Text Label 3050 4700 0    50   ~ 0
TDTPIN0
Wire Wire Line
	5850 4700 5500 4700
Text Label 5500 4700 0    50   ~ 0
TDTPIN2
$Comp
L dk_Transistors-FETs-MOSFETs-Single:IRF510PBF Q?
U 1 1 5F2645FB
P 7550 3050
F 0 "Q?" H 7658 3103 60  0000 L CNN
F 1 "IRF510PBF" H 7658 2997 60  0000 L CNN
F 2 "digikey-footprints:TO-220-3" H 7750 3250 60  0001 L CNN
F 3 "http://www.vishay.com/docs/91015/sihf510.pdf" H 7750 3350 60  0001 L CNN
F 4 "IRF510PBF-ND" H 7750 3450 60  0001 L CNN "Digi-Key_PN"
F 5 "IRF510PBF" H 7750 3550 60  0001 L CNN "MPN"
F 6 "Discrete Semiconductor Products" H 7750 3650 60  0001 L CNN "Category"
F 7 "Transistors - FETs, MOSFETs - Single" H 7750 3750 60  0001 L CNN "Family"
F 8 "http://www.vishay.com/docs/91015/sihf510.pdf" H 7750 3850 60  0001 L CNN "DK_Datasheet_Link"
F 9 "/product-detail/en/vishay-siliconix/IRF510PBF/IRF510PBF-ND/811710" H 7750 3950 60  0001 L CNN "DK_Detail_Page"
F 10 "MOSFET N-CH 100V 5.6A TO-220AB" H 7750 4050 60  0001 L CNN "Description"
F 11 "Vishay Siliconix" H 7750 4150 60  0001 L CNN "Manufacturer"
F 12 "Active" H 7750 4250 60  0001 L CNN "Status"
	1    7550 3050
	1    0    0    -1  
$EndComp
$Comp
L dk_Transistors-FETs-MOSFETs-Single:IRF510PBF Q?
U 1 1 5F268D13
P 7550 3900
F 0 "Q?" H 7658 3953 60  0000 L CNN
F 1 "IRF510PBF" H 7658 3847 60  0000 L CNN
F 2 "digikey-footprints:TO-220-3" H 7750 4100 60  0001 L CNN
F 3 "http://www.vishay.com/docs/91015/sihf510.pdf" H 7750 4200 60  0001 L CNN
F 4 "IRF510PBF-ND" H 7750 4300 60  0001 L CNN "Digi-Key_PN"
F 5 "IRF510PBF" H 7750 4400 60  0001 L CNN "MPN"
F 6 "Discrete Semiconductor Products" H 7750 4500 60  0001 L CNN "Category"
F 7 "Transistors - FETs, MOSFETs - Single" H 7750 4600 60  0001 L CNN "Family"
F 8 "http://www.vishay.com/docs/91015/sihf510.pdf" H 7750 4700 60  0001 L CNN "DK_Datasheet_Link"
F 9 "/product-detail/en/vishay-siliconix/IRF510PBF/IRF510PBF-ND/811710" H 7750 4800 60  0001 L CNN "DK_Detail_Page"
F 10 "MOSFET N-CH 100V 5.6A TO-220AB" H 7750 4900 60  0001 L CNN "Description"
F 11 "Vishay Siliconix" H 7750 5000 60  0001 L CNN "Manufacturer"
F 12 "Active" H 7750 5100 60  0001 L CNN "Status"
	1    7550 3900
	1    0    0    -1  
$EndComp
$Comp
L dk_Transistors-FETs-MOSFETs-Single:IRF510PBF Q?
U 1 1 5F26A450
P 7550 4650
F 0 "Q?" H 7658 4703 60  0000 L CNN
F 1 "IRF510PBF" H 7658 4597 60  0000 L CNN
F 2 "digikey-footprints:TO-220-3" H 7750 4850 60  0001 L CNN
F 3 "http://www.vishay.com/docs/91015/sihf510.pdf" H 7750 4950 60  0001 L CNN
F 4 "IRF510PBF-ND" H 7750 5050 60  0001 L CNN "Digi-Key_PN"
F 5 "IRF510PBF" H 7750 5150 60  0001 L CNN "MPN"
F 6 "Discrete Semiconductor Products" H 7750 5250 60  0001 L CNN "Category"
F 7 "Transistors - FETs, MOSFETs - Single" H 7750 5350 60  0001 L CNN "Family"
F 8 "http://www.vishay.com/docs/91015/sihf510.pdf" H 7750 5450 60  0001 L CNN "DK_Datasheet_Link"
F 9 "/product-detail/en/vishay-siliconix/IRF510PBF/IRF510PBF-ND/811710" H 7750 5550 60  0001 L CNN "DK_Detail_Page"
F 10 "MOSFET N-CH 100V 5.6A TO-220AB" H 7750 5650 60  0001 L CNN "Description"
F 11 "Vishay Siliconix" H 7750 5750 60  0001 L CNN "Manufacturer"
F 12 "Active" H 7750 5850 60  0001 L CNN "Status"
	1    7550 4650
	1    0    0    -1  
$EndComp
Wire Wire Line
	7250 4000 6900 4000
Wire Wire Line
	7250 3150 6900 3150
Text Label 6900 4000 0    50   ~ 0
GREENPIN
Text Label 6900 3150 0    50   ~ 0
REDPIN
Wire Wire Line
	7250 4750 6900 4750
Text Label 6900 4750 0    50   ~ 0
BLUEPIN
$Comp
L power:GND #PWR?
U 1 1 5F273183
P 7550 3250
F 0 "#PWR?" H 7550 3000 50  0001 C CNN
F 1 "GND" H 7555 3077 50  0000 C CNN
F 2 "" H 7550 3250 50  0001 C CNN
F 3 "" H 7550 3250 50  0001 C CNN
	1    7550 3250
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5F27390C
P 7550 4050
F 0 "#PWR?" H 7550 3800 50  0001 C CNN
F 1 "GND" H 7555 3877 50  0000 C CNN
F 2 "" H 7550 4050 50  0001 C CNN
F 3 "" H 7550 4050 50  0001 C CNN
	1    7550 4050
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5F273ECB
P 7550 4850
F 0 "#PWR?" H 7550 4600 50  0001 C CNN
F 1 "GND" H 7555 4677 50  0000 C CNN
F 2 "" H 7550 4850 50  0001 C CNN
F 3 "" H 7550 4850 50  0001 C CNN
	1    7550 4850
	1    0    0    -1  
$EndComp
Wire Wire Line
	7550 2850 7550 2700
Wire Wire Line
	7550 2700 7900 2700
Wire Wire Line
	7550 3700 7550 3550
Wire Wire Line
	7550 3550 7900 3550
Wire Wire Line
	7550 4450 7550 4300
Wire Wire Line
	7550 4300 7900 4300
Text Label 7900 2700 0    50   ~ 0
REDLED
Text Label 7900 3550 0    50   ~ 0
GREENLED
Text Label 7900 4300 0    50   ~ 0
BLUELED
$EndSCHEMATC
