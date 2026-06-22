import sqlite3

def get_all_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author FROM books")
    books = cursor.fetchall()
    conn.close()
    return books


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_connection():
    conn = sqlite3.connect("books.db")
    #conn.row_factory = sqlite3.Row
    return conn

def insert_book(title, author):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))  
        conn.commit()
        conn.close()


def delete_books(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def editing_book(id, title, author):
    conn = get_connection()
    cursor = conn.cursor()
    #book = cursor.fetchone()
    cursor.execute("UPDATE books SET title = ?, author = ? WHERE id = ?", (title, author, id))
    conn.commit()
    conn.close()


def get_book_id(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM books WHERE id = ?",
        (id,)
    )
    book = cursor.fetchone()
    conn.close()
    return book