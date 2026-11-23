EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Simulatore di cella di carico a ponte 348 ohm"
Date "2026-10-11"
Rev "P3"
Comp ""
Comment1 "Resistenze a foro"
Comment2 "Dispensa: dispensa_simulatore_ponte_348.html"
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Simulatore:R R3
U 1 1 A7CAC1A3
P 2500 2150
F 0 "R3" H 2570 2100 50  0000 L CNN
F 1 "348R 0,1%" H 2570 2200 50  0000 L CNN
F 2 "Simulatore:R_Axial_DIN0207_P10.16mm_Rot90" H 2500 2150 50  0001 C CNN
F 3 "~" H 2500 2150 50  0001 C CNN
	1    2500 2150
	1    0    0    -1  
$EndComp
$Comp
L Simulatore:R R4
U 1 1 BA411322
P 2500 5850
F 0 "R4" H 2570 5800 50  0000 L CNN
F 1 "348R 0,1%" H 2570 5900 50  0000 L CNN
F 2 "Simulatore:R_Axial_DIN0207_P10.16mm_Rot90" H 2500 5850 50  0001 C CNN
F 3 "~" H 2500 5850 50  0001 C CNN
	1    2500 5850
	1    0    0    -1  
$EndComp
$Comp
L Simulatore:R R1
U 1 1 E9E42599
P 3000 2150
F 0 "R1" H 3070 2100 50  0000 L CNN
F 1 "348R 0,1%" H 3070 2200 50  0000 L CNN
F 2 "Simulatore:R_Axial_DIN0207_P10.16mm_Rot90" H 3000 2150 50  0001 C CNN
F 3 "~" H 3000 2150 50  0001 C CNN
	1    3000 2150
	1    0    0    -1  
$EndComp
$Comp
L Simulatore:R R2
U 1 1 0059792B
P 3000 5850
F 0 "R2" H 3070 5800 50  0000 L CNN
F 1 "348R 0,1%" H 3070 5900 50  0000 L CNN
F 2 "Simulatore:R_Axial_DIN0207_P10.16mm_Rot90" H 3000 5850 50  0001 C CNN
F 3 "~" H 3000 5850 50  0001 C CNN
	1    3000 5850
	1    0    0    -1  
$EndComp
$Comp
L Simulatore:R R7
U 1 1 D999736D
P 5300 2150
F 0 "R7" H 5370 2100 50  0000 L CNN
F 1 "909R 1%" H 5370 2200 50  0000 L CNN
F 2 "Simulatore:R_Axial_DIN0207_P10.16mm_Rot90" H 5300 2150 50  0001 C CNN
F 3 "~" H 5300 2150 50  0001 C CNN
	1    5300 2150
	1    0    0    -1  
$EndComp
$Comp
L Simulatore:R R8
U 1 1 6E92184B
P 5300 5850
F 0 "R8" H 5370 5800 50  0000 L CNN
F 1 "909R 1%" H 5370 5900 50  0000 L CNN
F 2 "Simulatore:R_Axial_DIN0207_P10.16mm_Rot90" H 5300 5850 50  0001 C CNN
F 3 "~" H 5300 5850 50  0001 C CNN
	1    5300 5850
	1    0    0    -1  
$EndComp
$Comp
L Simulatore:R_H R5
U 1 1 1264078E
P 4100 4000
F 0 "R5" H 4170 3950 50  0000 L CNN
F 1 "3k65 0,1%" H 4170 4050 50  0000 L CNN
F 2 "Simulatore:R_Axial_DIN0207_P10.16mm_Horizontal" H 4100 4000 50  0001 C CNN
F 3 "~" H 4100 4000 50  0001 C CNN
	1    4100 4000
	1    0    0    -1  
$EndComp
$Comp
L Simulatore:R_H R6
U 1 1 509E8960
P 4100 4800
F 0 "R6" H 4170 4750 50  0000 L CNN
F 1 "71k5 1%" H 4170 4850 50  0000 L CNN
F 2 "Simulatore:R_Axial_DIN0207_P10.16mm_Horizontal" H 4100 4800 50  0001 C CNN
F 3 "~" H 4100 4800 50  0001 C CNN
	1    4100 4800
	1    0    0    -1  
$EndComp
$Comp
L Simulatore:POT_WL RV1
U 1 1 91E6CCCB
P 5300 4000
F 0 "RV1" H 5370 3950 50  0000 L CNN
F 1 "200R 10 giri SPAN" H 5370 4050 50  0000 L CNN
F 2 "Simulatore:PinHeader_1x03_P2.54mm_Vertical" H 5300 4000 50  0001 C CNN
F 3 "~" H 5300 4000 50  0001 C CNN
	1    5300 4000
	1    0    0    -1  
$EndComp
$Comp
L Simulatore:POT_WL RV2
U 1 1 2D15FAAB
P 6500 4800
F 0 "RV2" H 6570 4750 50  0000 L CNN
F 1 "10k 25 giri ZERO" H 6570 4850 50  0000 L CNN
F 2 "Simulatore:PinHeader_1x03_P2.54mm_Vertical" H 6500 4800 50  0001 C CNN
F 3 "~" H 6500 4800 50  0001 C CNN
	1    6500 4800
	1    0    0    -1  
