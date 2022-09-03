from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Create the database file in /database/new-books-collection.db
FILE_URI = 'sqlite:///new-books-collection.db'

# Create the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = FILE_URI  # load the configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Significant overhead if True. Future default: False
db = SQLAlchemy(app)  # create the SQLAlchemy object by passing it the application


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float(), unique=False, nullable=False)

    # def __repr__(self):
    #     # This will allow each book object to be identified by its title when printed.
    #     return f'<Book: {self.title}>'


# Create the database file and tables
# This code must come _after_ the class definition
if not os.path.isfile(FILE_URI):
    db.create_all()

# Create a book and store it in the database file
book = Books(title='Harry Potter2', author='J. K. Rowling', rating='9.3')
# print(book.__repr__())
db.session.add(book)
db.session.commit()
