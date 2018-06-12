import os
import wx
import webbrowser
import wx.stc as stc
import wx.lib.dialogs

#Main class
class Window(wx.Frame):
    def __init__(self, parent, title):
        #Filename and Directory name
        self.filename = ''
        self.dirname = ''

        #Line numbers enabled
        self.lineNumbersEnabled = True

        #Sets left margins width to be
        self.leftMarginWidth = 25

        #Window
        wx.Frame.__init__(self, parent, title=title, size=(600, 400))
        self.control = stc.StyledTextCtrl(self, style=wx.TE_MULTILINE | wx.TE_WORDWRAP)
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("favicon.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)

        self.SetupFunctions()

    def SetupFunctions(self):
        self.Margins()
        self.Status_Bar()
        self.FileMenu(), self.EditMenu(), self.ViewMenu(), self.ToolsMenu(), self.HelpMenu()
        self.MenuBar()
        self.ToolBar()
        self.BindsMenu()
        self.BindsTool()

    def Margins(self):
        self.control.SetViewWhiteSpace(False)
        self.control.SetMargins(5, 0)
        self.control.SetMarginType(1, stc.STC_MARGIN_NUMBER)
        self.control.SetMarginWidth(1, self.leftMarginWidth)

    def Status_Bar(self):
        #Status Bar
        self.statusbar = wx.StatusBar(self, 1)
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1,-1, 110])
        self.SetStatusBar(self.statusbar)
        self.StatusLineColumn(self)

    def FileMenu(self):
        #File Menu
        self.filemenu = wx.Menu()
        self.new = self.filemenu.Append(wx.ID_NEW, "&New", "Create new document")
        self.open = self.filemenu.Append(wx.ID_OPEN, "&Open", "Open existing document")
        self.save = self.filemenu.Append(wx.ID_SAVE, "Save")
        self.save_as = self.filemenu.Append(wx.ID_SAVEAS, "Save &As")
        self.filemenu.AppendSeparator()
        self.quit = self.filemenu.Append(wx.ID_EXIT, "&Quit")

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

    def ViewMenu(self):
        #View Menu
        self.viewmenu = wx.Menu()
        self.toglinenumbers = self.viewmenu.Append(wx.ID_ANY, "Toggle &Line Numbers", "Enable/Disable line numbers", wx.ITEM_CHECK)
        self.viewmenu.AppendSeparator()
        self.togstatusbar = self.viewmenu.Append(wx.ID_ANY, "Toggle &Status Bar", "Enable/Disable status bar", wx.ITEM_CHECK)
        self.viewmenu.AppendSeparator()
        self.zoom_in = self.viewmenu.Append(wx.ID_ZOOM_IN, "Zoom &In", "Zoom in to the applicaton")
        self.zoom_out = self.viewmenu.Append(wx.ID_ZOOM_OUT, "Zoom &Out", "Zoom out the applicaton")

    def ToolsMenu(self):
        #Tools Menu
        self.toolsmenu = wx.Menu()
        self.command = self.toolsmenu.Append(wx.ID_ANY, "&Command", "Enter in commands")

    def HelpMenu(self):
        #Help Menu
        self.helpmenu = wx.Menu()
        self.about = self.helpmenu.Append(wx.ID_ABOUT, "&About", "About Vema")
        self.helpmenu.AppendSeparator()
        self.github = self.helpmenu.Append(wx.ID_ANY, "&Github", "Vema's Github")
        self.gitlab = self.helpmenu.Append(wx.ID_ANY, "&Gitlab", "Vema's Gitlab")

    def MenuBar(self):
        #MenuBar
        self.menu = wx.MenuBar()
        self.menu.Append(self.filemenu, "&File")
        self.menu.Append(self.editmenu, "&Edit")
        self.menu.Append(self.viewmenu, "&View")
        self.menu.Append(self.toolsmenu, "&Tools")
        self.menu.Append(self.helpmenu, "&Help")
        self.SetMenuBar(self.menu)

    def ToolBar(self):
        #ToolBar
        self.toolbar = self.CreateToolBar()
        self.new_tool = self.toolbar.AddTool(wx.ID_NEW, 'New', wx.Bitmap('icons/gtk-new.png'), 'New')
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
        self.Bind(wx.EVT_MENU, self.Github, self.github)
        self.Bind(wx.EVT_MENU, self.Gitlab, self.gitlab)
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

    #Menu item functions
    def New(self, e):
        self.control.SetValue("")

    def Open(self, e):
        try:
            dig = wx.FileDialog(self, "Select a file", self.dirname, "", "*.*", wx.FD_OPEN)
            if(dig.ShowModal() == wx.ID_OK):
                self.filename = dig.GetFilename()
                self.dirname = dig.GetDirectory()
                f = open(os.path.join(self.dirname, self.filename), 'r')
                self.control.SetValue(f.read())
                f.close()
            dig.Destroy()
        except:
            dig = wx.MessageDialog(self, "Error loading file", "Error", wx.ICON_ERROR)
            dig.ShowModal()
            dig.Destroy()

    def Save(self, e):
        try:
            f = open(os.path.join(self.dirname, self.filename), 'w')
            f.write(self.control.GetValue())
            f.close()
        except:
            try:
                dig = wx.FileDialog(self, "Save file as", self.dirname, "Untitled", "*.*", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
                if (dig.ShowModal() == wx.ID_OK):
                    self.filename = dig.GetFilename()
                    self.dirname = dig.GetDirectory()
                    f = open(os.path.join(self.dirname, self.filename), 'w')
                    f.write(self.control.GetValue())
                    f.close()
                dig.Destroy()
            except:
                pass

    def SaveAs(self, e):
        try:
            dig = wx.FileDialog(self, "Save file as", self.dirname, "Untitled", "*.*", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
            if (dig.ShowModal() == wx.ID_OK):
                self.filename = dig.GetFilename()
                self.dirname = dig.GetDirectory()
                f = open(os.path.join(self.dirname, self.filename), 'w')
                f.write(self.control.GetValue())
                f.close()
            dig.Destroy()
        except:
            pass

    def Command(self, e):
    	dig = wx.TextEntryDialog(self, 'Enter command', 'Command')
    	dig.Destroy()

    def Quit(self, e):
        self.Close(True)

    def Undo(self, e):
        self.control.Undo()

    def Redo(self, e):
        self.control.Redo()

    def Cut(self, e):
        self.control.Cut()

    def Copy(self, e):
        self.control.Copy()

    def Paste(self, e):
        self.control.Paste()

    def Delete(self, e):
        self.control.DeleteBack()

    def SelectAll(self, e):
        self.control.SelectAll()

    def ZoomIn(self, e):
        self.control.ZoomIn()

    def ZoomOut(self, e):
        self.control.ZoomOut()

    def TogLineNumbers(self, e):
        if self.lineNumbersEnabled:
            self.control.SetMarginWidth(1, 0)
            self.lineNumbersEnabled = False
        else:
            self.control.SetMarginWidth(1, self.leftMarginWidth)
            self.lineNumbersEnabled = True

    def TogStatusBar(self, e):
        if self.statusbar.IsShown():
            self.statusbar.Hide()
            self.Update()
        else:
            self.statusbar.Show()

    def About(self, e):
        dig = wx.MessageDialog(self, "Vema is a lightweight text editor that is created and maintained by Mohamed Altarawy at https://github.com/Altarawy and runs under the GNU General Public License at https://www.gnu.org/licenses/gpl-3.0.en.html.", "About", wx.OK)
        dig.ShowModal()
        dig.Destroy()

    def Github(self, e):
        webbrowser.open('https://github.com/vemac')

    def Gitlab(self, e):
        webbrowser.open('https://gitlab.com/vema')

    def StatusLineColumn(self, e):
        line = self.control.GetCurrentLine() + 1
        col = self.control.GetColumn(self.control.GetCurrentPos())
        stat = "Line %s, Column %s" % (line, col)
        self.statusbar.SetStatusText(stat, 2)

    #Key binds
    def CharEvent(self, e):
        keycode = e.GetKeyCode()
        if (keycode == 14):
            self.New(self)
        elif (keycode == 15):
            self.Open(self)
        elif (keycode == 19):
            self.Save(self)

def main():
    app = wx.App()
    frame = Window(None, "Vema")
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
