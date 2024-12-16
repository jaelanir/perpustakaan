import tkinter as tk
from tkinter import messagebox
from library import Library  # Import library

# Inisialisasi perpustakaan
library = Library()
library.add_book("Python", "Ridwan", 2023, 5)
library.add_book("Programmer", "David Thomas", 1999, 3)
library.add_book("Algoritma", "Thomas", 2009, 4)
library.add_book("Kecerdasan Buatan", "Peter Norvig", 2010, 2)
library.add_book("Pola Desain", "Gamma", 1994, 6)

# Fungsi GUI
def tambah_buku_gui():
    def submit():
        title = title_entry.get().strip()
        author = author_entry.get().strip()
        year = year_entry.get().strip()
        try:
            copies = int(copies_entry.get().strip())
            library.add_book(title, author, year, copies)
            messagebox.showinfo("Sukses", f"Buku '{title}' berhasil ditambahkan!")
            tambah_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Jumlah salinan harus berupa angka valid.")

    tambah_window = tk.Toplevel(root)
    tambah_window.title("Tambah Buku Baru")
    tambah_window.geometry("400x300")
    tambah_window.configure(bg="#f0f8ff")
    
    frame = tk.Frame(tambah_window, bg="#f0f8ff", padx=20, pady=20)
    frame.pack(expand=True, fill="both")
    
    tk.Label(frame, text="Judul Buku:", font=("Helvetica", 12), bg="#f0f8ff").grid(row=0, column=0, sticky="w", pady=5)
    title_entry = tk.Entry(frame, font=("Helvetica", 12), width=30)
    title_entry.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Penulis:", font=("Helvetica", 12), bg="#f0f8ff").grid(row=1, column=0, sticky="w", pady=5)
    author_entry = tk.Entry(frame, font=("Helvetica", 12), width=30)
    author_entry.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="Tahun Terbit:", font=("Helvetica", 12), bg="#f0f8ff").grid(row=2, column=0, sticky="w", pady=5)
    year_entry = tk.Entry(frame, font=("Helvetica", 12), width=30)
    year_entry.grid(row=2, column=1, pady=5)

    tk.Label(frame, text="Jumlah Salinan:", font=("Helvetica", 12), bg="#f0f8ff").grid(row=3, column=0, sticky="w", pady=5)
    copies_entry = tk.Entry(frame, font=("Helvetica", 12), width=30)
    copies_entry.grid(row=3, column=1, pady=5)

    tk.Button(
        frame, text="Tambah", command=submit, font=("Helvetica", 12), bg="#00796b", fg="white", width=15
    ).grid(row=4, column=0, columnspan=2, pady=20)

def tampilkan_buku_gui():
    books = library.books
    if not books:
        messagebox.showinfo("Informasi", "Tidak ada buku yang tersedia.")
        return

    tampilkan_window = tk.Toplevel(root)
    tampilkan_window.title("Daftar Buku")
    tampilkan_window.geometry("400x300")
    tampilkan_window.configure(bg="#f0f8ff")

    frame = tk.Frame(tampilkan_window, bg="#f0f8ff", padx=20, pady=20)
    frame.pack(expand=True, fill="both")

    tk.Label(frame, text="Daftar Buku yang Tersedia:", font=("Helvetica", 14), bg="#f0f8ff").pack(pady=10)
    
    for i, book in enumerate(books, start=1):
        book_info = f"{i}. {book.title} oleh {book.author} ({book.year}) - {book.copies} salinan tersedia"
        tk.Label(frame, text=book_info, font=("Helvetica", 12), anchor="w", bg="#f0f8ff", pady=5).pack(fill="x")

def pinjam_buku_gui():
    def submit():
        title = title_entry.get().strip()
        name = name_entry.get().strip()

        if not title or not name:
            messagebox.showerror("Error", "Judul buku dan nama peminjam tidak boleh kosong.")
            return

        if library.pinjam_buku(title, name):
            messagebox.showinfo("Sukses", f"Buku '{title}' berhasil dipinjam oleh {name}!")
        else:
            messagebox.showerror("Error", f"Buku '{title}' tidak tersedia untuk dipinjam.")
        
        pinjam_window.destroy()

    pinjam_window = tk.Toplevel(root)
    pinjam_window.title("Pinjam Buku")
    pinjam_window.geometry("400x250")
    pinjam_window.configure(bg="#f0f8ff")
    
    frame = tk.Frame(pinjam_window, bg="#f0f8ff", padx=20, pady=20)
    frame.pack(expand=True, fill="both")
    
    tk.Label(frame, text="Judul Buku:", font=("Helvetica", 12), bg="#f0f8ff").grid(row=0, column=0, sticky="w", pady=5)
    title_entry = tk.Entry(frame, font=("Helvetica", 12), width=30)
    title_entry.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Nama Peminjam:", font=("Helvetica", 12), bg="#f0f8ff").grid(row=1, column=0, sticky="w", pady=5)
    name_entry = tk.Entry(frame, font=("Helvetica", 12), width=30)
    name_entry.grid(row=1, column=1, pady=5)

    tk.Button(
        frame, text="Pinjam", command=submit, font=("Helvetica", 12), bg="#00796b", fg="white", width=15
    ).grid(row=2, column=0, columnspan=2, pady=20)

