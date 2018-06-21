import wx

def ToolBar(self):
    #ToolBar
    self.toolbar = self.CreateToolBar()
    self.new_tool = self.toolbar.AddTool(wx.ID_NEW, 'New', wx.Bitmap('icons/gtk-new.png'))
    self.open_tool = self.toolbar.AddTool(wx.ID_OPEN, 'Open', wx.Bitmap('icons/gtk-open.png'))
    self.save_tool = self.toolbar.AddTool(wx.ID_SAVE, 'Save', wx.Bitmap('icons/gtk-save.png'))
    self.save_as_tool = self.toolbar.AddTool(wx.ID_SAVEAS, 'Save As', wx.Bitmap('icons/gtk-save-as.png'))
    self.toolbar.AddSeparator()
    self.undo_tool = self.toolbar.AddTool(wx.ID_ANY, 'Undo', wx.Bitmap('icons/gtk-undo-ltr.png'))
    self.redo_tool = self.toolbar.AddTool(wx.ID_ANY, 'Redo', wx.Bitmap('icons/gtk-redo-ltr.png'))
    self.toolbar.AddSeparator()
    self.cut_tool = self.toolbar.AddTool(wx.ID_ANY, 'Cut', wx.Bitmap('icons/gtk-cut.png'))
    self.copy_tool = self.toolbar.AddTool(wx.ID_ANY, 'Copy', wx.Bitmap('icons/gtk-copy.png'))
    self.paste_tool = self.toolbar.AddTool(wx.ID_ANY, 'Paste', wx.Bitmap('icons/gtk-paste.png'))
    self.toolbar.AddSeparator()
    self.zoom_in_tool = self.toolbar.AddTool(wx.ID_ANY, 'Zoom Out', wx.Bitmap('icons/gtk-zoom-in.png'))
    self.zoom_out_tool = self.toolbar.AddTool(wx.ID_ANY, 'Zoom In', wx.Bitmap('icons/gtk-zoom-out.png'))
    self.toolbar.AddSeparator()
    self.quit_tool = self.toolbar.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('icons/gtk-quit.png'))
