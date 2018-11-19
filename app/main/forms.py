from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField
from wtforms.validators import Required
from wtforms import ValidationError


class PitchForm(FlaskForm):
    content = TextAreaField("Your Pitch ?",validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    description = TextAreaField('Add comment',validators=[Required()])
    submit = SubmitField()

class UpdateProfile(FlaskForm):
    bio = TextAreaField('About You.',validators = [Required()])
    submit = SubmitField('Submit')
