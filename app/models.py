from app import db

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    lang_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
    summary = db.Column(db.String(255))

    def __repr__(self):
        return self.title


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    date_of_birth = db.Column(db.String(255))
    date_of_death = db.Column(db.String(255))
    books = db.relationship('Book', backref='author')

    def __repr__(self):
        return self.name


class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(255), nullable=False)
    books = db.relationship('Book', backref='genre')

    def __repr__(self):
        return self.genre


class Language(db.Model):
    __tablename__ = 'languages'

    id = db.Column(db.Integer, primary_key=True)
    lang = db.Column(db.String(255), nullable=False)
    books = db.relationship('Book', backref='lang')

    def __repr__(self):
        return self.lang