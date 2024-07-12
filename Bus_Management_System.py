import tkinter as tk
import sqlite3 
from tkinter import ttk, messagebox
from tkinter import PhotoImage
import os
import datetime



current_bus = None  # To track the selected bus

bookings = [] #catcher of booking details

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
        
    def on_view_bookings_click():
        app.withdraw()  # Hide the bus selection window
        create_view_bookings_window(app)
        
    app = tk.Tk()
    app.title("City Bus Selection")
    app.geometry("650x500")
    app.configure(bg='navyblue')

    # Button configuration
    button_config = {
        'font': ("calibri", 12, "bold"),
        'fg': "white",
        'bg': 'navyblue',
        'width': 25,
        'height': 3
    }
    view_bookings_button_config = {
        'font': ("calibri", 12, "bold"),
        'fg': "navyblue",    
        'bg': 'white',       
        'width': 25,
        'height': 3,
        'highlightthickness': 2,
        'highlightbackground': "navyblue" 
    }

    # Logo image
    img = PhotoImage(file=os.path.join(os.path.dirname(__file__), "Assets", "CITY.png"))
    logo_label = tk.Label(app, image=img, bg='navyblue', height=200, width=350)
    logo_label.image = img
    logo_label.pack(pady=10)

    # Main Frame (holds all content except the logo)
    main_frame = tk.Frame(app, bg='navyblue')
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Outer container for centering
    outer_container = tk.Frame(main_frame, bg='white')
    outer_container.pack(expand=True, padx=20, pady=20)

        # Inner container for buses
    container = tk.Frame(outer_container, bg='white')
    container.pack(expand=True, padx=40, pady=30)

        # "Select Bus Schedule" text
    select_bus_label = tk.Label(container, text="Select Bus Schedule:", font=("calibri", 12, "bold"), bg='white')
    select_bus_label.grid(row=0, column=0, columnspan=2, padx=7, pady=(5, 10), sticky='w')

    bus_details = fetch_bus_details()
    

    for i, (bus_id, info) in enumerate(bus_details.items()):
        button_text = f"{bus_id}\n{info['route']}\n{info['capacity']} seats"

        bus_button = tk.Button(container, text=button_text, 
                               command=lambda bus=bus_id: on_bus_click(bus), **button_config)
        bus_button.grid(row=i // 2 + 1, column=i % 2, padx=10, pady=10)
    

    view_bookings_button = tk.Button(outer_container, text="View Bookings", command=on_view_bookings_click, **view_bookings_button_config)
    view_bookings_button.pack(side=tk.RIGHT, padx=(0, 15), pady=(0, 20))


    app.mainloop()

def fetch_bus_details():
    bus_details = {}
    try:
        conn = sqlite3.connect('BMS.db')  
        cursor = conn.cursor()

        # Fetch data from the v_BusSelection view with the new column names
        cursor.execute("SELECT Bus_ID, StartPoint, EndPoint, Capacity FROM v_BusSelection")
        rows = cursor.fetchall()

        for row in rows:
            bus_id, start_point, end_point, capacity = row

            # Create route information by combining start and end points
            route = f"{start_point} - {end_point}"

            # Use bus_id as the key in bus_details
            bus_details[bus_id] = {"route": route, "capacity": capacity}

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

    return bus_details


def create_bus_trip_interface(bus_info, master):
    bus_id = bus_info
    # Fetch trip details from the database
    trip_details, stops = fetch_bus_trip_details(bus_id)

    # Create a top-level window associated with the main window (master)
    root = tk.Toplevel(master)
    root.title("City Bus Trip")
    root.geometry("400x500")
    root.config(bg="navyblue")

    # Logo Image
    img = PhotoImage(file=os.path.join(os.path.dirname(__file__), "Assets", "CITY.png"))  
    logo_label = tk.Label(root, image=img, bg='navyblue')
    logo_label.image = img  # Keep a reference to avoid garbage collection
    logo_label.pack(pady=(20, 10))  

    frame = ttk.Frame(root, padding=(200, 30), relief="solid")
    frame.place(relx=0.5, rely=0.6, anchor="center")

    # Display trip details if available
    if trip_details:
        _, trip_id, start_point, end_point, shift, driver, departure_time = trip_details #Skip the first column (Bus_ID)
        route = f"{start_point} - {end_point}"
        time = f"{departure_time} ({shift})"

        title_label = ttk.Label(frame, text=f"Bus {bus_id}", font=("calibri", 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        route_label = ttk.Label(frame, text=route, font=("calibri", 12, "bold"), justify="center")
        route_label.grid(row=1, column=0, columnspan=2, pady=(0, 5))

        # Trip details labels
        route_label = ttk.Label(frame, text=time, font=("calibri", 11), justify="center")
        route_label.grid(row=2, column=0, columnspan=2, pady=(0, 0))

        route_label = ttk.Label(frame, text=f"Driver: {driver}", font=("calibri", 10), justify="center")
        route_label.grid(row=3, column=0, columnspan=2, pady=(0, 20))

        # Display stops
        stops_label = tk.Label(frame, text="Stops:", font=("calibri", 12, "bold"))
        stops_label.grid(row=5, column=0, columnspan=2, pady=(10, 5))

        for i, stop in enumerate(stops):
            stop_label = ttk.Label(frame, text=f"{i+1}. {stop}", font=("calibri", 10))
            stop_label.grid(row=i + 6, column=0, columnspan=2, sticky="w")

        back_button = tk.Button(frame, text="BACK", bg="navyblue", fg="white", padx=20, command=root.destroy)
        back_button.grid(row=len(stops) + 7, column=0, pady=(30, 0), padx=4)

        next_button = tk.Button(frame, text="NEXT", bg="navyblue", fg="white", padx=20, command=lambda: [root.destroy(), create_ticket_booking_window(master, bus_info)])  # Pass bus_info here
        next_button.grid(row=len(stops) + 7, column=1, pady=(30, 0), padx=4)

    else:
        error_label = ttk.Label(frame, text="Trip details not found!", font=("calibri", 12, "bold"))
        error_label.grid(row=2, column=0, columnspan=2, pady=(10, 0))

    root.mainloop()

def fetch_bus_trip_details(bus_id):
    trip_details = None
    stops = []  # List to hold the stops
    try:
        conn = sqlite3.connect('BMS.db')
        cursor = conn.cursor()

        # Fetch trip details
        cursor.execute(
            "SELECT Bus_ID, Trip_ID, StartPoint, EndPoint, Shift, Name, DepartureTime " 
            "FROM v_BusTripInformation WHERE Bus_ID = ?",
            (bus_id,)
        )
        trip_details = cursor.fetchone()

        # Fetch the stops for the trip (if trip_details were found)
        if trip_details:
            bus_id = trip_details[1]  # Get the Trip_ID (now at index 1)
            cursor.execute(
                "SELECT Name FROM v_BusTripInformationStopList WHERE Trip_ID = ?",
                (bus_id,)
            )
            stops = [stop[0] for stop in cursor.fetchall()]

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

    return trip_details, stops

def create_ticket_booking_window(app, bus_id):  # Accept bus_id
    def on_next_button_click():
        name = name_entry.get()
        contact = contact_entry.get()
        amount = amount_entry.get()

        

        if not name or not contact or not amount:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Save booking data to the database (t_Ticket and t_Passenger)
        try:
            conn = sqlite3.connect('BMS.db')
            cursor = conn.cursor()

            # Get the Trip_ID from v_BusTripInformation based on the selected bus_id
            cursor.execute("SELECT Trip_ID FROM v_BusTripInformation WHERE Bus_ID = ?", (bus_id,))
            trip_id = cursor.fetchone()

            if trip_id:
                trip_id = trip_id[0]  # Extract Trip_ID from the result
                current_date = datetime.date.today().strftime('%Y-%m-%d') # Get current date in YYYY-MM-DD

                # Insert ticket into t_Ticket
                cursor.execute("INSERT INTO t_Ticket (Trip_ID, Price, ScheduledDate, DatePurchased) VALUES (?, ?, ?, ?)",
                               (trip_id, amount, current_date, current_date))  # Use today as both scheduled and purchased date
                ticket_id = cursor.lastrowid  # Get the inserted Ticket_ID

                # Insert passenger into t_Passenger
                cursor.execute("INSERT INTO t_Passenger (Ticket_ID, Name, ContactInfo) VALUES (?, ?, ?)",
                               (ticket_id, name, contact))

                conn.commit()
                root.destroy()  # Close the ticket booking window
                create_ticket_success_window(name, contact, amount, bus_id)
            else:
                messagebox.showerror("Error", "Bus trip information not found.")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")
        finally:
            if conn:
                conn.close()
            

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

    trip_price = fetch_trip_price(bus_id)
    if trip_price:
        amount_entry.insert(0, str(trip_price))
    else:
        messagebox.showerror("Error", "Trip price not found.")
    # ...

    root.mainloop()

def fetch_trip_price(bus_id):
    try:
        conn = sqlite3.connect('BMS.db')
        cursor = conn.cursor()

        cursor.execute("SELECT Fare FROM v_BusTripInformation WHERE Bus_ID = ?", (bus_id,))
        trip_price = cursor.fetchone()

        if trip_price:
            return trip_price[0]  # Extract price from the tuple
        else:
            return None

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        if conn:
            conn.close()

   
        
    

def create_ticket_success_window(name, contact, amount, bus_id):
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

    
    conn = sqlite3.connect('BMS.db')
    cursor = conn.cursor()

            # Get the Trip_ID from v_BusTripInformation based on the selected bus_id
    cursor.execute("SELECT * FROM v_BusTripInformation WHERE Bus_ID = ?", (current_bus,))
    bus_info = cursor.fetchone()
    bus_number = str(bus_info[0])
    route = str(f"{bus_info[2]} - {bus_info[3]}")
    driver = str(bus_info[5])
    

    # Booking details labels

    if bus_info:

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

def on_listbox_select(event):
    widget = event.widget
    selection = widget.curselection()
    if selection:
        index = selection[0]
        value = widget.get(index)
        details_label.config(text=value)

def create_view_bookings_window(master):
    global details_label  # Declare details_label as global

    view_bookings_window = tk.Toplevel(master)
    view_bookings_window.title("View Bookings")
    view_bookings_window.config(bg="navyblue")

    # Logo Image
    img = PhotoImage(file=os.path.join(os.path.dirname(__file__), "Assets", "CITY.png"))  
    logo_label = tk.Label(view_bookings_window, image=img, bg='navyblue')
    logo_label.image = img  # Keep a reference to avoid garbage collection
    logo_label.pack(pady=(20, 10))  

    # Main Frame (holds all content except the logo)
    main_frame = tk.Frame(view_bookings_window, bg="navyblue")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Booking Details Frame
    details_frame = tk.Frame(main_frame, bg="white", bd=2, relief=tk.SOLID)
    details_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)  

    # Details Label (inside the details_frame)
    details_label = tk.Label(details_frame, text="", bg="white", font=("Calibri", 12)) #Empty at the start
    details_label.pack(pady=10)
    
    # Listbox to display bookings
    listbox = tk.Listbox(details_frame, width=50)
    for booking in bookings:
        listbox.insert(tk.END, booking)  
    listbox.pack(pady=10, fill=tk.BOTH, expand=True) 
    listbox.bind("<<ListboxSelect>>", on_listbox_select)

    # Button Frame
    button_frame = tk.Frame(main_frame, bg="navyblue")  # Pack button frame in main_frame
    button_frame.pack(pady=10)

    # Edit Button
    edit_button = tk.Button(button_frame, text="Edit", bg="white", fg="navyblue", font=("Calibri", 12, "bold"), command=on_edit)
    edit_button.pack(side=tk.LEFT, padx=5)

    # Delete Button
    delete_button = tk.Button(button_frame, text="Delete", bg="white", fg="navyblue", font=("Calibri", 12, "bold"), command=on_delete)
    delete_button.pack(side=tk.LEFT, padx=5)

    # Update Button (initially disabled)
    update_button = tk.Button(button_frame, text="Update", bg="white", fg="navyblue", font=("Calibri", 12, "bold"), state=tk.DISABLED, command=on_update)
    update_button.pack(side=tk.LEFT, padx=5)

    # Back button to close the view bookings window and show the main window again
    back_button = tk.Button(button_frame, text="Back", command=lambda: [view_bookings_window.destroy(), master.deiconify()])
    back_button.pack(side=tk.LEFT, padx=5) 


# Functions for button actions (replace with your actual logic)
def on_edit():
    update_button.config(state=tk.NORMAL)  # Enable the Update button

def on_delete():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        booking = bookings[index]
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete this booking:\n{booking}?"):
            listbox.delete(index)
            del bookings[index]
            messagebox.showinfo("Success", "Booking deleted successfully.")

def on_update():
    update_button.config(state=tk.DISABLED)



# --- Program Start ---
if __name__ == "__main__":
    create_login_window()  # Start with the login window