def kembalikan_buku_gui():
    def submit():
        title = title_entry.get().strip()
        borrower = borrower_entry.get().strip()
        
        if not title or not borrower:
            messagebox.showerror("Error", "Judul buku dan nama peminjam tidak boleh kosong.")
            return
        
        if library.kembalikan_buku(title, borrower):
            overdue_days = library.calculate_overdue_days(title, borrower)
            if overdue_days > 0:
                denda = library.calculate_denda(overdue_days)
                messagebox.showinfo(
                    "Sukses",
                    f"Buku '{title}' berhasil dikembalikan oleh {borrower}!\nJumlah denda keterlambatan: Rp{denda}"
                )
            else:
                messagebox.showinfo(
                    "Sukses", f"Buku '{title}' berhasil dikembalikan oleh {borrower} tanpa denda."
                )
        else:
            messagebox.showerror(
                "Error", f"Buku '{title}' tidak ditemukan atau tidak sedang dipinjam oleh {borrower}."
            )
        kembalikan_window.destroy()

    kembalikan_window = tk.Toplevel(root)
    kembalikan_window.title("Kembalikan Buku")
    kembalikan_window.geometry("400x250")
    kembalikan_window.configure(bg="#f0f8ff")
    
    frame = tk.Frame(kembalikan_window, bg="#f0f8ff", padx=20, pady=20)
    frame.pack(expand=True, fill="both")
    
    tk.Label(frame, text="Judul Buku:", font=("Helvetica", 12), bg="#f0f8ff").grid(row=0, column=0, sticky="w", pady=5)
    title_entry = tk.Entry(frame, font=("Helvetica", 12), width=30)
    title_entry.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Nama Peminjam:", font=("Helvetica", 12), bg="#f0f8ff").grid(row=1, column=0, sticky="w", pady=5)
    borrower_entry = tk.Entry(frame, font=("Helvetica", 12), width=30)
    borrower_entry.grid(row=1, column=1, pady=5)

    tk.Button(
        frame, text="Kembalikan", command=submit, font=("Helvetica", 12), bg="#d32f2f", fg="white", width=15
    ).grid(row=2, column=0, columnspan=2, pady=20)

def tampilkan_buku_dipinjam_gui():
    borrowed_books = library.get_borrowed_books()
    if not borrowed_books:
        messagebox.showinfo("Informasi", "Tidak ada buku yang sedang dipinjam.")
        return

    tampilkan_dipinjam_window = tk.Toplevel(root)
    tampilkan_dipinjam_window.title("Daftar Buku yang Dipinjam")
    tampilkan_dipinjam_window.geometry("400x300")
    tampilkan_dipinjam_window.configure(bg="#f0f8ff")

    frame = tk.Frame(tampilkan_dipinjam_window, bg="#f0f8ff", padx=20, pady=20)
    frame.pack(expand=True, fill="both")

    tk.Label(frame, text="Daftar Buku yang Dipinjam:", font=("Helvetica", 14), bg="#f0f8ff").pack(pady=10)

    for i, (title, borrower) in enumerate(borrowed_books.items(), start=1):
        book_info = f"{i}. '{title}' dipinjam oleh {borrower}"
        tk.Label(frame, text=book_info, font=("Helvetica", 12), anchor="w", bg="#f0f8ff", pady=5).pack(fill="x")

# GUI utama
root = tk.Tk()
root.title("Sistem Manajemen Perpustakaan")
root.geometry("500x500")
root.configure(bg="#f0f8ff")

frame = tk.Frame(root, bg="#f0f8ff", padx=20, pady=20)
frame.pack(expand=True, fill="both")

tk.Label(frame, text="Sistem Manajemen Perpustakaan", font=("Helvetica", 18), bg="#f0f8ff", fg="#00796b").pack(pady=10)
tk.Label(frame, text="Selamat datang di sistem perpustakaan!", font=("Helvetica", 12), bg="#f0f8ff").pack(pady=5)

tk.Button(frame, text="Tambah Buku", width=20, command=tambah_buku_gui, font=("Helvetica", 12), bg="#00796b", fg="white").pack(pady=5)
tk.Button(frame, text="Tampilkan Buku", width=20, command=tampilkan_buku_gui, font=("Helvetica", 12), bg="#00796b", fg="white").pack(pady=5)
tk.Button(frame, text="Pinjam Buku", width=20, command=pinjam_buku_gui, font=("Helvetica", 12), bg="#00796b", fg="white").pack(pady=5)
tk.Button(frame, text="Kembalikan Buku", width=20, command=kembalikan_buku_gui, font=("Helvetica", 12), bg="#00796b", fg="white").pack(pady=5)
tk.Button(frame, text="Buku yang Dipinjam", width=20, command=tampilkan_buku_dipinjam_gui, font=("Helvetica", 12), bg="#00796b", fg="white").pack(pady=5)
tk.Button(frame, text="Keluar", width=20, command=root.destroy, font=("Helvetica", 12), bg="#b71c1c", fg="white").pack(pady=20)

root.mainloop()  
