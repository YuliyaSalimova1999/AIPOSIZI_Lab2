from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from .models import Language, Genre

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    genre = SelectField('Genre', choices=[(genre.genre, genre.genre) for genre in Genre.query.all()])
    lang = SelectField('Languages', choices=[(lang.lang, lang.lang) for lang in Language.query.all()])
    summary = TextAreaField('Summary')
    submit = SubmitField()


class AuthorForm(FlaskForm):
    name = StringField('Author', validators=[DataRequired()])
    date_of_birth = StringField('Date of birth')
    date_of_death = StringField('Date of death')
    submit = SubmitField()


class LanguageForm(FlaskForm):
    lang = StringField('Language')
    submit = SubmitField()


class GenreForm(FlaskForm):
    genre = StringField('Genre')
    submit = SubmitField()