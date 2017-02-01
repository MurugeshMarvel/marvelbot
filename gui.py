import wx

app = wx.App()

window = wx.Frame(None, style = wx.MAXIMIZE_BOX | wx.RESIZE_BORDER |wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
dialog = wx.TextEntryDialog(None, "Enter Your message","Text entry","",style=wx.OK|wx.CANCEL)
if dialog.ShowModal()==wx.ID_OK:
	print dialog.GetValue()
dialog.Show(True)

app.MainLoop()


	#def inputbox(self):
	#	app = wx.MyApp()
		