from flask import Flask, render_template, request, url_for, redirect
import sqlite3


app = Flask(__name__) 

# create database and table
def init_db():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT NOT NULL,
                   author TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
# initialize the database
init_db()


@app.route('/')
def home():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author FROM books")
    books = cursor.fetchall()
    conn.close()

    return render_template("index.html", books=books)


@app.route('/books', methods=['GET', 'POST'])
def books():
    title = None
    author = None
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        conn = sqlite3.connect("books.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))  
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template("books.html",title=title,author=author)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_book(id):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    #return "Book deleted!"
    return redirect(url_for('home'))


@app.route('/edit/<int:id>', methods =['GET', 'POST'])
def edit_book(id):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("SELECT title, author FROM books WHERE id = ?", (id,))
    book = cursor.fetchone()
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        cursor.execute("UPDATE books SET title = ?, author = ? WHERE id = ?", (title, author, id))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    conn.close()
    return render_template("edit.html", book=book, id=id)
    

if __name__ == "__main__":
    app.run(debug=True)
  

