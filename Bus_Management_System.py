import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage
import os



current_bus = None  # To track the selected bus
bus_details = {
    "Bus 1": {
        "stops": [("SM Caloocan", 1), ("SM Fairview", 2), ("SM North", 3)],
        "driver": "Bentong",
    },
    #DB catch other Bus Details
}


# --- Login Window ---
def create_login_window():
    def login():
        username = username_entry.get()
        password = password_entry.get()

        # Testing account
        if username == "admin" and password == "admin":
            print("Login successful!")
            root.destroy()  
            create_bus_selection_window() 
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    root = tk.Tk()
    root.title("City Bus Management System")
    root.configure(background="white")

    img = PhotoImage(file=os.path.join(os.path.dirname(__file__), "Assets", "CBMS.png"))
    label = tk.Label(root, image=img, height=400, width=350)
    label.pack(padx=30, pady=1)

    frame = tk.Frame(root, background="white")
    frame.pack(padx=0, pady=50)

    username_label = tk.Label(frame, text="Username:", width=50, background="white", anchor='w')
    username_label.pack()

    username_entry = tk.Entry(frame, width=58)
    username_entry.pack()

    password_label = tk.Label(frame, text="Password:", width=50, background="white", anchor='w')
    password_label.pack()

    password_entry = tk.Entry(frame, width=58, show="*")
    password_entry.pack()

    login_button = tk.Button(
        frame, text="Login", command=login, bg="navyblue", 
        font=("Calibri", 10, "bold"), fg="white", padx=5, pady=5, width=10
    )
    login_button.pack(pady=20)

    root.mainloop()


# --- Bus Selection Window ---
def create_bus_selection_window():
    def on_bus_click(bus_info):
        global current_bus
        current_bus = bus_info
        create_bus_trip_interface(bus_info, app) 
        
        

    app = tk.Tk()
    app.title("City Bus Selection")
    app.geometry("650x500")
    app.configure(bg='navyblue')

    # Logo image
    img = PhotoImage(file=os.path.join(os.path.dirname(__file__), "Assets", "CITY.png"))
    logo_label = tk.Label(app, image=img, bg='navyblue', height=200, width=350)
    logo_label.image = img
    logo_label.pack(pady=10)

    # Outer container for centering
    outer_container = tk.Frame(app, bg='white')
    outer_container.pack(expand=True, padx=20, pady=20)

        # Inner container for buses
    container = tk.Frame(outer_container, bg='white')
    container.pack(expand=True, padx=40, pady=30)

        # "Select Bus Schedule" text
    select_bus_label = tk.Label(container, text="Select Bus Schedule:", font=("calibri", 12, "bold"), bg='white')
    select_bus_label.grid(row=0, column=0, columnspan=2, padx=7, pady=(5, 10), sticky='w')

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

    app.mainloop()


