from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD SEARCH  --------------------------------- #

def find_password():
    if len(email_user_entry.get()) == 0 or len(web_entry.get()) == 0:
        messagebox.showerror(title="Error", message="You left a field empty. Please go back and fill it out.")
        return
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="You do not currently have any saved passwords.")
        return
    
    try:
        messagebox.showinfo(title="Password info", message=f"Website: {web_entry.get()} \nPassword: {data[web_entry.get()]['password']}")
    except KeyError:
        messagebox.showerror(title="Error", message="No details for the website exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)
    
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    if len(web_entry.get()) == 0 or len(email_user_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="Error", message="You left a field empty. Please go back and fill it out.")
    else:
        new_entry = {web_entry.get(): {"email": email_user_entry.get(), "password": password_entry.get()}}
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_entry)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_entry, file, indent=4)
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            web_entry.delete(0,'end')
            password_entry.delete(0,'end')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1, row=0)

#Labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries

web_entry = Entry(width=30)
web_entry.focus()
web_entry.grid(column=1, row=1,)

email_user_entry = Entry(width=49)
email_user_entry.insert(0, "yesman@yes.com")
email_user_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

#Buttons

search_button = Button(text="Search", command=find_password, width=15)
search_button.grid(column=2, row=1)

generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()