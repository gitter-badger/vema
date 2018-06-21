import wx

def ToolsMenu(self):
    #Tools Menu
    self.toolsmenu = wx.Menu()
    self.command = self.toolsmenu.Append(wx.ID_ANY, "&Command", "Enter in commands")
