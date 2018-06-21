import src.margins
import src.statusbar
import src.toolbar
import src.menubar
import src.binds

def SetupFunctions(self):
    self.Margins()
    self.Status_Bar()
    self.FileMenu(), self.EditMenu(), self.ViewMenu(), self.ToolsMenu(), self.HelpMenu()
    self.MenuBar()
    self.ToolBar()
    self.BindsMenu()
    self.BindsTool()
