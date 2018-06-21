import wx

def About(self, e):
    dlg = wx.MessageDialog(self, "Vema is a lightweight text editor that is created and maintained by Mohamed Altarawy at https://github.com/Altarawy and runs under the GNU General Public License at https://www.gnu.org/licenses/gpl-3.0.en.html.", "About", wx.OK)
    dlg.ShowModal()
    dlg.Destroy()
