#!/usr/bin/env python
from fractions import Fraction
import matplotlib.pyplot as plt
import wx
import FileDialog
import Tkinter
import numpy




def isfraction(input):
    try:
        return Fraction(input) != None;
    except ValueError:
        return False;
def isfloat(input):
    try:
        return float(input) != None;
    except ValueError:
        return False;

def diploma():

    print 'SiHx + 2 H2O = SiO2+ (2+x/2) H2'
    mass_boolean = False
    x_boolean = False

    while mass_boolean != True:
        mass = raw_input('Enter SiHx mass in gramms: ')
        if isfraction(mass) == True:
            mass = Fraction(mass)
            if mass > 0:
                mass_boolean = True
            else:
                mass_boolean = False
        elif isfloat(mass) == True:
            mass_boolean = True
        else:
            print 'Please, enter valid value'
            mass_boolean=False
    while x_boolean != True:
        x = raw_input('Enter x in range [0,3]: ')
        if x.isdigit() and int(x) in range(4):
            x_boolean = True

    result0 = (2 * 22.4 * float(mass)) / (28)
    result1 = (2.5 * 22.4 * float(mass)) / (29)
    result2 = (3 * 22.4 * float(mass)) / (30)
    result3 = (3.5 * 22.4 * float(mass)) / (31)
    print ''
    print ''
    if int(x) == 0:
        print ''
        print "Si + 2H2O = SiO2 + 2H2 "
        print result0, "gramms of Hydrogen was allocated"

    elif int(x) == 1:
        print ''
        print "2SiH + 4H2O = 2SiO2 + 5H2 "
        print result1, "gramms of Hydrogen was allocated"

    elif int(x) == 2:
        print ''
        print "SiH2 + 2 H2O = SiO2 + 3H2"
        print result2, "gramms of Hydrogen was allocated"
    elif int(x) == 3:
        print ''
        print "2SiH3 + 4H2O = 2SiO2 + 7H2"
        print result3, "gramms of Hydrogen was allocated"
#    plt.ion()
    plt.plot([result0, result1, result2, result3], [0, 1, 2, 3], 'ro-')
    plt.axis([0, result3 + 200, 0, 4])
    plt.ylabel('X')
    plt.xlabel('AMOUNT')
    plt.autoscale(enable=True,axis='both',tight=None)
    plt.show()
#    close = True
#    while close is True:
#        print 'Close current plot?'
#        choise= raw_input('y/n?')
#        if choise == 'y':
#            print 'OK, closing plot. . .'
#            plt.clf()
#            close = False
#        elif choise == 'n':
#            print 'OK, current plot will remain.'
#        else:
#            print 'Your decision must be either \"y\" or \"n\".'



diploma()

def repeat():
    repeating = True
    while repeating is True:
        print 'Repeat calculations with different values?'
        decision = raw_input('y/n?')
        if decision == 'n':
            print 'OK, terminating . . .'
            repeating = False
        elif decision == 'y':
            diploma()
        else:
            print 'Your decision must be either \"y\" or \"n\".'
repeat()