def create_bus_trip_interface(bus_info, master):
    # Parse information from bus_info
    bus_number, route, seats = bus_info.split('\n')

    bus_details = {
        "Bus 1": {
            "stops": [("SM Caloocan", 1), ("SM Fairview", 2), ("SM North", 3)],
            "driver": "Bentong",
        },
        "Bus 2": {
            "stops": [("SM Fairview", 1), ("SM North", 2), ("SM Megamall", 3)],
            "driver": "Lars",
        },
        "Bus 3": {
            "stops": [("SM Fairview", 1), ("SM Caloocan", 2), ("SM MOA", 3)],
            "driver": "Seth",
        },
        "Bus 4": {
            "stops": [("SM Novaliches", 1), ("SM Caloocan", 2), ("SM MOA", 3)],
            "driver": "Andeng",
        },
        "Bus 5": {
            "stops": [("SM Manila", 1), ("SM Caloocan", 2), ("SM North", 3)],
            "driver": "Sean",
        },
    }

    root = tk.Toplevel(master)
    root.title("City Bus Trip")
    root.geometry("400x500")
    root.config(bg="navyblue")

    img = PhotoImage(file=os.path.join(os.path.dirname(__file__), "Assets", "CITY.png"))
    logo_label = tk.Label(root, image=img, bg='navyblue')
    logo_label.image = img
    logo_label.pack(pady=(20, 10))

    frame = ttk.Frame(root, padding=(200, 30), relief="solid")
    frame.place(relx=0.5, rely=0.6, anchor="center")

  
    title_label = ttk.Label(frame, text=bus_number, font=("calibri", 18, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
    route_label = ttk.Label(frame, text=route, font=("calibri", 12, "bold"), justify="center")
    route_label.grid(row=1, column=0, columnspan=2, pady=(0, 5))

   
    details = bus_details.get(bus_number)
    if details:
        route_label = ttk.Label(frame, text="Mon - Fri", font=("calibri", 10), justify="center")
        route_label.grid(row=2, column=0, columnspan=2, pady=(0, 0))

        route_label = ttk.Label(frame, text="6:00am - 9:00am", font=("calibri", 11), justify="center")
        route_label.grid(row=3, column=0, columnspan=2, pady=(0, 0))

        route_label = ttk.Label(frame, text=f"Driver: {details['driver']}", font=("calibri", 10), justify="center")
        route_label.grid(row=4, column=0, columnspan=2, pady=(0, 20))

  
        for stop, row in details['stops']:
            stop_label = ttk.Label(frame, text=f"{row}", font=("calibri", 10, "bold"))
            stop_label.grid(row=row + 4, column=0, padx=(0, 10))
            stop_name_label = ttk.Label(frame, text=stop, font=("calibri", 10))
            stop_name_label.grid(row=row + 4, column=1, sticky="w")

        # Back button
        back_button = tk.Button(frame, text="BACK", bg="navyblue", fg="white", padx=20, command=root.destroy)
        back_button.grid(row=len(details['stops']) + 5, column=0, pady=(30, 0), padx=4)

        # Next button
        next_button = tk.Button(frame, text="NEXT", bg="navyblue", fg="white", padx=20, command=lambda: [root.destroy(), create_ticket_booking_window(master)]) 
        next_button.grid(row=len(details['stops']) + 5, column=1, pady=(30, 0), padx=4)
    else:
        error_label = ttk.Label(frame, text="Invalid Bus Number!", font=("calibri", 12, "bold"))
        error_label.grid(row=2, column=0, columnspan=2, pady=(10, 0))

    root.mainloop()

def create_ticket_booking_window(app):
    def on_next_button_click():
        name = name_entry.get()
        contact = contact_entry.get()
        amount = amount_entry.get()

        if not name or not contact or not amount:
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            # Will add the process for booking information 
            # (save to a database and calculate fares)
            root.destroy()
            #(B.TICKET SUCCESS)
            create_ticket_success_window(name, contact, amount)

            # destroy window after process
            

    root = tk.Toplevel(app)
    root.title("City Bus Book Ticket")
    root.geometry("400x500")
    root.configure(bg="navyblue")
    root.attributes('-topmost', 1)  

    img = PhotoImage(file=os.path.join(os.path.dirname(__file__), "Assets", "CITY.png"))
    logo_label = tk.Label(root, image=img, bg='navyblue')
    logo_label.image = img
    logo_label.pack(pady=(20, 10))

    # Frame for the form
    form_frame = tk.Frame(root, bg="white", padx=60, pady=50)
    form_frame.pack(pady=(0, 20)) 

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
    next_button = tk.Button(form_frame, text="NEXT", bg="navyblue", fg="white", padx=30, command=on_next_button_click)
    next_button.grid(row=7, column=0, columnspan=2, pady=20)

    


    # Run the application
    root.mainloop()

def create_ticket_success_window(name, contact, amount):

    # This function displays the success message on button click
    def show_message():
        messagebox.showinfo("Booking Information", details_text) # Reference the details_text defined outside

    root = tk.Tk()
    root.title("Booking Confirmation")
    root.configure(bg="navyblue")

    # Main frame
    main_frame = tk.Frame(root, bg="navyblue")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Title label
    title_label = tk.Label(main_frame, text="Book Successfully!", bg="navyblue", fg="white", font=("calibri", 18, "bold"))
    title_label.pack(pady=50)

    # Booking details frame
    details_frame = tk.Frame(main_frame, bg="white")
    details_frame.pack(ipady=50, ipadx=80, expand=True)

    # Booking details labels
    bus_info = current_bus
    if bus_info:
        bus_number, route, _ = bus_info.split('\n')
        driver = bus_details.get(bus_number, {}).get('driver', 'Unknown')
        details_text = (
            f"Name: {name}\n"
            f"Contact: {contact}\n\n"
            f"{bus_number}\n"
            f"Trip: {route}\n"
            f"Driver: {driver}\n\n"
            f"Amount: {amount}"
        )
    else:
        details_text = (
            f"Name: {name}\n"
            f"Contact: {contact}\n\n"
            f"Amount: {amount}"
        )
        
    details_label = tk.Label(details_frame, text=details_text, bg="white", font=("calibri", 12))
    details_label.pack(pady=10)

    # OK button (call show_message function when clicked)
    ok_button = tk.Button(details_frame, text="OK", command=lambda: [show_message(), root.destroy()], font=("calibri", 12), bg="navyblue", fg="white", width=10)
    ok_button.pack(pady=10)

    # Show the details when the window is created
    show_message()

    root.mainloop()


# --- Program Start ---
if __name__ == "__main__":
    create_login_window()  # Start with the login window