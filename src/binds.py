import toolbar
import menu.filemenu
import menu.editmenu
import menu.viewmenu
import menu.toolmenu
import menu.helpmenu
import functions.control
import functions.new
import functions.open
import functions.save
import functions.save_as
import functions.command
import functions.quit
import functions.undo
import functions.redo
import functions.cut
import functions.copy
import functions.paste
import functions.delete
import functions.select_all
import functions.zoom_in
import functions.zoom_out
import toglinenumbers
import togstatusbar
import functions.about
import functions.github

def BindsMenu(self):
    #Binding menu functions and items
    self.Bind(wx.EVT_MENU, self.New, self.new)
    self.Bind(wx.EVT_MENU, self.Open, self.open)
    self.Bind(wx.EVT_MENU, self.Save, self.save)
    self.Bind(wx.EVT_MENU, self.SaveAs, self.save_as)
    self.Bind(wx.EVT_MENU, self.Command, self.command)
    self.Bind(wx.EVT_MENU, self.Quit, self.quit)
    self.Bind(wx.EVT_MENU, self.Undo, self.undo)
    self.Bind(wx.EVT_MENU, self.Redo, self.redo)
    self.Bind(wx.EVT_MENU, self.Cut, self.cut)
    self.Bind(wx.EVT_MENU, self.Copy, self.copy)
    self.Bind(wx.EVT_MENU, self.Paste, self.paste)
    self.Bind(wx.EVT_MENU, self.Delete, self.delete)
    self.Bind(wx.EVT_MENU, self.SelectAll, self.select_all)
    self.Bind(wx.EVT_MENU, self.ZoomIn, self.zoom_in)
    self.Bind(wx.EVT_MENU, self.ZoomOut, self.zoom_out)
    self.Bind(wx.EVT_MENU, self.TogLineNumbers, self.toglinenumbers)
    self.Bind(wx.EVT_MENU, self.TogStatusBar, self.togstatusbar)
    self.Bind(wx.EVT_MENU, self.About, self.about)
    self.Bind(wx.EVT_MENU, self.GitHub, self.github)
    self.control.Bind(wx.EVT_KEY_UP, self.StatusLineColumn)

def BindsTool(self):
    #Binding menu functions and toolbar
    self.Bind(wx.EVT_MENU, self.New, self.new_tool)
    self.Bind(wx.EVT_MENU, self.Open, self.open_tool)
    self.Bind(wx.EVT_MENU, self.Save, self.save_tool)
    self.Bind(wx.EVT_MENU, self.SaveAs, self.save_as_tool)
    self.Bind(wx.EVT_MENU, self.Undo, self.undo_tool)
    self.Bind(wx.EVT_MENU, self.Redo, self.redo_tool)
    self.Bind(wx.EVT_MENU, self.Cut, self.cut_tool)
    self.Bind(wx.EVT_MENU, self.Copy, self.copy_tool)
    self.Bind(wx.EVT_MENU, self.Paste, self.paste_tool)
    self.Bind(wx.EVT_MENU, self.ZoomIn, self.zoom_in_tool)
    self.Bind(wx.EVT_MENU, self.ZoomOut, self.zoom_out_tool)
    self.Bind(wx.EVT_MENU, self.Quit, self.quit_tool)
    self.toolbar.Realize()
