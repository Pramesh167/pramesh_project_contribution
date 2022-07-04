from tkinter import *
from PIL import Image, ImageTk
window=Tk()
window.title("Product")
window.geometry('640x420')
window.resizable(False,False)
window.config(bg="#0a3570")
product_img = ImageTk.PhotoImage(file="product.png")

my_canvas=Canvas(window,width=600,height=420,bg="#0a3570",highlightthickness=0,borderwidth=0)
my_canvas.create_image(0,0,image=product_img,anchor=NW)
my_canvas.pack(fill="both",expand=True)
add_btn=Button(window,text="ADD NEW PRODUCT",font=("comic sans",14,"normal"),
                     bg="#ffbd59",fg="#0c0c0c",border=0,activebackground="#ffbd59",activeforeground="#0c0c0c")
add_btn.place(x=87,y=123)
delete_btn=Button(window,text="DELETE PRODUCT",font=("comic sans",14,"normal"),
                     bg="#ffbd59",fg="#0c0c0c",border=0,activebackground="#ffbd59",activeforeground="#0c0c0c")
delete_btn.place(x=90,y=210)
Edit_btn=Button(window,text="EDIT QUANTITY",font=("comic sans",14,"normal"),
                     bg="#ffbd59",fg="#0c0c0c",border=0,activebackground="#ffbd59",activeforeground="#0c0c0c")
Edit_btn.place(x=93,y=303)
home=ImageTk.PhotoImage((Image.open("home icon.png")))
home_btn=Button(window, image=home,border=0,bg="#ffffff")
home_btn.place(x=10, y=5)
window.mainloop()

