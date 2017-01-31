import wx

def ip():
    app = wx.PySimpleApp()
    dialog = wx.TextEntryDialog(None, 
            "Enter you message here.",
            "Text Entry", "", style=wx.OK|wx.CANCEL)
    if dialog.ShowModal() == wx.ID_OK:
        return dialog.GetValue()
    
