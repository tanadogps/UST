from tkinter import filedialog
from tkinter import * 
from PIL import Image
import os

s_path = 'C:\\Users\\BRUNO\\Desktop\\CNN\\UST\\van_gogh.png'
c_path = 'C:\\Users\\BRUNO\\Desktop\\CNN\\UST\\tiger.png'
output_path = 'C:\\Users\\BRUNO\\Desktop\\CNN\\UST\\outputs'


def run():
    alpha = str(alpha_scale.get()/100)
    mastercode = 'python stylize.py --checkpoints models/relu5_1 models/relu4_1 models/relu3_1 models/relu2_1 models/relu1_1 --relu-targets relu5_1 relu4_1 relu3_1 relu2_1 relu1_1 --style-size 512 --alpha ' + alpha + ' --style-path ' + s_path + ' --content-path ' + c_path + ' --out-path ' + output_path
    print(mastercode)
    os.system(mastercode)

window = Tk()
#Geometria da janela (width x height + left distance + top distance)
window.geometry("1000x800+50+50")

def import_style():
    global s_path
    window.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
    s_path = window.filename
    s_path = s_path.replace('/','\\')
    #change_style()



def import_content():
    global c_path
    window.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
    c_path = window.filename
    c_path = c_path.replace('/','\\')


def save_output():
    global output_path
    window.filename = filedialog.askdirectory()
    output_path = window.filename
    output_path = output_path.replace('/','\\')

def change_style():
    #import image with PIL
    style_example = Image.open(s_path)
    #resize to new (width, height)
    style_example = style_example.resize((200,200), Image.ANTIALIAS)
    #convert to tkinter format 
    style_example.save("pic1.ppm", "ppm")
    pic1 = PhotoImage(file='pic1.ppm')
    lb2 = Label(window, image = pic1)
    lb2.place(x=400, y=150)
    



alpha_scale = Scale(window, from_=0, to=100, length=500,tickinterval=10, orient=HORIZONTAL)
alpha_scale.set(60)
alpha_scale.place(x=100, y=500)

#change_style()

lb1 = Label(window, text="Universal Style Transfer - Graphical User Interface", bd=16, relief="sunken", font = 'Times 28')
lb1.place(x=120, y=50)

#import image with PIL
#style_example = Image.open(s_path)
#resize to new (width, height)
#style_example = style_example.resize((200,200), Image.ANTIALIAS)
#convert to tkinter format 
#style_example.save("pic1.ppm", "ppm")
#pic1 = PhotoImage(file='pic1.ppm')
#lb2 = Label(window, image = pic1, bd=16, relief="ridge")
#lb2.place(x=400, y=150)

#lb_plus = Label(window, text = '+', font = 'Times 40')
#lb_plus.place(x=350, y=240)

#import image with PIL
#content_example = Image.open(c_path)
#resize to new (width, height)
#content_example = content_example.resize((200,200), Image.ANTIALIAS)
#convert to tkinter format 
#content_example.save("pic2.ppm", "ppm")
#pic2 = PhotoImage(file='pic2.ppm')
#lb3 = Label(window, image = pic2, bd=16, relief="ridge")
#lb3.place(x=100, y=150)

#lb_equal = Label(window, text = '=', font = 'Times 40')
#lb_equal.place(x=650, y=240)

#lb_alpha = Label(window, text = 'Style Parameter', font = 'Times 20', bd=8, relief ='ridge')
#lb_alpha.place(x=650, y=500)

#import image with PIL
#output_example = Image.open(output_path + '\\tiger_van_gogh.png')
#resize to new (width, height)
#output_example = output_example.resize((200,200), Image.ANTIALIAS)
#convert to tkinter format 
#output_example.save("pic3.ppm", "ppm")
#pic3 = PhotoImage(file='pic3.ppm')
#lb4 = Label(window, image = pic3, bd=16, relief="ridge")
#lb4.place(x=700, y=150)


bt1 = Button(window, width=20, text="Style Image", command = import_style)
bt1.place(x=100, y=650)
bt2 = Button(window, width=20, text="Content Image", command = import_content)
bt2.place(x=100, y=700)
bt3 = Button(window, width=20, text="Output Folder", command = save_output)
bt3.place(x=500, y=680)
bt4 = Button(window, width=20, text="Run", command = run)
bt4.place(x=800, y=680)


window.mainloop()