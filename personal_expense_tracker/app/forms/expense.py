from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Optional


class ExpenseForm(FlaskForm):
    amount = DecimalField("Amount", places=2, validators=[DataRequired()])
    description = StringField("Description", validators=[Optional()])
    date = DateField("Date", validators=[DataRequired()])
    category_id = SelectField("Category", coerce=int, validators=[Optional()])
    submit = SubmitField("Add Expense")
