import wx

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        self.init_ui()

    def on_close(self, e):
        self.Close(True)    

    def init_ui(self):   
        pnl = wx.Panel(self)
        cbtn = wx.Button(pnl, label='Close', pos=(20, 30))
        cbtn.Bind(wx.EVT_BUTTON, self.on_close)
        self.SetSize((250, 200))
        self.SetTitle('wx.Button')
        self.Centre()
        self.Show(True)          

def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()
    
main()
