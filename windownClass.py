import wx


class WindownClass(wx.Frame):
    def __init__(self, parent, title, size):
        super(WindownClass, self).__init__(parent, title=title, size=size)

        self.Centre()
        self.Show(True)
        self.CreateStatusBar()
