from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional


class BudgetForm(FlaskForm):
    month = IntegerField("Month", validators=[DataRequired(), NumberRange(min=1, max=12)])
    year = IntegerField("Year", validators=[DataRequired(), NumberRange(min=2000, max=2100)])
    amount = DecimalField("Amount", places=2, validators=[DataRequired()])
    category_id = SelectField("Category", coerce=int, validators=[Optional()])
    submit = SubmitField("Save Budget")
