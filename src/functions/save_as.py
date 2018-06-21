import wx
import control
import variables.filename
import variables.dirname
import os

def SaveAs(self, e):
    try:
        dlg = wx.FileDialog(self, "Save file as", self.dirname, "Untitled", "*.*", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if (dlg.ShowModal() == wx.ID_OK):
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'w')
            f.write(self.control.GetValue())
            f.close()
        dlg.Destroy()
    except:
        pass
