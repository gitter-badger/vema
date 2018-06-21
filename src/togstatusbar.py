import statusbar

def TogStatusBar(self, e):
    if self.statusbar.IsShown():
        self.statusbar.Hide()
        self.Update()
    else:
        self.statusbar.Show()
