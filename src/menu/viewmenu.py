import wx

def ViewMenu(self):
    #View Menu
    self.viewmenu = wx.Menu()
    self.toglinenumbers = self.viewmenu.Append(wx.ID_ANY, "Toggle &Line Numbers", "Enable/Disable line numbers")
    self.viewmenu.AppendSeparator()
    self.togstatusbar = self.viewmenu.Append(wx.ID_ANY, "Toggle &Status Bar", "Enable/Disable status bar")
    self.viewmenu.AppendSeparator()
    self.zoom_in = self.viewmenu.Append(wx.ID_ZOOM_IN, "Zoom &In", "Zoom in to the applicaton")
    self.zoom_out = self.viewmenu.Append(wx.ID_ZOOM_OUT, "Zoom &Out", "Zoom out the applicaton")
