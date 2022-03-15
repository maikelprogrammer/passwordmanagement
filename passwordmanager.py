from tkinter import *
from tkinter import  messagebox
from random import randint,choice,shuffle
import pyperclip

#password generator
def password_generator():
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers_case = "0123456789"
    symbols_case = "!@#$%^&[]{}"

    lower = [choice(lower_case) for _ in range(randint(3, 5))]
    upper = [choice(upper_case) for _ in range(randint(3, 5))]
    numbers = [choice(numbers_case) for _ in range(randint(2, 4))]
    symbols = [choice(symbols_case) for _ in range(randint(2, 4))]

    password_list = lower + upper + numbers + symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

#data storing
def on_button():
    website_data=(website_entry.get())
    email_data=(email_entry.get())
    password_data=(password_entry.get())
    all_data=f"{website_data} | {email_data} | {password_data}\n"

    if len(website_data)==0 or len(password_data)==0 or len(email_data) ==0:
        messagebox.showerror(title="oops", message="please don't leave any field empty")
    else:
        message_box=messagebox.askokcancel(title=website_data,message=f"these are the"
                                                          f" details entered:\n email: {email_data}\n"
                                                          f"password: {password_data}\n Is it ok to save?")
        if message_box:
            with open("data.txt", mode="a") as data:
                data.write(all_data)
                website_entry.delete(0,END)
                password_entry.delete(0,END)

#UI setup
window=Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
logo_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)

#labels
website_label=Label(text="Website:")
website_label.grid(column=0,row=1)

email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)

password_label=Label(text="Password:")
password_label.grid(column=0,row=3)

#entries
website_entry=Entry(width=35)
website_entry.grid(row=1,column=1, columnspan=2)
website_entry.focus()

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1, columnspan=2)


password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)

#buttons
generate_button=Button(text="Generate password",command=password_generator)
generate_button.grid(column=2,row=3)

add_button=Button(text="Add",width=36,command=on_button)
add_button.grid(row=4,column=1, columnspan=2)


window.mainloop()
