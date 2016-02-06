from fractions import Fraction
import Tkinter as tk


class window2:
    def __init__(self, master1):
        self.panel2 = tk.Frame(master1)
        self.panel2.grid()
        self.button2 = tk.Button(self.panel2, text = "Quit", command = self.panel2.quit)
        self.button2.grid()
        vcmd = (master1.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.text1 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd)
        self.text1.grid()
        self.text1.focus()

    def validate(self, action, index, value_if_allowed,
                       prior_value, mass, validation_type, trigger_type, widget_name):
        if mass in "0123456789.-+/":
            try:
                Fraction(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

root1 = tk.Tk()
window2(root1)
root1.mainloop()
