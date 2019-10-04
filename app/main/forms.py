
from wtforms.validators import Required, Email, EqualTo
from flask_wtf import  FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField,DateTimeField, PasswordField,BooleanField, ValidationError
from flask_wtf.file import FileField, FileRequired,DataRequired
from wtforms.validators import Required
from werkzeug.utils import secure_filename


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class BookingForm(FlaskForm):
   types=StringField('Type', validators=[Required()])
   name=SelectField('Company name',choices=[('Tembera ','Tembera '),('Safari',' Safari'),('Virunga','Virunga')], validators=[Required()])
   loc_name=SelectField('location name',choices=[('Akagera park ','Akagera park '),('Volcanoes park',' Volcanoes park'),('Nyungwe park','Nyungwe park')], validators=[Required()])
   start_date = DateTimeField("Start date",format='%d/%m/%Y',validators=[Required()] )
   submit=SubmitField('Book now')
class CommentForm(FlaskForm):
   comment=TextAreaField('Leave a comment',validators=[Required()])
   submit=SubmitField('Comment')
class LocationForm(FlaskForm):
   name=StringField('Location Name', validators=[Required()])
   description=StringField('Description', validators=[Required()])
   image = FileField(validators=[FileRequired()])
   submit=SubmitField('Submit')