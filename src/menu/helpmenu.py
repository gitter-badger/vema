import wx

def HelpMenu(self):
    #Help Menu
    self.helpmenu = wx.Menu()
    self.about = self.helpmenu.Append(wx.ID_ABOUT, "&About", "About Vema")
    self.helpmenu.AppendSeparator()
    self.github = self.helpmenu.Append(wx.ID_ANY, "&GitHub", "Vema's GitHub")
