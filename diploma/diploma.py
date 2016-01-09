#!/usr/bin/env python
import matplotlib.pyplot as plt
import FileDialog
import Tkinter
import numpy


def diploma():
    print 'SiHx + 2 H2O = SiO2+ (2+x/2) H2'
    mb = False
    xb = False
    while mb != True:
        mass = int(raw_input('Enter SiHx mass in gramms: '))
        if mass > 0:
            mb = True
    while xb != True:
        x = int(raw_input('Enter x in range [0,3]: '))
        if x in range(4):
            xb = True

    result0 = (2 * 22.4 * mass) / (28)
    result1 = (2.5 * 22.4 * mass) / (29)
    result2 = (3 * 22.4 * mass) / (30)
    result3 = (3.5 * 22.4 * mass) / (31)
    print ''
    print ''
    if x == 0:
        print ''
        print "Si + 2H2O = SiO2 + 2H2 "
        print result0, "gramms of Hydrogen was allocated"

    elif x == 1:
        print ''
        print "2SiH + 4H2O = 2SiO2 + 5H2 "
        print result1, "gramms of Hydrogen was allocated"

    elif x == 2:
        print ''
        print "SiH2 + 2 H2O = SiO2 + 3H2"
        print result2, "gramms of Hydrogen was allocated"
    elif x == 3:
        print ''
        print "2SiH3 + 4H2O = 2SiO2 + 7H2"
        print result3, "gramms of Hydrogen was allocated"
    plt.plot([result0, result1, result2, result3], [0, 1, 2, 3], 'ro-')
    plt.axis([0, result3 + 200, 0, 4])
    plt.ylabel('X')
    plt.xlabel('AMOUNT')
    plt.show()


diploma()
