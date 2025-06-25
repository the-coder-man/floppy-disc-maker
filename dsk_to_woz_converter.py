import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Dummy converter function (replace this with actual DSK to WOZ conversion logic)
def convert_dsk_to_woz(dsk_path):
    try:
        with open(dsk_path, 'rb') as dsk_file:
            data = dsk_file.read()
        # Simulate conversion by writing the same content (placeholder)
        woz_path = dsk_path.replace('.dsk', '.woz')
        with open(woz_path, 'wb') as woz_file:
            woz_file.write(data)  # Replace with actual WOZ content
        return woz_path
    except Exception as e:
        messagebox.showerror("Conversion Error", str(e))
        return None

class DSKtoWOZConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DSK to WOZ Converter")
        self.file_path = ""
        self.woz_path = ""

        self.upload_button = tk.Button(root, text="Upload .DSK File", command=self.upload_file)
        self.upload_button.pack(pady=10)

        self.convert_button = tk.Button(root, text="Convert to .WOZ", command=self.convert_file, state=tk.DISABLED)
        self.convert_button.pack(pady=10)

        self.download_button = tk.Button(root, text="Download .WOZ File", command=self.download_file, state=tk.DISABLED)
        self.download_button.pack(pady=10)

    def upload_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("DSK files", "*.dsk")])
        if self.file_path:
            self.convert_button.config(state=tk.NORMAL)
            messagebox.showinfo("File Selected", f"Selected file: {self.file_path}")

    def convert_file(self):
        if self.file_path:
            self.woz_path = convert_dsk_to_woz(self.file_path)
            if self.woz_path:
                messagebox.showinfo("Conversion Complete", f"Converted to: {self.woz_path}")
                self.download_button.config(state=tk.NORMAL)

    def download_file(self):
        if self.woz_path:
            dest_path = filedialog.asksaveasfilename(defaultextension=".woz",
                                                     filetypes=[("WOZ files", "*.woz")])
            if dest_path:
                try:
                    with open(self.woz_path, 'rb') as src:
                        data = src.read()
                    with open(dest_path, 'wb') as dest:
                        dest.write(data)
                    messagebox.showinfo("Download Complete", f"File saved to: {dest_path}")
                except Exception as e:
                    messagebox.showerror("Download Error", str(e))

if __name__ == '__main__':
    root = tk.Tk()
    app = DSKtoWOZConverterApp(root)
    root.mainloop()
