import wx


class MyApp(wx.App):
	def OnInit(self):
		frame = MyFrame("Hello World",(50,60),(450,340))
		frame.Show()
		self.SetTopWindow(frame)
		return True

class MyFrame(wx.Frame):
	def __init__(self,title,pos,size):
		wx.Frame.__init__(self,None,-1, title,pos,size)
		menuFile = wx.Menu()
		menuFile.Append(1, "&About")
		menuFile.AppendSeparator()
		menuFile.Append(2, "&Exit")
		menuBar = wx.MenuBar()
		menuBar.Append(menuFile,"&File")
		self.SetMenuBar(menuBar)
		self.CreateStatusBar()
		self.SetStatusText("Welcome to wxPython")
		self.Bind(wx.EVT_MENU, self.OnAbout, id=1)
		self.Bind(wx.EVT_MENU, self.OnQuit, id=2)


	def OnQuit(self,event):
		self.Close()

	def OnAbout(self,event):
		wx.MessageBox("This is a simple Wxpython hello World sample","About Hello world",wx.OK|wx.ICON_INFORMATION,self)
	def inputbox(self):
		app = wx.MyApp()
		dialog = wx.TextEntryDialog(None, "Enter Your message","Text entry","",style=wx.OK|wx.CANCEL)
		if dialog.ShowModal()==wx.ID_OK:
			return dialog.GetValue()