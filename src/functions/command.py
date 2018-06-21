import wx

def Command(self, e):
	dlg = wx.TextEntryDialog(self, 'Enter command', 'Command')
	dlg.Destroy()
