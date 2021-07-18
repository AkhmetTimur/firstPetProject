from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField,DateField
from wtforms.validators import DataRequired

class WeightForm(FlaskForm):
    weight_date = DateField('Date (Year-month-day)', validators=[DataRequired()])
    weight = TextField('Weight', validators=[DataRequired()])
    submit = SubmitField('Add')
    