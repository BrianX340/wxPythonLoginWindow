from req import *

cwd = os.getcwd()


app = wx.App()

#Creamos la base de datos si no existe
crear_bd()

# Creamos la ventana principal
frame1 = Frame1(None, -1, "X-Login")
frame1.Centre()

# Creamos el panel
image_file = (cwd+'\\source\\menu.jpg')
panel1 = Panel1(frame1, -1,image_file)

#Agregamos botones al panel
login_img = img_dir(cwd+'\\source\\login_button.png')
panel1.button_login = wx.BitmapButton(panel1.bitmap1, -1, bitmap=login_img, pos=(80, 200), size=(135, 45), style=0)
panel1.button_login.Bind( event=wx.EVT_BUTTON, handler=lambda x=None:[frame1.Hide(),login(self=frame1)])

register_img = img_dir(cwd+'\\source\\register_button.png')
panel1.button_exit = wx.BitmapButton(panel1.bitmap1, -1, bitmap=register_img, pos=(80, 270), size=(135, 45), style=0)
panel1.button_exit.Bind( event=wx.EVT_BUTTON, handler=lambda x=None:[frame1.Hide(),register(self=frame1)])

exit_img = img_dir(cwd+'\\source\\exit_button.png')
panel1.button_exit = wx.BitmapButton(panel1.bitmap1, -1, bitmap=exit_img, pos=(80, 340), size=(135, 45), style=0)
panel1.button_exit.Bind( event=wx.EVT_BUTTON, handler=lambda x=None:[frame1.Destroy()])

#Mostramos la ventana
frame1.Show(True)


app.MainLoop()