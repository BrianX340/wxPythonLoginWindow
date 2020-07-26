import wx
import sqlite3
import hashlib
import os

cwd = os.getcwd()

#################################   Clases   #################################

class Frame1(wx.Frame):
    
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title,size=(300,535))
        self.parent=parent
    
class Panel1(wx.Panel):
    """La clase panel1 crea un panel con una imagen de fondo"""
    def __init__(self, parent, id,image_file):
        # Creamos el panel
        wx.Panel.__init__(self, parent, id)
        image_file = image_file
        try:
            bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            # image's upper left corner anchors at panel coordinates (0, 0)
            self.bitmap1 = wx.StaticBitmap(self, -1, bmp1, (0, 0))
        except IOError:
            print("Image file %s not found" % imageFile)
            raise SystemExit



#################################   Funciones   #################################

def crear_bd():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    try:
        cursor.execute('''
            CREATE TABLE usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(100) UNIQUE NOT NULL)''')
        conexion.close()
    except sqlite3.OperationalError:
        print("Ya existe la tabla")
    else:
        print("La tabla usuarios se ha creado")

def login(self):
    frame_login = Frame1(self, -1, "X-login")
    frame_login.Centre()

    panel_login = wx.Panel(frame_login, -1)
    image_file = (cwd+'\\source\\login.jpg')
    bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
    panel_login.bitmap1 = wx.StaticBitmap(panel_login, -1, bmp1, (0, 0))
    
    
    
    userName = wx.TextCtrl(panel_login, -1, "", size=(175, -1),pos=(110,227))
    userName.SetInsertionPoint(0)
    
    passw = wx.TextCtrl(panel_login, -1, "", size=(175, -1),pos=(110,279),style=wx.TE_PASSWORD)
    passw.SetInsertionPoint(0)
    
    panel_login.button_confirm = wx.Button(panel_login.bitmap1, -1, 'Confirm', (110, 370))
    panel_login.button_confirm.Bind(wx.EVT_BUTTON, handler=lambda x=None:[verify(self=self,user=userName.GetValue(),
                                                                                  passw=passw.GetValue()),
                                                                             frame_login.Destroy(),
                                                                             self.Show(True)
                                                                            ])
    
    panel_login.button_cancel = wx.Button(panel_login.bitmap1, -1, 'Cancel', (110, 400))
    panel_login.button_cancel.Bind(wx.EVT_BUTTON, handler=lambda x=None:[frame_login.Destroy(),self.Show(True)])
    
    frame_login.Show(True)
    frame_login.Bind(wx.EVT_CLOSE, handler=lambda x=None:[frame_login.Destroy(),
                                                            self.Show(True)] )

def register(self):
    frame_register = Frame1(self, -1, "X-Register")
    frame_register.Centre()

    panel_register = wx.Panel(frame_register, -1)
    image_file = (cwd+'\\source\\register.jpg')
    bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
    panel_register.bitmap1 = wx.StaticBitmap(panel_register, -1, bmp1, (0, 0))
    
    #.SetBackgroundColour('#232321')
    
    
    userName = wx.TextCtrl(panel_register, -1, "", size=(175, -1),pos=(120,217))
    userName.SetInsertionPoint(0)
    
    email = wx.TextCtrl(panel_register, -1, "", size=(175, -1),pos=(120,262))
    email.SetInsertionPoint(0)

    passw = wx.TextCtrl(panel_register, -1, "", size=(175, -1),pos=(120,310),style=wx.TE_PASSWORD)
    passw.SetInsertionPoint(0)
    
    panel_register.button_confirm = wx.Button(panel_register.bitmap1, -1, 'Confirm', (110, 370))
    panel_register.button_confirm.Bind(wx.EVT_BUTTON, handler=lambda x=None:[dataSave(self=self,userName=userName.GetValue(),
                                                                                  email=email.GetValue(),
                                                                                  passw=passw.GetValue()),
                                                                             frame_register.Destroy(),
                                                                             self.Show(True)
                                                                            ])
    
    panel_register.button_cancel = wx.Button(panel_register.bitmap1, -1, 'Cancel', (110, 400))
    panel_register.button_cancel.Bind(wx.EVT_BUTTON, handler=lambda x=None:[frame_register.Destroy(),self.Show(True)])
    
    frame_register.Show(True)
    frame_register.Bind(wx.EVT_CLOSE, handler=lambda x=None:[frame_register.Destroy(),
                                                            self.Show(True)] )

def crypt(clave):
    enc = hashlib.sha256(clave.encode('utf-8')).hexdigest()
    return enc


def dataSave(self,userName,email,passw):
    passw = crypt(passw)
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    
    try:
        entities = (userName, passw )
        cursor.execute("INSERT INTO usuarios(id, user, password) VALUES(null, ?,?)", entities)
        
    except sqlite3.IntegrityError:
        return wx.MessageDialog(self,message='User already exist!',caption='User error!').ShowModal()
    else:
        return wx.MessageDialog(self,message='You user has been created!',caption='Created User').ShowModal()
    
    conexion.commit()
    conexion.close()
    
    
def verify(self,user,passw):
    passw = crypt(passw)
    
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    a = cursor.execute("select * from usuarios where user=:user and password=:passw", {"user": user, "passw": passw})
    b = cursor.fetchone()
    if b:
        return wx.MessageDialog(self,message='You has been Login!',caption='Loged User').ShowModal()
    else:
        return wx.MessageDialog(self,message='Invalid Account!',caption='Login Error').ShowModal()

    conexion.close()

def img_dir(dirr):
    bitmap = wx.Image(dirr, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
    return bitmap