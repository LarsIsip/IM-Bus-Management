B.LOG-IN

from tkinter import *

ANCHOR = W  # Or any other anchor constant (N, S, E, etc.)

def login():
  # Get the username and password from the entry fields
  username = username_entry.get()
  password = password_entry.get()

  print("Login successful!")

root = Tk()
root.title("City Bus Management System")

# For main window to bg-white
root.configure(background="white")

img = PhotoImage(file='C:/Users/ASUS/Downloads/CITY.png')

label = Label(root, image=img, height=400, width=350)
label.pack(padx=30, pady=1)

# For Creating a frame to hold the label and entry fields
frame = Frame(root, background="white")
frame.pack(padx=0, pady=50)

# For Creating a label for the username
username_label = Label(frame, text="Username:", width=50, background="white", anchor='w')
username_label.pack()

# Creating an entry field for the username
username_entry = Entry(frame, width=58)
username_entry.pack()

# Label for the password
password_label = Label(frame, text="Password:", width=50, background="white", anchor='w')
password_label.pack()

# For entry field for the password (set show="*" for password masking)
password_entry = Entry(frame, width=58, show="*")  # Password masking added
password_entry.pack()

# For button to login
login_button = Button(frame, text="Login", command=login, bg="navyblue", font=("Calibri", 10, "bold"), fg="white", padx=5, pady=5, width=10)
login_button.pack(pady=20)

root.mainloop()


B.SELECTION OF BUS

import tkinter as tk
from tkinter import PhotoImage

