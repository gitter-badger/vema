def StatusLineColumn(self, e):
    line = self.control.GetCurrentLine() + 1
    col = self.control.GetColumn(self.control.GetCurrentPos())
    stat = "Line %s, Column %s" % (line, col)
    self.statusbar.SetStatusText(stat, 1)
