from flask_wtf import  FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField,DateField
from wtforms.validators import Required


class BookingForm(FlaskForm):
    type=StringField('Type', validators=[Required()])
    company_choice=SelectField('Company name',choices=[('Tembera URwanda','Tembera URwanda'),('Kigali Safari','Kigali Safari'),('Virunga','Virunga')], validators=[Required()])
    # date=DateField('Your date',format='%m/%d/%y')
    submit=SubmitField('Book now')

class CommentForm(FlaskForm):
    comment=TextAreaField('Leave a comment',validators=[Required()])
    submit=SubmitField('Comment')