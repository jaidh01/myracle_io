import tkinter as tk
from tkinter import filedialog, ttk
import os
import google.generativeai as genai
from dotenv import load_dotenv
from myracle_io import *

class ScreenshotTestingTool:
    def __init__(self, master):
        self.master = master
        master.title("Screenshot Testing Tool")
        master.geometry("400x300")

        # Optional Context
        ttk.Label(master, text="Optional Context").pack(pady=5)
        self.context_entry = tk.Text(master, height=5)
        self.context_entry.pack(padx=10, pady=5, fill=tk.X)

        # Upload Screenshots
        ttk.Label(master, text="Upload Screenshots").pack(pady=5)
        self.file_frame = ttk.Frame(master)
        self.file_frame.pack(fill=tk.X, padx=10)
        
        self.file_entry = ttk.Entry(self.file_frame)
        self.file_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        self.choose_button = ttk.Button(self.file_frame, text="Choose Files", command=self.choose_files)
        self.choose_button.pack(side=tk.RIGHT)

        # Describe Testing Instructions Button
        self.describe_button = ttk.Button(master, text="Describe Testing Instructions", command=self.describe_instructions)
        self.describe_button.pack(pady=20)

    def choose_files(self):
        files = filedialog.askopenfilenames(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if files:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, ", ".join(files))

    def describe_instructions(self):
        
        try:
            print("Generating instructions...")
            generatecontent(self.context_entry.get("1.0", tk.END).strip(), self.file_entry.get())
            #print("Files:", self.file_entry.get())
            #print("Context:", self.context_entry.get("1.0", tk.END).strip())
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    root = tk.Tk()
    app = ScreenshotTestingTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()