from flask import Flask, flash, render_template, request, url_for, redirect, abort
from database import (init_db, 
                      insert_book, 
                      delete_books, 
                      editing_book,get_all_books, get_book_id)


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
    if book is None:
        abort(404)  # if the book does not exist, return a 404 error
    
    # next line verifies if the user is trying to edit a book that does not exist, if so it redirects to the home page
    if request.method == 'POST':
        title = request.form['title'].strip()
        author = request.form['author'].strip()
        
        if not title or not author:
            return render_template("edit.html", book=book, error="Title and Author cannot be empty.")
        
        editing_book(id, title, author)  #this calls the database manager
        #flash('Book updated successfully!')
        return redirect(url_for('home'))
    return render_template("edit.html", book=book)  #this runs only in a GET request


@app.route('/books', methods=['GET', 'POST'])
def books():
    title = None
    author = None
    if request.method == 'POST':
        title = request.form['title'].strip()
        author = request.form['author'].strip()
        if not title or not author:
            return render_template("books.html",title=title,author=author, error="Title and Author cannot be empty.")
   
        insert_book(title, author)
        return redirect(url_for('home'))
    return render_template("books.html",title=title,author=author)

# the only allowed method is POST because we do not want to delete
#  a book by just clicking a link, we want
#  to make sure that the user is aware of the action they are taking
@app.route('/delete/<int:id>', methods=['POST'])
def delete_book(id):
    delete_books(id)
    return redirect(url_for('home'))

if __name__ == "__main__":
    #app.run(debug=True)
    #for ducker the next line is used
    app.run(host="0.0.0.0", port=5000, debug=True)
    # for runing the app in production, use a WSGI server like Gunicorn or uWSGI instead of the built-in Flask server.  
    #app.run()
