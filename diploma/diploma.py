import matplotlib.pyplot as plt
import numpy as np


def diploma():
    print 'SiHx + 2 H2O = SiO2+ (2+x/2) H2'
    mass = int(raw_input('Enter SiHx mass in gramms: '))
    x = int(raw_input('Enter x: '))

    result0 = (3 * 22.4 * mass) / 30
    result1 = (3 * 22.4 * mass) / 30
    result2 = (3 * 22.4 * mass) / 30
    result3 = (3 * 22.4 * mass) / 30
    if x == 0:
        print result0, "gramms of Hydrogen was allocated"

    elif x == 1:
        print result1, "gramms of Hydrogen was allocated"

    elif x == 2:
        print result2, "gramms of Hydrogen was allocated"

    elif x == 3:
        print result3, "gramms of Hydrogen was allocated"
    print result0, result1, result2, result3


diploma()
