import tkinter as tk
from tkinter import scrolledtext, font
import subprocess

def launch_program():
    # Launch the main.py program using subprocess
    subprocess.run(["python", "main.py"])

# Create the main window
window = tk.Tk()

# Set the window title
window.title("AVOID")

# Set the window dimensions
window.geometry("800x500")

# Create a title label
title_label = tk.Label(window, text="AVOID – AI Vision-based Online Cheating Interception and Detection", font=("Helvetica", 20, "bold"))
title_label.pack(pady=20)

# Create a frame to hold the window contents
frame = tk.Frame(window)
frame.pack(fill=tk.BOTH, expand=True)

# Add the project image
image = tk.PhotoImage(file="bg.png")
image_label = tk.Label(frame, image=image)
image_label.grid(row=0, column=0, padx=20, pady=20)


# Load the project description from a text file
with open("proj_desc.txt", "r") as file:
    project_description = file.read()

# Configure the font style
font_style = font.Font(family="Helvetica", size=14)

# Add the project description box with scrollbars if needed
description_box = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=18.5, font=font_style)
description_box.insert(tk.INSERT, project_description)
description_box.grid(row=0, column=1, padx=20, pady=20)

# Add the launch button with custom styling
launch_button = tk.Button(frame, text="LAUNCH", command=launch_program, bg="blue", fg="white", font=("Helvetica", 14, "bold"), padx=10, pady=5)
launch_button.grid(row=1, column=0, columnspan=2, pady=10)

# Center the contents within the frame
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Start the GUI event loop
window.mainloop()
