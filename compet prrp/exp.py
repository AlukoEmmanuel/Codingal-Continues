import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My First GUI App")

# Add a label widget
label = tk.Label(window, text="Hello, Python GUI!")
label.pack(padx=20, pady=20)

# Add a button to close the window
button = tk.Button(
    window,
    text="Close",
    command=window.destroy  # Closes the window when clicked
)
button.pack(pady=10)

# Start the GUI event loop
window.mainloop()