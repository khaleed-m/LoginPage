from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root  = Tk()

def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email=='SRM@gmail.com' and password =='1234':
        messagebox.showinfo('Yayy',"Login Successful!")
    else:
        messagebox.showerror("ERROR",'Login Failed, please try again!')

root.title('login')

#providing the min size
#root.minsize(100,100)

#providing the max size
#root.maxsize(300,300)


root.geometry('350x500')
#adding an icon on the top left 
root.iconbitmap('designer.ico')

#addding background color
root.configure(background='#0096DC')


#adding an image to the GUI

#img = ImageTk.PhotoImage(Image.open('logo.png'))

img = Image.open('logo.png')
reseized_img =  img.resize((70,70))

img =ImageTk.PhotoImage(reseized_img)
img_label =Label(root,image= img)

#display the img we are using label / pady used to give some disatnce from top and bottom
img_label.pack(pady = (10,10))


text_label =Label(root, text='Filpkart', fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',24))

#HERE WE GIVING THE THE other line 
email_label=Label(root, text="Enter Your email ID",fg='white' ,bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=("verdana" ,14))
email_label.pack()


#taking input from the user
email_input =Entry(root,width=50)
email_input.pack(ipady = 6,pady=(20,5))
#email_input.config(font=('verdana',10))

#password text
password_label=Label(root, text="Enter the password",fg='white' ,bg='#0096DC')
password_label.pack(pady=(20,5))
password_label.config(font=("verdana" ,14))
password_label.pack()


#taking input from the user
password_input =Entry(root,show="*",width=50)
password_input.pack(ipady = 6,pady=(20,5))

login_btn=Button(root,text='Login Here' , width=20, height=2, command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',10))

root.mainloop()  #