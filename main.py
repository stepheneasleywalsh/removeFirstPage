import os
import sys
import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox


def removeFirstPage(folder_path, output_folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            pdf_file = PyPDF2.PdfReader(file_path)
            # remove the first page
            pages = list(pdf_file.pages)
            pages.pop(0)
            # save the output file
            output_file = PyPDF2.PdfWriter()
            for page in pages:
                output_file.add_page(page)
            output_file_path = os.path.join(output_folder_path, filename)
            with open(output_file_path, "wb") as f:
                output_file.write(f)


def browse_source_folder():
    source_folder_path = filedialog.askdirectory()
    source_entry.delete(0, tk.END)  # Clear any previous entry
    source_entry.insert(0, source_folder_path)


def browse_destination_folder():
    destination_folder_path = filedialog.askdirectory()
    destination_entry.delete(0, tk.END)  # Clear any previous entry
    destination_entry.insert(0, destination_folder_path)


def process_folders():
    source_folder = source_entry.get()
    destination_folder = destination_entry.get()
    if not source_folder == destination_folder:
        messagebox.showinfo("Folders Processed",
                        f"Source Folder: {source_folder}\nDestination Folder: {destination_folder}\n\nJob Done !!!\n\n")
        removeFirstPage(source_folder, destination_folder)
    else:
        messagebox.showinfo("Folders NOT Processed","SOURCE folder and DESTINATION folder must be different!")


# Create main window
root = tk.Tk()
root.title("Folder Selection")

# Source Folder Selection
source_label = tk.Label(root, text="Source Folder:")
source_label.grid(row=0, column=0, padx=10, pady=5)
source_entry = tk.Entry(root, width=50)
source_entry.grid(row=0, column=1, padx=10, pady=5)
source_button = tk.Button(root, text="Browse", command=browse_source_folder)
source_button.grid(row=0, column=2, padx=10, pady=5)

# Destination Folder Selection
destination_label = tk.Label(root, text="Destination Folder:")
destination_label.grid(row=1, column=0, padx=10, pady=5)
destination_entry = tk.Entry(root, width=50)
destination_entry.grid(row=1, column=1, padx=10, pady=5)
destination_button = tk.Button(root, text="Browse", command=browse_destination_folder)
destination_button.grid(row=1, column=2, padx=10, pady=5)

# Button to process folders
process_button = tk.Button(root, text="Process Folders", command=process_folders)
process_button.grid(row=2, column=1, padx=10, pady=10)


def main():
    root.mainloop()


if __name__ == "__main__":
    main()


sys.exit()