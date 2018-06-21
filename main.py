import os
import wx
import setupfunctions
import src.functions.control

#Main class
class Window(wx.Frame):
    def __init__(self, parent, title):
        #Window
        wx.Frame.__init__(self, parent, title=title, size=(600, 400))
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("favicon.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)

        setupfunctions.SetupFunctions(self)

def main():
    app = wx.App()
    frame = Window(None, "Vema")
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
