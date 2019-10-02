from flask_wtf import  FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField,DateField
from wtforms.validators import Required



class BookingForm(FlaskForm):
    types=StringField('Type', validators=[Required()])
    name=SelectField('Company name',choices=[('Tembera ','Tembera '),('Safari',' Safari'),('Virunga','Virunga')], validators=[Required()])
    # date=DateField('Your date',format='%m/%d/%y')
    submit=SubmitField('Book now')

class CommentForm(FlaskForm):
    comment=TextAreaField('Leave a comment',validators=[Required()])
    submit=SubmitField('Comment')