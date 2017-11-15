#!/user/bin/python
# Joeliphant
# Parallel Circuit w/3 Values

import math
from math import pi
import CalculatedBeginnings as cplx

def RectangularToPolar(RectangularNumber):
    angle1 = (math.atan(RectangularNumber[1]/RectangularNumber[0]))
    angle2 = (angle1 * (180/pi))
    magnitude = (math.sqrt((RectangularNumber[0]*RectangularNumber[0])+(RectangularNumber[1]*RectangularNumber[1])))
    answer = (magnitude, angle2)
    return answer

def PolarToRectangular(PolarNumber):
    y = PolarNumber[0] * (math.sin(PolarNumber[1] * pi/180))
    x = PolarNumber[0] * (math.cos(PolarNumber[1] * pi/180))
    rectangular = (x, y)
    return rectangular

def Magnitude(number):
    absolute = math.sqrt((number[0] * number[0]) + (number[1] * number[1]))
    return absolute

print("This is for calculating a parallel AC circuit with one Ris. Cap. nd Ind.")
Voltage = input("What is the voltage of the source? (in RMS): ")
Frequency = input("What is the frequency of the source? (in Hz): ")
ResistorValue = input("What is the value of the resistor? (in Ohms): ")
CapacitorValue = input("What is the value of the capacitor? (in Farads): ")
InductorValue = input("What is the value of the inductor? (in Henrys): ")
InductorResistance = input("What is the resistance of the wiring of the inductor? (in Ohms): ")

BaseLC = 2 * pi * Frequency
one = (1,0)
Voltage = (float(Voltage), 0)
Resistance = (float(ResistorValue), 0)
InductorResistance = ((InductorResistance), 0) 
Inductance = ((BaseLC * float(InductorValue), 90))
InductorLine = cplx.complexAdding(PolarToRectangular(Inductance), PolarToRectangular(InductorResistance))
print("InductorLine = %f, %f" % (InductorLine[0], InductorLine[1]))
CapacitorBottom = (float(BaseLC) * float(CapacitorValue))
Capacitance = (((1) / (float(CapacitorBottom))), -90)
print ("Capacitance = %f, %f" % (Capacitance[0], Capacitance[1]))
InverseResistance = cplx.complexDividing(one, Resistance)
InverseInductance = cplx.complexDividing(one, RectangularToPolar(InductorLine))
InverseCapacitance = cplx.complexDividing(one, Capacitance)
ImpedanceDenomenator = cplx.complexAdding(PolarToRectangular(InverseCapacitance), PolarToRectangular(InverseInductance))
ImpedanceDenomenators = cplx.complexAdding(ImpedanceDenomenator, PolarToRectangular(InverseResistance))
TotalImpedance = cplx.complexDividing(one, RectangularToPolar(ImpedanceDenomenators))
TotalCurrent = cplx.complexDividing(Voltage, TotalImpedance)
Phase = TotalCurrent[1]

if Inductance > Capacitance:
    print("The current will lag the voltage by the percentage of %f degrees" % Phase)
if Capacitance > Inductance:
    print("The current will lead the voltage by the percentage of %f degrees" % Phase)
if Capacitance == InductorLine:
    print("Your current and voltage will be in phase")
print ("The total impedance is: %.2f + %.2fj" % (TotalImpedance[0], TotalImpedance[1]))
print ("Since this is a parallel circuit each component drops the source voltage.")
print ("The total current of the circuit is %f Amps" % TotalCurrent[0])
