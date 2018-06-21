import wx
import control
import variables.filename
import variables.dirname
import os

def Open(self, e):
    try:
        dlg = wx.FileDialog(self, "Select a file", self.dirname, "", "*.*", wx.FD_OPEN)
        if(dlg.ShowModal() == wx.ID_OK):
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()
    except:
        dlg = wx.MessageDialog(self, "Error loading file", "Error", wx.ICON_ERROR)
        dlg.ShowModal()
        dlg.Destroy()
