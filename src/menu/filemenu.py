import wx

def FileMenu(self):
    #File Menu
    self.filemenu = wx.Menu()
    self.new = self.filemenu.Append(wx.ID_NEW, "&New", "Create new document")
    self.open = self.filemenu.Append(wx.ID_OPEN, "&Open", "Open existing document")
    self.save = self.filemenu.Append(wx.ID_SAVE, "Save")
    self.save_as = self.filemenu.Append(wx.ID_SAVEAS, "Save &As")
    self.filemenu.AppendSeparator()
    self.quit = self.filemenu.Append(wx.ID_EXIT, "&Quit")
