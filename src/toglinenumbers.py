import functions.control
import margins
import functions.variables.linenumbersenabled

def TogLineNumbers(self, e):
    if self.lineNumbersEnabled:
        self.control.SetMarginWidth(1, 0)
        self.lineNumbersEnabled = False
    else:
        self.control.SetMarginWidth(1, self.leftMarginWidth)
        self.lineNumbersEnabled = True
