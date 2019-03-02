

from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    teaser = StringField('Pitch Teaser',validators=[Required()])
    pitch = TextAreaField('Whole Pitch', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment =  StringField('comment',validators=[Required()])
    submit = SubmitField('Submit')

