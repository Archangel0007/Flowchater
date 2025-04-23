import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import subprocess
import os

def run_pipeline():
    text_input = text_box.get("1.0", tk.END).strip()
    if not text_input:
        messagebox.showwarning("Input Required", "Please enter some text first.")
        return
    with open("Input.txt", "w") as f:
        f.write(text_input)

    try:
        subprocess.run(["python3", "Reasoning_Api_gemini.py"], check=True)
        subprocess.run(["python3", "graphviz_flowcharter.py"], check=True)

        img = Image.open("flowchart_output.cairo.cairo.png")
        img = img.resize((600, 600))  
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk

        messagebox.showinfo("Success", "Flowchart generated and displayed!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
root = tk.Tk()
root.title("Flowchart Generator")

tk.Label(root, text="Enter Description Below:").pack(pady=5)

text_box = tk.Text(root, height=10, width=80)
text_box.pack()

tk.Button(root, text="Generate Flowchart", command=run_pipeline).pack(pady=10)

image_label = tk.Label(root)
image_label.pack()

root.mainloop()
