from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CategoryForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=1, max=120)])
    submit = SubmitField("Save")
