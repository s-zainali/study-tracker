from tkinter import *
import app
import threading
import time

root = Tk()
root.title("Study Tracker")

# Set the initial size of the window to maintain a 16:9 ratio
width = 500
height = int(width * 9 / 16)
root.geometry(f"{width}x{height}")
root.configure(bg="#302c34")

# Create frames
label_frame = Frame(root, bg="#302c34")
button_frame = Frame(root, bg="#302c34")

label_frame.pack(fill=BOTH, expand=True)
button_frame.pack(fill=BOTH, expand=True)

# Create labels
study_text_label = Label(label_frame, text="Study Time:", bg="#302c34", fg="white")
study_text_label.grid(row=0, column=0, padx=5, pady=5)
study_label = Label(label_frame, text="", bg="#302c34", fg="white")
study_label.grid(row=0, column=1, padx=5, pady=5)

break_text_label = Label(label_frame, text="Break Time:", bg="#302c34", fg="white")
break_text_label.grid(row=1, column=0, padx=5, pady=5)
break_label = Label(label_frame, text="", bg="#302c34", fg="white")
break_label.grid(row=1, column=1, padx=5, pady=5)

# Center the labels
for widget in label_frame.winfo_children():
    widget.grid_configure(sticky="ew")

def update_label():
    study_label.config(text=round(app.STUDY, 0))
    break_label.config(text=round(app.BREAK, 0))
    root.after(1000, update_label)  # Update every second

def start_study_session():
    app.FLAG_BREAK = True
    study_thread = threading.Thread(target=app.start_study, args=(7,))
    study_thread.start()

def start_break_session():
    app.FLAG_STUDY = True
    break_thread = threading.Thread(target=app.start_break)
    break_thread.start()

def chill():
    app.FLAG_BREAK = True
    app.FLAG_STUDY = True

# Create buttons
button1 = Button(button_frame, text="Study Mode", command=start_study_session, bg="#61bc9a", fg="white", bd=0)
button2 = Button(button_frame, text="Break Mode", command=start_break_session, bg="#ff6480", fg="white", bd=0)
button3 = Button(button_frame, text="Chill Mode", command=chill, bg="#f6bc4f", fg="white", bd=0)

button1.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
button2.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
button3.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

# Make buttons equally sized and spaced
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)

update_label()  # Initial call to start the update loop
root.mainloop()
