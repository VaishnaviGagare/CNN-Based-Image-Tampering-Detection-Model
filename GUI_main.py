import tkinter  as tk 
from tkinter import * 


from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  

root = tk.Tk()
#root.geometry('500x500')
#root.title("Login Form")


#------------------------------------------------------

root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("main")
#------------------Frame----------------------

# image2 =Image.open('A.jpg')
# image2 =image2.resize((750,890), Image.ANTIALIAS)

# background_image=ImageTk.PhotoImage(image2)
# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=250, y=0) #, relwidth=1, relheight=1)
# #
# def shift():
#     x1,y1,x2,y2 = canvas.bbox("marquee")
#     if(x2<0 or y1<0): #reset the coordinates
#         x1 = canvas.winfo_width()
#         y1 = canvas.winfo_height()//2
#         canvas.coords("marquee",x1,y1)
#     else:
#         canvas.move("marquee", -2, 0)
#     canvas.after(1000//fps,shift)

# canvas=tk.Canvas(root,bg="maroon")
# canvas.pack()
# text_var="Form Based Document Using OCR Using Machine Learning_Crime & Fake Document Prediction"
# text=canvas.create_text(0,-2000,text=text_var,font=('Raleway',25,'bold'),fill='white',tags=("marquee",),anchor='w')
# x1,y1,x2,y2 = canvas.bbox("marquee")
# width = 1600
# height = 100
# canvas['width']=width
# canvas['height']=height
# fps=40    #Change the fps to make the animation faster/slower
# shift()


#-------function------------------------

def reg():
    
##### tkinter window ######
    
    print("reg")
    from subprocess import call
    call(["python", "registration.py"])   



def login():
    
##### tkinter window ######
    
    print("log")
    from subprocess import call
    call(["python", "login.py"])   
    


def window():
    root.destroy()

#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('a1.png')
image2 =image2.resize((1400,700), Image.LANCZOS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


lbl = tk.Label(root, text="Image Foregery Detection", font=('times', 40,' bold '), height=1, width=50,bg="BLACK",fg="white")
lbl.place(x=0, y=0)

# framed = tk.LabelFrame(root, text=" --WELCOME-- ", width=400, height=300, bd=5, font=('times', 14, ' bold '),bg="seashell2")
# framed.grid(row=0, column=0, sticky='nw')
# framed.place(x=140, y=180)
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
button1 = tk.Button(root, text='Login Now',width=15,height=2,bd=5,bg='blue',font=('times', 15, ' bold '),fg='white',command=login).place(x=550,y=150)
button1 = tk.Button(root, text='Register',width=15,height=2,bd=5,bg='green',font=('times', 15, ' bold '),fg='white',command=reg).place(x=550,y=250)
exit = tk.Button(root, text="Exit", command=window, width=15, height=2, bd=5,font=('times', 15, ' bold '),bg="red",fg="white").place(x=550, y=350)

root.mainloop()
