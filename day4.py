import tkinter as tk
from tkinter import messagebox

# Function to handle login
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Placeholder for actual authentication logic
    if username == "user" and password == "pass":
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")

# Create the main window
root = tk.Tk()
root.title("Twinker")

# Create and place the username label and entry
label_username = tk.Label(root, text="Username")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Create and place the password label and entry
label_password = tk.Label(root, text="Password")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Create and place the login button
button_login = tk.Button(root, text="Login", command=login)
button_login.pack(pady=20)

# Run the main loop
root.mainloop()
