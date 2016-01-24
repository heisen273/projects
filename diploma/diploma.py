#!/usr/bin/env python
from __future__ import division
from fractions import Fraction
import matplotlib.pyplot as plt
import FileDialog
from Tkinter import *
import numpy


class app():
    def __init__(self):
        self.window = Tk()
        self.window.title('app')
        self.mass_string = StringVar()
        mass = Entry(self.window, textvariable=self.mass_string)
        mass.grid(row=0, column=1, columnspan=2)

        mass_labeltext = StringVar()
        mass_labeltext.set('Enter SiHx mass in gramms:')
        mass_label = Label(self.window, textvariable=mass_labeltext, height=1)
        mass_label.grid(row=0, column=0)

        self.x_string = StringVar()
        x = Entry(self.window, textvariable=self.x_string)
        x.grid(row=1, column=1, columnspan=10)

        x_labeltext = StringVar()
        x_labeltext.set('Enter x in range [0,3]:')
        x_label = Label(self.window, textvariable=x_labeltext, height=1)
        x_label.grid(row=1, column=0)

        self.output = Text(self.window, height=10, width=60, highlightbackground='black')
        self.output.grid(row=4, column=0)

        output_labeltext = StringVar()
        output_labeltext.set('Program Output')
        output_label = Label(self.window, textvariable=output_labeltext, height=1)
        output_label.grid(row=3, column=0)
        values = ['quit', 'plot', 'clear', 'close', 'reset output']

        for txt in values:
            padx = 6
            pady = 5

            if txt == 'clear':
                btn = Button(self.window, height=2, width=4, padx=padx, pady=pady, text=txt,
                             command=lambda: self.clear())
                btn.grid(row=3, column=2, padx=1, pady=1)
            elif txt == 'close':
                btn = Button(self.window, height=2, width=5, padx=padx, pady=pady, text=txt,
                             command=lambda: self.close())
                btn.grid(row=2, column=2, padx=1, pady=1)
            elif txt == 'plot':
                btn = Button(self.window, height=2, width=4, padx=padx, pady=pady, text=txt,
                             command=lambda: self.plot(mass))
                btn.grid(row=2, column=1, padx=1, pady=1)
            elif txt == 'quit':
                btn = Button(self.window, height=2, width=4, padx=padx, pady=pady, text=txt,
                             command=lambda: self.quit())
                btn.grid(row=3, column=1, padx=1, pady=1)
            elif txt == 'reset output':
                btn = Button(self.window, height=2, width=10, padx=padx, pady=pady, text=txt,
                             command=lambda: self.reset_output())
                btn.grid(row=4, column=1, padx=1, pady=1)

        self.output.insert(INSERT, 'SiHx + 2 H2O = SiO2+ (2+x/2) H2')
        self.window.mainloop()

    def quit(self):
        self.window.destroy()

    def clear(self):
        self.mass_string.set('')

        self.x_string.set('')
        plt.clf()

    def close(self):
        plt.close('all')

    def reset_output(self):
        self.output.delete('1.0', END)
        self.output.insert(INSERT, 'SiHx + 2 H2O = SiO2+ (2+x/2) H2')
    def plot(self, mass):
        try:
            mass = Fraction(self.mass_string.get())

            if int(mass) < 0:
                raise Exception
        except Exception:
            self.mass_string.set('error')

        try:
            x = self.x_string.get()

            if x.isdigit() is not True or int(x) not in range(4):
                raise Exception

        except Exception:
            self.x_string.set('error')
            return False;



        result0 = (2 * 22.4 * mass) / (28)
        result1 = (2.5 * 22.4 * mass) / (29)
        result2 = (3 * 22.4 * mass) / (30)
        result3 = (3.5 * 22.4 * mass) / (31)

        if int(x) == 0:
            self.output.insert(INSERT, '\nx ')
            self.output.insert(INSERT, '= 0')
            self.output.insert(INSERT, "\n\nSi + 2H2O = SiO2 + 2H2 \n\n")
            self.output.insert(INSERT, result0)
            self.output.insert(INSERT, " liters of Hydrogen was allocated")
            self.output.see(END)
        elif int(x) == 1:
            self.output.insert(INSERT, '\nx ')
            self.output.insert(INSERT, '= 1')
            self.output.insert(INSERT, "\n\n2SiH + 4H2O = 2SiO2 + 5H2 \n\n")
            self.output.insert(INSERT, result1)
            self.output.insert(INSERT, " liters of Hydrogen was allocated")
            self.output.see(END)
        elif int(x) == 2:
            self.output.insert(INSERT, '\nx ')
            self.output.insert(INSERT, '= 2')
            self.output.insert(INSERT, "\n\nSiH2 + 2 H2O = SiO2 + 3H2 \n\n")
            self.output.insert(INSERT, result2)
            self.output.insert(INSERT, " liters of Hydrogen was allocated")
            self.output.see(END)
        elif int(x) == 3:
            self.output.insert(INSERT, '\nx ')
            self.output.insert(INSERT, '= 3')
            self.output.insert(INSERT, "\n\n2SiH3 + 4H2O = 2SiO2 + 7H2 \n\n")
            self.output.insert(INSERT, result3)
            self.output.insert(INSERT, " liters of Hydrogen was allocated")
            self.output.see(END)

        plt.ion()
        plt.plot([result0, result1, result2, result3], [0, 1, 2, 3], 'ro-')
        plt.axis([0, result3 + 200, 0, 4])
        plt.ylabel('X')
        plt.xlabel('H2 AMOUNT, liters')
        plt.autoscale(enable=True, axis='both', tight=None)
        plt.show()


app()