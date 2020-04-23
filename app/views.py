from flask import render_template, request, redirect, url_for

from app import app
from .forms import BookForm, AuthorForm, LanguageForm, GenreForm
from .models import Book, Author, Genre, Language, db
from .logger import Logger

logger = Logger()


@app.route('/')
def index():
    return render_template('navigation.html', title = 'Main')


@app.route('/books/')
def books():
    books = db.session.query(Book).all()
    logger.log_in_file("GET /books/ HTTP/1.1 200")
    return render_template('books.html', title = 'Books', books=books)


@app.route('/books/add/', methods=['get', 'post'])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        book = update_book(form)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('books'))
    return render_template('add_edit.html', title='Add book', form=form)


@app.route("/books/edit/<int:book_id>/", methods=['get', 'post'])
def edit_book(book_id):
    book = db.session.query(Book).filter(Book.id == book_id).one()
    form = BookForm()
    if form.validate_on_submit():
        update_book(form, book)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('books'))
    else:
        form.title.data = book.title
        form.author.data = book.author
        form.genre.data = book.genre
        form.lang.data = book.lang
        form.summary.data = book.summary
        return render_template('add_edit.html', title='Edit book', form=form)


@app.route('/books/<int:book_id>/delete/', methods=['get', 'post'])
def delete_book(book_id):
    book = db.session.query(Book).filter(Book.id == book_id).one()
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('books'))
    else:
        return render_template('delete.html', title='Delete book', instance=book)


@app.route('/authors/')
def show_authors():
    authors = db.session.query(Author).all()
    logger.log_in_file("GET /authors/ HTTP/1.1 200")
    return render_template('authors.html', title='Authors',  authors=authors)


@app.route('/authors/add/', methods=['get', 'post'])
def add_author():
    form = AuthorForm()
    if form.validate_on_submit():
        author = update_author(form)
        db.session.add(author)
        db.session.commit()
        return redirect(url_for('show_authors'))
    return render_template('add_edit.html', title='Add author', form=form)


@app.route('/authors/edit/<int:author_id>/', methods=['get', 'post'])
def edit_author(author_id):
    author = db.session.query(Author).filter(Author.id == author_id).one()
    form = AuthorForm()
    if form.validate_on_submit():
        update_author(form, author)
        db.session.add(author)
        db.session.commit()
        return redirect(url_for('show_authors'))
    else:
        form.name.data = author.name
        form.date_of_birth.data = author.date_of_birth
        form.date_of_death.data = author.date_of_death
        return render_template('add_edit.html', title='Edit author', form=form)


@app.route('/authors/delete/<int:author_id>/', methods=['get', 'post'])
def delete_author(author_id):
    author = db.session.query(Author).filter(Author.id == author_id).one()
    if request.method == 'POST':
        db.session.delete(author)
        db.session.commit()
        return redirect(url_for('show_authors'))
    else:
        return render_template('delete.html', title='Delete author', instance=author)


@app.route('/languages/')
def show_languages():
    languages = db.session.query(Language).all()
    logger.log_in_file("GET /languages/ HTTP/1.1 200")
    return render_template('languages.html', title = 'Languages', languages=languages)


@app.route('/languages/add', methods=['get', 'post'])
def add_language():
    form = LanguageForm()
    if form.validate_on_submit():
        lang = update_lang(form)
        db.session.add(lang)
        db.session.commit()
        return redirect(url_for('show_languages'))
    return render_template('add_edit.html', title='Add language', form=form)


@app.route('/languages/edit/<int:lang_id>/', methods=['get', 'post'])
def edit_language(lang_id):
    lang = db.session.query(Language).filter(Language.id == lang_id).one()
    form = LanguageForm()
    if form.validate_on_submit():
        update_lang(form, lang)
        db.session.add(lang)
        db.session.commit()
        return redirect(url_for('show_languages'))
    else:
        form.lang.data = lang.lang
        return render_template('add_edit.html', title='Edit language', form=form)


@app.route('/languages/delete/<int:lang_id>/', methods=['get', 'post'])
def delete_language(lang_id):
    lang = db.session.query(Language).filter(Language.id == lang_id).one()
    if request.method == 'POST':
        db.session.delete(lang)
        db.session.commit()
        return redirect(url_for('show_languages'))
    else:
        return render_template('delete.html', title='Delete language', instance=lang)


@app.route('/genres/')
def show_genres():
    genres = db.session.query(Genre).all()
    logger.log_in_file("GET /genres/ HTTP/1.1 200")
    return render_template('genres.html', title='Genres',  genres=genres)

@app.route('/genres/add', methods=['get', 'post'])
def add_genre():
    form = GenreForm()
    if form.validate_on_submit():
        genre = update_genre(form)
        db.session.add(genre)
        db.session.commit()
        return redirect(url_for('show_genres'))
    return render_template('add_edit.html', title='Add genre', form=form)


@app.route('/genres/edit/<int:genre_id>/', methods=['get', 'post'])
def edit_genre(genre_id):
    genre = db.session.query(Genre).filter(Genre.id == genre_id).one()
    form = GenreForm()
    if form.validate_on_submit():
        update_publisher(form, genre)
        db.session.add(lang)
        db.session.commit()
        return redirect(url_for('show_languages'))
    else:
        form.genre.data = genre.genre
        return render_template('add_edit.html', title='Edit genre', form=form)


@app.route('/genres/delete/<int:genre_id>/', methods=['get', 'post'])
def delete_genre(genre_id):
    genre = db.session.query(Genre).filter(Genre.id == genre_id).one()
    if request.method == 'POST':
        db.session.delete(genre)
        db.session.commit()
        return redirect(url_for('show_genres'))
    else:
        return render_template('delete.html', title='Delete genre', instance=genre)


def update_book(form, book=None):
    title = form.title.data
    author_name = form.author.data
    genre_name = form.genre.data if form.genre.data != '' else None
    lang_name = form.lang.data if form.lang.data != '' else None
    summary = form.summary.data if form.summary.data != '' else None

    if book is None:
        book = Book()

    book.title = title
    book.summary = summary

    query_res = db.session.query(Author).filter(Author.name == author_name).first()
    if query_res is None:
        author = Author(name=author_name)
    else:
        author = query_res
    book.author = author

    if genre_name is not None:
        query_res = db.session.query(Genre).filter(Genre.genre == genre_name).first()
        if query_res is None:
            genre = Genre(genre=genre_name)
        else:
            genre = query_res
        book.genre = genre

    if lang_name is not None:
        query_res = db.session.query(Language).filter(Language.lang == lang_name).first()
        if query_res is None:
            lang = Language(lang=lang_name)
        else:
            lang = query_res
        book.lang = lang

    return book


def update_author(form, author=None):
    name = form.name.data
    dom = form.date_of_birth.data if form.date_of_birth.data != '' else None
    dod = form.date_of_death.data if form.date_of_death.data != '' else None

    if author is None:
        author = Author()

    author.name = name
    author.date_of_birth = dom
    author.date_of_death = dod

    return author


def update_lang(form, lang=None):
    name = form.lang.data

    if lang is None:
        lang = Language()

    lang.lang = name

    return lang

def update_genre(form, genre=None):
    name = form.genre.data

    if genre is None:
        genre = Genre()

    genre.genre = name

    return genre