import wx

def chat(msg):
    app = wx.PySimpleApp()
    dialog = wx.TextEntryDialog(None, 
            msg,
            "Text Entry", "", style=wx.OK|wx.CANCEL)
    if dialog.ShowModal() == wx.ID_OK:
    	return dialog.GetValue()

    dialog.Destroy()