class CityBusManagementSystem(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("City Bus Selection")
        self.geometry("650x500")  # Adjusted to fit all elements comfortably.
        self.configure(bg='navyblue')

        # Logo image
        img = PhotoImage(file='C:/Users/ASUS/Downloads/CBMS.1.png')
        logo_label = tk.Label(self, image=img, bg='navyblue', height=200, width=350)
        logo_label.image = img  # To keep a reference to avoid garbage collection
        logo_label.pack(pady=10)

        # Outer container for centering
        outer_container = tk.Frame(self, bg='white')
        outer_container.pack(expand=True, padx=20, pady=20)

        # Inner container for buses
        container = tk.Frame(outer_container, bg='white')
        container.pack(expand=True, padx=40, pady=30)

        # "Select Bus Schedule" text
        select_bus_label = tk.Label(container, text="Select Bus Schedule:", font=("calibri", 12, "bold"), bg='white')
        select_bus_label.grid(row=0, column=0, columnspan=2, padx=7, pady=(5, 10), sticky='w')

        # Click event handler
        def on_bus_click(bus_info):
            print(f"You clicked on {bus_info}")

        # Button configuration
        button_config = {
            'font': ("calibri", 12, "bold"),
            'fg': "white",
            'bg': 'navyblue',
            'width': 25,
            'height': 3
        }

        # Bus 1
        bus1_button = tk.Button(container, text="Bus 1\nSM Caloocan - SM North\n30 seats", command=lambda: on_bus_click("Bus 1\nSM Caloocan - SM North\n30 seats"), **button_config)
        bus1_button.grid(row=1, column=0, padx=10, pady=10)

        # Bus 2
        bus2_button = tk.Button(container, text="Bus 2\nSM Fairview - SM Megamall\n50 seats", command=lambda: on_bus_click("Bus 2\nSM Fairview - SM Megamall\n50 seats"), **button_config)
        bus2_button.grid(row=1, column=1, padx=10, pady=10)

        # Bus 3
        bus3_button = tk.Button(container, text="Bus 3\nSM Fairview - SM MOA\n40 seats", command=lambda: on_bus_click("Bus 3\nSM Fairview - SM MOA\n40 seats"), **button_config)
        bus3_button.grid(row=2, column=0, padx=10, pady=10)

        # Bus 4
        bus4_button = tk.Button(container, text="Bus 4\nSM Novaliches - SM MOA\n60 seats", command=lambda: on_bus_click("Bus 4\nSM Novaliches - SM MOA\n60 seats"), **button_config)
        bus4_button.grid(row=2, column=1, padx=10, pady=10)

        # Bus 5
        bus5_button = tk.Button(container, text="Bus 5\nSM Manila - SM North\n45 seats", command=lambda: on_bus_click("Bus 5\nSM Manila - SM North\n45 seats"), **button_config)
        bus5_button.grid(row=3, column=0, columnspan=2, padx=15, pady=15)  # Centering the button

if __name__ == "__main__":
    app = CityBusManagementSystem()
    app.mainloop()


B1. TRIP

import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

def create_bus_trip_interface():
    root = tk.Tk()
    root.title("City Bus Trip")
    root.geometry("400x500")  # Adjusted to accommodate the logo
    root.config(bg="navyblue")

    # Logo image
    img = PhotoImage(file='C:/Users/ASUS/Downloads/CBMS.1.png')
    logo_label = tk.Label(root, image=img, bg='navyblue', height=200, width=350)
    logo_label.image = img  # To Keep a reference to avoid garbage collection
    logo_label.pack(pady=10)

    # Frame for the bus trip details.
    frame = ttk.Frame(root, padding=(200, 30), relief="solid")
    frame.place(relx=0.5, rely=0.6, anchor="center")  # Adjusted to fit below the logo

    # For the Title
    title_label = ttk.Label(frame, text="Bus 1", font=("calibri", 18, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    # For Route details labels
    route_label = ttk.Label(frame, text="SM Caloocan - SM North", font=("calibri", 12, "bold"), justify="center")
    route_label.grid(row=1, column=0, columnspan=2, pady=(0, 5))

    route_label = ttk.Label(frame, text="Mon - Fri", font=("calibri", 10), justify="center")
    route_label.grid(row=2, column=0, columnspan=2, pady=(0, 0))

    route_label = ttk.Label(frame, text="6:00am - 9:00am", font=("calibri", 11), justify="center")
    route_label.grid(row=3, column=0, columnspan=2, pady=(0, 0))

    route_label = ttk.Label(frame, text="Driver: Bentong", font=("calibri", 10), justify="center")
    route_label.grid(row=4, column=0, columnspan=2, pady=(0, 20))

    # For Stops
    stops = [("SM Caloocan", 1), ("SM Fairview", 2), ("SM North", 3)]
    for stop, row in stops:
        stop_label = ttk.Label(frame, text=f"{row}", font=("calibri", 10, "bold"))
        stop_label.grid(row=row+4, column=0, padx=(0, 10))
        stop_name_label = ttk.Label(frame, text=stop, font=("calibri", 10))
        stop_name_label.grid(row=row+4, column=1, sticky="w")

    # Back button
    back_button = tk.Button(frame, text="BACK", bg="navyblue", fg="white", padx=20, command=root.destroy)
    back_button.grid(row=len(stops) + 5, column=0, pady=(30, 0))

    # Next button
    next_button = tk.Button(frame, text="NEXT", bg="navyblue", fg="white", padx=20)
    next_button.grid(row=len(stops) + 5, column=1, pady=(30, 0))

    root.mainloop()

if __name__ == "__main__":
    create_bus_trip_interface()


B2.TRIP

import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

def create_bus_trip_interface():
    root = tk.Tk()
    root.title("City Bus Trip")
    root.geometry("400x500")  # Adjusted to accommodate the logo
    root.config(bg="navyblue")

    # Logo image
    img = PhotoImage(file='C:/Users/ASUS/Downloads/CBMS.1.png')
    logo_label = tk.Label(root, image=img, bg='navyblue', height=200, width=350)
    logo_label.image = img  # To Keep a reference to avoid garbage collection
    logo_label.pack(pady=10)

    # Frame for the bus trip details.
    frame = ttk.Frame(root, padding=(200, 30), relief="solid")
    frame.place(relx=0.5, rely=0.6, anchor="center")  # Adjusted to fit below the logo

    # For the Title
    title_label = ttk.Label(frame, text="Bus 2", font=("calibri", 18, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    # For Route details labels
    route_label = ttk.Label(frame, text="SM Fairview - SM Megamall", font=("calibri", 12, "bold"), justify="center")
    route_label.grid(row=1, column=0, columnspan=2, pady=(0, 5))

    route_label = ttk.Label(frame, text="Mon - Fri", font=("calibri", 10), justify="center")
    route_label.grid(row=2, column=0, columnspan=2, pady=(0, 0))

    route_label = ttk.Label(frame, text="6:00am - 9:00am", font=("calibri", 11), justify="center")
    route_label.grid(row=3, column=0, columnspan=2, pady=(0, 0))

    route_label = ttk.Label(frame, text="Driver: Lars", font=("calibri", 10), justify="center")
    route_label.grid(row=4, column=0, columnspan=2, pady=(0, 20))

    # For Stops
    stops = [("Sm Fairview", 1), ("SM Fairview", 2), ("SM Megamall", 3)]
    for stop, row in stops:
        stop_label = ttk.Label(frame, text=f"{row}", font=("calibri", 10, "bold"))
        stop_label.grid(row=row+4, column=0, padx=(0, 10))
        stop_name_label = ttk.Label(frame, text=stop, font=("calibri", 10))
        stop_name_label.grid(row=row+4, column=1, sticky="w")

    # Back button
    back_button = tk.Button(frame, text="BACK", bg="navyblue", fg="white", padx=20, command=root.destroy)
    back_button.grid(row=len(stops) + 5, column=0, pady=(30, 0))

    # Next button
    next_button = tk.Button(frame, text="NEXT", bg="navyblue", fg="white", padx=20)
    next_button.grid(row=len(stops) + 5, column=1, pady=(30, 0))

    root.mainloop()

if __name__ == "__main__":
    create_bus_trip_interface()


B3.TRIP

import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

def create_bus_trip_interface():
    root = tk.Tk()
    root.title("City Bus Trip")
    root.geometry("400x500")  # Adjusted to accommodate the logo
    root.config(bg="navyblue")

    # Logo image
    img = PhotoImage(file='C:/Users/ASUS/Downloads/CBMS.1.png')
    logo_label = tk.Label(root, image=img, bg='navyblue', height=200, width=350)
    logo_label.image = img  # To Keep a reference to avoid garbage collection
    logo_label.pack(pady=10)

    # Frame for the bus trip details.
    frame = ttk.Frame(root, padding=(200, 30), relief="solid")
    frame.place(relx=0.5, rely=0.6, anchor="center")  # Adjusted to fit below the logo

    # For the Title
    title_label = ttk.Label(frame, text="Bus 3", font=("calibri", 18, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    # For Route details labels
    route_label = ttk.Label(frame, text="SM Fairview - SM Moa", font=("calibri", 12, "bold"), justify="center")
    route_label.grid(row=1, column=0, columnspan=2, pady=(0, 5))

    route_label = ttk.Label(frame, text="Mon - Fri", font=("calibri", 10), justify="center")
    route_label.grid(row=2, column=0, columnspan=2, pady=(0, 0))

    route_label = ttk.Label(frame, text="6:00am - 9:00am", font=("calibri", 11), justify="center")
    route_label.grid(row=3, column=0, columnspan=2, pady=(0, 0))

    route_label = ttk.Label(frame, text="Driver: Seth", font=("calibri", 10), justify="center")
    route_label.grid(row=4, column=0, columnspan=2, pady=(0, 20))

    # For Stops
    stops = [("Sm Fairview", 1), ("SM Caloocan", 2), ("SM Moa", 3)]
    for stop, row in stops:
        stop_label = ttk.Label(frame, text=f"{row}", font=("calibri", 10, "bold"))
        stop_label.grid(row=row+4, column=0, padx=(0, 10))
        stop_name_label = ttk.Label(frame, text=stop, font=("calibri", 10))
        stop_name_label.grid(row=row+4, column=1, sticky="w")

    # Back button
    back_button = tk.Button(frame, text="BACK", bg="navyblue", fg="white", padx=20, command=root.destroy)
    back_button.grid(row=len(stops) + 5, column=0, pady=(30, 0), padx=4)

    # Next button
    next_button = tk.Button(frame, text="NEXT", bg="navyblue", fg="white", padx=20)
    next_button.grid(row=len(stops) + 5, column=1, pady=(30, 0), padx=4)

    root.mainloop()

if __name__ == "__main__":
    create_bus_trip_interface()


B4.TRIP

import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

def create_bus_trip_interface():
    root = tk.Tk()
    root.title("City Bus Trip")
    root.geometry("400x500")  # Adjusted to accommodate the logo
    root.config(bg="navyblue")

    # Logo image
    img = PhotoImage(file='C:/Users/ASUS/Downloads/CBMS.1.png')
    logo_label = tk.Label(root, image=img, bg='navyblue', height=200, width=350)
    logo_label.image = img  # To Keep a reference to avoid garbage collection
    logo_label.pack(pady=10)

    # Frame for the bus trip details.
    frame = ttk.Frame(root, padding=(200, 30), relief="solid")
    frame.place(relx=0.5, rely=0.6, anchor="center")  # Adjusted to fit below the logo

    # For the Title
    title_label = ttk.Label(frame, text="Bus 4", font=("calibri", 18, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    # For Route details labels
    route_label = ttk.Label(frame, text="SM Novaliches - SM Moa", font=("calibri", 12, "bold"), justify="center")
    route_label.grid(row=1, column=0, columnspan=2, pady=(0, 5))

    route_label = ttk.Label(frame, text="Mon - Fri", font=("calibri", 10), justify="center")
    route_label.grid(row=2, column=0, columnspan=2, pady=(0, 0))

    route_label = ttk.Label(frame, text="6:00am - 9:00am", font=("calibri", 11), justify="center")
    route_label.grid(row=3, column=0, columnspan=2, pady=(0, 0))

    route_label = ttk.Label(frame, text="Driver: Andeng", font=("calibri", 10), justify="center")
    route_label.grid(row=4, column=0, columnspan=2, pady=(0, 20))

    # For Stops
    stops = [("Sm Novaliches", 1), ("SM Caloocan", 2), ("SM Moa", 3)]
    for stop, row in stops:
        stop_label = ttk.Label(frame, text=f"{row}", font=("calibri", 10, "bold"))
        stop_label.grid(row=row+4, column=0, padx=(0, 10))
        stop_name_label = ttk.Label(frame, text=stop, font=("calibri", 10))
        stop_name_label.grid(row=row+4, column=1, sticky="w")

    # Back button
    back_button = tk.Button(frame, text="BACK", bg="navyblue", fg="white", padx=20, command=root.destroy)
    back_button.grid(row=len(stops) + 5, column=0, pady=(30, 0))

    # Next button
    next_button = tk.Button(frame, text="NEXT", bg="navyblue", fg="white", padx=20)
    next_button.grid(row=len(stops) + 5, column=1, pady=(30, 0))

    root.mainloop()

if __name__ == "__main__":
    create_bus_trip_interface()


B5.TRIP

import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

def create_bus_trip_interface():
    root = tk.Tk()
    root.title("City Bus Trip")
    root.geometry("400x500")  # Adjusted to accommodate the logo
    root.config(bg="navyblue")

    # Logo image
    img = PhotoImage(file='C:/Users/ASUS/Downloads/CBMS.1.png')
    logo_label = tk.Label(root, image=img, bg='navyblue', height=200, width=350)
    logo_label.image = img  # To Keep a reference to avoid garbage collection
    logo_label.pack(pady=10)

    # Frame for the bus trip details.
    frame = ttk.Frame(root, padding=(200, 30), relief="solid")
    frame.place(relx=0.5, rely=0.6, anchor="center")  # Adjusted to fit below the logo

    # For the Title
    title_label = ttk.Label(frame, text="Bus 5", font=("calibri", 18, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    # For Route details labels
    route_label = ttk.Label(frame, text="SM Manila - SM North", font=("calibri", 12, "bold"), justify="center")
    route_label.grid(row=1, column=0, columnspan=2, pady=(0, 5))

    route_label = ttk.Label(frame, text="Mon - Fri", font=("calibri", 10), justify="center")
    route_label.grid(row=2, column=0, columnspan=2, pady=(0, 0))

    route_label = ttk.Label(frame, text="6:00am - 9:00am", font=("calibri", 11), justify="center")
    route_label.grid(row=3, column=0, columnspan=2, pady=(0, 0))

    route_label = ttk.Label(frame, text="Driver: Sean", font=("calibri", 10), justify="center")
    route_label.grid(row=4, column=0, columnspan=2, pady=(0, 20))

    # For Stops
    stops = [("Sm Manila", 1), ("SM Caloocan", 2), ("SM North", 3)]
    for stop, row in stops:
        stop_label = ttk.Label(frame, text=f"{row}", font=("calibri", 10, "bold"))
        stop_label.grid(row=row+4, column=0, padx=(0, 10))
        stop_name_label = ttk.Label(frame, text=stop, font=("calibri", 10))
        stop_name_label.grid(row=row+4, column=1, sticky="w")

    # Back button
    back_button = tk.Button(frame, text="BACK", bg="navyblue", fg="white", padx=20, command=root.destroy)
    back_button.grid(row=len(stops) + 5, column=0, pady=(30, 0), padx=4)

    # Next button
    next_button = tk.Button(frame, text="NEXT", bg="navyblue", fg="white", padx=20)
    next_button.grid(row=len(stops) + 5, column=1, pady=(30, 0), padx=4)

    root.mainloop()

if __name__ == "__main__":
    create_bus_trip_interface()


B.TICKET

import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("City Bus Book Ticket")
root.geometry("400x500")  # Adjusted to fit the image and forms
root.configure(bg="navyblue")

# For image/logo
image = tk.PhotoImage(file="C:/Users/ASUS/Downloads/CBMS.1.png")

# Label for the image and place it above the form
image_label = tk.Label(root, image=image, bg="navyblue")
image_label.pack(pady=(20, 10))  # Adjust padding as needed

# Frame for the form
form_frame = tk.Frame(root, bg="white", padx=60, pady=50)
form_frame.pack(pady=(0, 20))  # Adjust padding as needed

# Instruction label
instruction_label = tk.Label(form_frame, text="Please fill out the form:", bg="white", font=("calibri", 12, "bold"))
instruction_label.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky=tk.W)

# Place for the labels and entry widgets
name_label = tk.Label(form_frame, text="Name", bg="white")
name_label.grid(row=1, column=0, columnspan=2, pady=(0, 5), sticky=tk.W)

name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=2, column=0, columnspan=2, pady=5)

contact_label = tk.Label(form_frame, text="Contact Number", bg="white")
contact_label.grid(row=3, column=0, columnspan=2, pady=(10, 5), sticky=tk.W)

contact_entry = tk.Entry(form_frame, width=30)
contact_entry.grid(row=4, column=0, columnspan=2, pady=5)

amount_label = tk.Label(form_frame, text="Amount", bg="white")
amount_label.grid(row=5, column=0, columnspan=2, pady=(10, 5), sticky=tk.W)

amount_entry = tk.Entry(form_frame, width=30)
amount_entry.grid(row=6, column=0, columnspan=2, pady=5)

# For placing the Next button
next_button = tk.Button(form_frame, text="NEXT", bg="navyblue", fg="white", padx=30)
next_button.grid(row=7, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()


B.TICKET SUCCESS

import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Booking Information", "Name: Juan\nContact: 0123456789\nBUS 1\nTrip: SM Caloocan - SM North\n6:00 am - 9:00 am\nDriver: Bentong\nAmount: 50")

root = tk.Tk()
root.title("Booking Confirmation")

# Setting the background color of the root window
root.configure(bg="navyblue")

# For main frame
main_frame = tk.Frame(root, bg="navyblue")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# For Add title label
title_label = tk.Label(main_frame, text="Book Successfully!", bg="navyblue", fg="white", font=("calibri", 18, "bold"))
title_label.pack(pady=50)

# Booking details frame
details_frame = tk.Frame(main_frame, bg="white")
details_frame.pack(ipady=50, ipadx=80, expand=True)

# For Add booking details labels
details_text = (
    "Name: Juan\n"
    "Contact: 0123456789\n\n"
    "BUS 1\n"
    "Trip: SM Caloocan - SM North\n"
    "6:00 am - 9:00 am\n"
    "Driver: Bentong\n\n"
    "Amount: 50"
)
details_label = tk.Label(details_frame, text=details_text, bg="white", font=("calibri", 12))
details_label.pack(pady=10)

# For OK button
ok_button = tk.Button(details_frame, text="OK", command=show_message, font=("calibri", 12), bg="navyblue", fg="white", width=10)
ok_button.pack(pady=10)

root.mainloop()