$EndComp
$Comp
L Simulatore:R_H R9
U 1 1 EE1DBE2C
P 1500 2000
F 0 "R9" H 1570 1950 50  0000 L CNN
F 1 "ponte 0R (cavo)" H 1570 2050 50  0000 L CNN
F 2 "Simulatore:R_Axial_DIN0207_P5.08mm_Horizontal" H 1500 2000 50  0001 C CNN
F 3 "~" H 1500 2000 50  0001 C CNN
	1    1500 2000
	1    0    0    -1  
$EndComp
$Comp
L Simulatore:R_H R10
U 1 1 D9DF038F
P 1500 6000
F 0 "R10" H 1570 5950 50  0000 L CNN
F 1 "ponte 0R (cavo)" H 1570 6050 50  0000 L CNN
F 2 "Simulatore:R_Axial_DIN0207_P5.08mm_Horizontal" H 1500 6000 50  0001 C CNN
F 3 "~" H 1500 6000 50  0001 C CNN
	1    1500 6000
	1    0    0    -1  
$EndComp
$Comp
L Simulatore:CONN_01X06 J1
U 1 1 3BD08F79
P 1200 4000
F 0 "J1" H 1270 3950 50  0000 L CNN
F 1 "Conn_01x06" H 1270 4050 50  0000 L CNN
F 2 "Simulatore:PinHeader_1x06_P2.54mm_Vertical" H 1200 4000 50  0001 C CNN
F 3 "~" H 1200 4000 50  0001 C CNN
	1    1200 4000
	1    0    0    -1  
$EndComp
$Comp
L Simulatore:MOUNTINGHOLE H1
U 1 1 233CF70B
P 800 6900
F 0 "H1" H 870 6850 50  0000 L CNN
F 1 "M2.5" H 870 6950 50  0000 L CNN
F 2 "Simulatore:MountingHole_2.7mm_M2.5" H 800 6900 50  0001 C CNN
F 3 "~" H 800 6900 50  0001 C CNN
	1    800 6900
	1    0    0    -1  
$EndComp
$Comp
L Simulatore:MOUNTINGHOLE H2
U 1 1 C495934A
P 1800 6900
F 0 "H2" H 1870 6850 50  0000 L CNN
F 1 "M2.5" H 1870 6950 50  0000 L CNN
F 2 "Simulatore:MountingHole_2.7mm_M2.5" H 1800 6900 50  0001 C CNN
F 3 "~" H 1800 6900 50  0001 C CNN
	1    1800 6900
	1    0    0    -1  
$EndComp
Wire Wire Line
	1800 2000 2500 2000
Wire Wire Line
	2500 2000 3000 2000
Wire Wire Line
	3000 2000 5300 2000
Wire Wire Line
	5300 2000 6500 2000
Wire Wire Line
	1800 6000 2500 6000
Wire Wire Line
	2500 6000 3000 6000
Wire Wire Line
	3000 6000 5300 6000
Wire Wire Line
	5300 6000 6500 6000
Wire Wire Line
	1650 2000 1800 2000
Wire Wire Line
	1650 6000 1800 6000
Wire Wire Line
	2500 2300 2500 5700
Wire Wire Line
	3000 2300 3000 4000
Wire Wire Line
	3000 4000 3000 4800
Wire Wire Line
	3000 4800 3000 5700
Wire Wire Line
	3950 4000 3000 4000
Wire Wire Line
	3950 4800 3000 4800
Wire Wire Line
	5300 2300 5300 3850
Wire Wire Line
	5300 5700 5300 4150
Wire Wire Line
	4250 4000 5150 4000
Wire Wire Line
	4250 4800 6350 4800
Wire Wire Line
	6500 4650 6500 2000
Wire Wire Line
	6500 4950 6500 6000
Wire Wire Line
	700 3800 1000 3800
Wire Wire Line
	700 3900 1000 3900
Wire Wire Line
	700 4000 1000 4000
Wire Wire Line
	700 4100 1000 4100
Wire Wire Line
	700 4200 1000 4200
Wire Wire Line
	700 4300 1000 4300
Wire Wire Line
	1350 2000 1050 2000
Wire Wire Line
	1350 6000 1050 6000
Connection ~ 2500 2000
Connection ~ 3000 2000
Connection ~ 5300 2000
Connection ~ 2500 6000
Connection ~ 3000 6000
Connection ~ 5300 6000
Connection ~ 3000 4000
Connection ~ 3000 4800
Text GLabel 2150 2000 0 50   Passive ~ 0
E+
Text GLabel 2150 6000 0 50   Passive ~ 0
E-
Text GLabel 2500 3500 0 50   Passive ~ 0
A-
Text GLabel 3000 3500 0 50   Passive ~ 0
A+
Text GLabel 5300 3100 0 50   Passive ~ 0
N1
Text GLabel 5300 5300 0 50   Passive ~ 0
N2
Text GLabel 4600 4000 0 50   Passive ~ 0
W1
Text GLabel 4600 4800 0 50   Passive ~ 0
W2
Text GLabel 700 3800 2 50   Passive ~ 0
EXC+
Text GLabel 700 3900 2 50   Passive ~ 0
E+
Text GLabel 700 4000 2 50   Passive ~ 0
A+
Text GLabel 700 4100 2 50   Passive ~ 0
A-
Text GLabel 700 4200 2 50   Passive ~ 0
E-
Text GLabel 700 4300 2 50   Passive ~ 0
EXC-
Text GLabel 1050 2000 2 50   Passive ~ 0
EXC+
Text GLabel 1050 6000 2 50   Passive ~ 0
EXC-
$EndSCHEMATC
