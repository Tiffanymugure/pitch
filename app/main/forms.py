from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField, RadioField
from wtforms.validators import Required
from wtforms import ValidationError


class PitchForm(FlaskForm):
    content = TextAreaField("Your Pitch ?",validators=[Required()])
    category = RadioField('PitchListing', choices = [('Business', 'Business'), ('comedy', 'comedy'), ('Entertainment', 'Entertainment'),('Politics', 'Politics')])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    description = TextAreaField('Add comment',validators=[Required()])
    submit = SubmitField()

class UpdateProfile(FlaskForm):
    bio = TextAreaField('About You.',validators = [Required()])
    submit = SubmitField('Submit')

class ListingForm(FlaskForm):
    add = TextAreaField('Add Listing.',validators= [Required()])
    submit = SubmitField('Submit')