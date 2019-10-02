from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField, SubmitField, ValidationError, TextAreaField
from wtforms.validators import Required, Email, EqualTo

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')