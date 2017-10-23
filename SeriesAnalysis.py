#!/user/bin/python
# Joeliphant
# Series Circuit w/3 Values

import math
from math import pi

def RectangularToPolar(x,y):
    angle = (math.atan(y/x))
    angle = angle = 180 * (180/pi)
    magnitude = (math.sqrt((x*x)+(y*y)))
    answer = magnitude, angle

def PolarToRectangular(PolarNumber):
    y = PolarNumber[0] * (math.sin(PolarNumber[1] * pi/180))
    x = PolarNumber[0] * (math.cos(PolarNumber[1] * pi/180))
    rectangular = x, y
    return rectangular

def Magnitude(number):
    absolute = math.sqrt((number[0] * number[0]) + (number[1] * number[1]))
    return absolute

print("This is for calculating a series AC circuit with one Ris. Cap. and Ind.")
Voltage = input("What is the voltage of the source? (in RMS): ")
Frequency = input("What is the frequency of the source? (in Hz): ")
ResistorValue = input("What is the value of the resistor? (in Ohms): ")
CapacitorValue = input("What is the value of the capacitor? (in Farads): ")
InductorValue = input("What is the value of the inductor? (in Henrys): ")
InductorResistance = input("What is the resistance of the wiring of the inductor? (in Ohms): ")

BaseLC = 2 * pi * Frequency
TotalResistance = InductorResistance + ResistorValue
Inductance = BaseLC * InductorValue
MagnitudeInductance = (InductorResistance, Inductance)
MagnitudeInductance = Magnitude(MagnitudeInductance)
Capacitance = (1/(BaseLC * CapacitorValue))
Impedance = TotalResistance, (Inductance + -Capacitance)
MagnitudeImpedance = Magnitude(Impedance)
Current = float(Voltage) / float(MagnitudeImpedance)
VoltageResistor = Current * ResistorValue
VoltageInductor = Current * Inductance
VoltageCapacitor = Current * Capacitance

if Inductance > Capacitance:
    ArgumentSend = Impedance[0] / Impedance[1]
else:
    if Capacitance > Inductance:
        ArgumentSend = Impedance[0] / Impedance[1]
    else:
        ArgumentSend = 0
PhaseRadians = math.atan(ArgumentSend)
PhaseAngle = PhaseRadians * (180/pi)

if Inductance > Capacitance:
    print("The current will lag the voltage by the percentage of %f degrees" % PhaseAngle)
if Capacitance > Inductance:
    print("The current will lead the voltage by the percentage of %f degrees" % PhaseAngle)
print ("The total impedance is: %.2f + %.2fj" % (Impedance[0], Impedance[1]))
print ("The magnitude of the impedance is: %.2f" % MagnitudeImpedance)
print ("The current is: %f A" % Current)
print ("V(R) = %.2f, V(L) = %.2f, V(C) = %.2f" % (VoltageResistor, VoltageInductor, VoltageCapacitor))
