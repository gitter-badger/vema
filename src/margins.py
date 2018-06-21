import main
import functions.control

def Margins(self):
    self.control.SetViewWhiteSpace(False)
    self.control.SetMargins(5, 0)
    self.control.SetMarginType(1, stc.STC_MARGIN_NUMBER)
    self.control.SetMarginWidth(1, self.leftMarginWidth)
