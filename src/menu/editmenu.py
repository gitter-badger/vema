import wx

def EditMenu(self):
    #Edit Menu
    self.editmenu = wx.Menu()
    self.undo = self.editmenu.Append(wx.ID_UNDO, "&Undo", "Undo last step")
    self.redo = self.editmenu.Append(wx.ID_REDO, "&Redo", "Redo last step")
    self.editmenu.AppendSeparator()
    self.cut = self.editmenu.Append(wx.ID_CUT, "&Cut", "Cut selected text")
    self.copy = self.editmenu.Append(wx.ID_COPY, "&Copy", "Copy selected text")
    self.paste = self.editmenu.Append(wx.ID_PASTE, "&Paste", "Paste copied text")
    self.delete = self.editmenu.Append(wx.ID_DELETE, "&Delete", "Delete selected text")
    self.editmenu.AppendSeparator()
    self.select_all = self.editmenu.Append(wx.ID_SELECTALL, "&Select All", "Select the entire document")
