import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

def file_to_dsk(input_path, output_path=None):
    if not input_path.lower().endswith(('.rom', '.py', '.txt')):
        raise ValueError("Input file must be a .ROM, .PY, or .TXT file")

    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"File not found: {input_path}")

    with open(input_path, 'rb') as input_file:
        file_data = input_file.read()

    max_dsk_size = 143360
    if len(file_data) > max_dsk_size:
        raise ValueError("File is too large to fit on a standard Apple II disk image")

    padded_data = file_data + b'\x00' * (max_dsk_size - len(file_data))

    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + '.dsk'

    with open(output_path, 'wb') as dsk_file:
        dsk_file.write(padded_data)

    return output_path

def open_file(filepath):
    try:
        if sys.platform == "win32":
            os.startfile(filepath)
        elif sys.platform == "darwin":
            subprocess.call(['open', filepath])
        else:
            subprocess.call(['xdg-open', filepath])
    except Exception as e:
        messagebox.showerror("Error", f"Cannot open file: {str(e)}")

def upload_file():
    filepath = filedialog.askopenfilename(filetypes=[("Supported files", "*.rom *.py *.txt")])
    if filepath:
        try:
            output = file_to_dsk(filepath)
            messagebox.showinfo("Success", f"Converted to: {output}")
            download_btn.config(command=lambda fp=output: open_file(fp))
            download_btn.pack(pady=10)
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == '__main__':
    root = tk.Tk()
    root.title("ROM/PY/TXT to DSK Converter")
    root.geometry("300x150")

    upload_btn = tk.Button(root, text="Upload .ROM, .PY, or .TXT File", command=upload_file)
    upload_btn.pack(pady=10)

    download_btn = tk.Button(root, text="Open Converted .DSK File")

    root.mainloop()

