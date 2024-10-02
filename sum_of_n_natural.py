# # num=int(input("enter the number"))
# # sum=0
# # for i in range(num):
# #     sum+=i
# # print("sum=",sum)
#
# #
# def tail(file, n=1, bs=1024):
#     f = open(file)
#     f.seek(0,2)
#     l = 1-f.read(1).count('\n')
#     B = f.tell()
#     while n >= l and B > 0:
#             block = min(bs, B)
#             B -= block
#             f.seek(B, 0)
#             l += f.read(block).count('\n')
#     f.seek(B, 0)
#     l = min(l,n)
#     lines = f.readlines()[-l:]
#     f.close()
#     return lines
# lines = tail("Untitled.txt", 2)
# for line in lines:
# 	print(line)
#
# # f=open("Untitled.txt","r")
# # print(f.read())
# #
# # f=open("Untitled.txt","a+")
# # f.write("world!")
# #
# # print(f.read())
# # f.close()



# import tkinter as tk
#
# # Create the main window
# root = tk.Tk()
# root.title("Widget Example")
#
# # Create a label widget with the specified options
# label = tk.Label(root, text="Hello, World!", bg="red", font=("Times", 18))
#
# # Display the label
# label.pack(pady=20, padx=20)
#
# # Run the application
# root.mainloop()

#
# import tkinter as tk
#
# def show_message():
#     label_var.set("You clicked the button!")
#
# def toggle_check():
#     label_var.set(f"Checkbutton is {'checked' if check_var.get() else 'unchecked'}")
#
# def select_radio():
#     label_var.set(f"Selected option: {radio_var.get()}")
#
# def scale_changed(val):
#     label_var.set(f"Scale value: {val}")
#
# # Create the main window
# root = tk.Tk()
# root.title("Widget Experiment")
# root.geometry("400x400")
#
# # Message widget
# message = tk.Message(root, text="This is a Message widget", width=300, bg="lightblue", font=("Arial", 12))
# message.pack(pady=10)
#
# # Button widget
# button = tk.Button(root, text="Click Me", command=show_message, bg="lightgreen", font=("Arial", 10))
# button.pack(pady=5)
#
# # Entry widget
# entry = tk.Entry(root, width=30, font=("Arial", 10))
# entry.pack(pady=5)
# entry.insert(0, "Type here")
#
# # Checkbutton widget
# check_var = tk.BooleanVar()
# checkbutton = tk.Checkbutton(root, text="Check me", variable=check_var, command=toggle_check, font=("Arial", 10))
# checkbutton.pack(pady=5)
#
# # Radiobutton widget
# radio_var = tk.StringVar(value="Option 1")
# radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1", command=select_radio, font=("Arial", 10))
# radiobutton1.pack(anchor=tk.W)
# radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2", command=select_radio, font=("Arial", 10))
# radiobutton2.pack(anchor=tk.W)
#
# # Scale widget
# scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=scale_changed, font=("Arial", 10))
# scale.pack(pady=5)
#
# # Label to display messages from button, checkbutton, radiobutton, and scale
# label_var = tk.StringVar()
# label = tk.Label(root, textvariable=label_var, font=("Arial", 12))
# label.pack(pady=20)
#
# # Start the main event loop
# root.mainloop()




import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('database_app.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')
conn.commit()

def add_record():
    name = input("Enter name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")

    try:
        cursor.execute("INSERT INTO records (name, age, email) VALUES (?, ?, ?)", (name, age, email))
        conn.commit()
        print("Record added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Email must be unique.")

def view_records():
    cursor.execute("SELECT * FROM records")
    records = cursor.fetchall()

    if records:
        for record in records:
            print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Email: {record[3]}")
    else:
        print("No records found.")

def update_record():
    record_id = input("Enter the ID of the record to modify: ")
    name = input("Enter new name: ")
    age = input("Enter new age: ")
    email = input("Enter new email: ")

    try:
        cursor.execute("UPDATE records SET name = ?, age = ?, email = ? WHERE id = ?", (name, age, email, record_id))
        if cursor.rowcount > 0:
            conn.commit()
            print("Record updated successfully.")
        else:
            print("No record found with that ID.")
    except sqlite3.IntegrityError:
        print("Error: Email must be unique.")

def delete_record():
    record_id = input("Enter the ID of the record to delete: ")

    cursor.execute("DELETE FROM records WHERE id = ?", (record_id,))
    if cursor.rowcount > 0:
        conn.commit()
        print("Record deleted successfully.")
    else:
        print("No record found with that ID.")

def main_menu():
    print("\nDatabase Application")
    while True:

        print("1. Add Record")
        print("2. View Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_record()
        elif choice == '2':
            view_records()
        elif choice == '3':
            update_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please select from 1-5.")

if __name__ == "__main__":
    main_menu()

# Close the database connection when the program exits
conn.close()
