import wx
import menu.filemenu
import menu.editmenu
import menu.viewmenu
import menu.toolmenu
import menu.helpmenu

def MenuBar(self):
    #MenuBar
    self.menu = wx.MenuBar()
    self.menu.Append(self.filemenu, "&File")
    self.menu.Append(self.editmenu, "&Edit")
    self.menu.Append(self.viewmenu, "&View")
    self.menu.Append(self.toolsmenu, "&Tools")
    self.menu.Append(self.helpmenu, "&Help")
    self.SetMenuBar(self.menu)
