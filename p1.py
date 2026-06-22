from flask import Flask, render_template, request, url_for, redirect
from database import get_connection, init_db, insert_book, delete_books, editing_book,get_all_books, get_book_id


app = Flask(__name__) 
   
init_db()

# it does not need to be specified that the method is GET because it is the default method
@app.route('/')
def home():
    books= get_all_books()
    return render_template("index.html", books=books)

@app.route('/edit/<int:id>', methods =['GET', 'POST'])
def edit_book(id):
    book = get_book_id(id)
    # next line verifies if the user is trying to edit a book that does not exist, if so it redirects to the home page
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        editing_book(id, title, author)
        return redirect(url_for('home'))
    return render_template("edit.html", book=book)  #this runs only in a GET request


@app.route('/books', methods=['GET', 'POST'])
def books():
    title = None
    author = None
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        insert_book(title, author)
        return redirect(url_for('home'))
    return render_template("books.html",title=title,author=author)


@app.route('/delete/<int:id>', methods=['POST'])
def delete_book(id):
    delete_books(id)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
  
