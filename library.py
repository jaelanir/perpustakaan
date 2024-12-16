from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, year, copies):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies
        self.borrowed_by = {}  # Dictionary untuk menyimpan peminjam beserta waktu peminjaman

    def borrow(self, borrower):
        if self.copies > 0:
            self.copies -= 1
            self.borrowed_by[borrower] = datetime.now()
            return True
        return False

    def return_book(self, borrower):
        if borrower in self.borrowed_by:
            self.copies += 1
            del self.borrowed_by[borrower]
            return True
        return False


class Library:
    def __init__(self):
        self.books = []  # List untuk menyimpan semua buku

    def add_book(self, title, author, year, copies):
        """Tambahkan buku baru ke perpustakaan."""
        self.books.append(Book(title, author, year, copies))

    def find_book(self, title):
        """Cari buku berdasarkan judul."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def pinjam_buku(self, title, borrower):
        """Pinjam buku untuk seorang peminjam."""
        book = self.find_book(title)
        if book and book.borrow(borrower):
            return True
        return False

    def kembalikan_buku(self, title, borrower):
        """Kembalikan buku dari seorang peminjam."""
        book = self.find_book(title)
        if book:
            return book.return_book(borrower)
        return False

    def calculate_overdue_days(self, title, borrower):
        """Hitung jumlah hari keterlambatan."""
        book = self.find_book(title)
        if book and borrower in book.borrowed_by:
            borrowed_time = book.borrowed_by[borrower]
            overdue_days = (datetime.now() - borrowed_time).days - 7  # 7 hari waktu pinjam normal
            return max(overdue_days, 0)  # Tidak ada denda jika nilai negatif
        return 0

    def calculate_denda(self, overdue_days):
        """Hitung denda berdasarkan jumlah hari keterlambatan."""
        return overdue_days * 2000  # Denda Rp2000 per hari keterlambatan
    
    def get_borrowed_books(self):
        """Mengembalikan buku yang sedang dipinjam beserta peminjamnya."""
        borrowed_books = {}
        for book in self.books:
            for borrower, borrowed_time in book.borrowed_by.items():
                borrowed_books[book.title] = borrower
        return borrowed_books
