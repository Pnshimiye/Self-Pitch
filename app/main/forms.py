 

# # class ReviewForm(FlaskForm):

# #     title = StringField('Review title',validators=[Required()])
# #     review = TextAreaField('Movie review', validators=[Required()])
# #     submit = SubmitField('Submit')

    
# class UpdateProfile(FlaskForm):
#     pitch = TextAreaField('Pitch for yourself',validators = [Required()])
#     submit = SubmitField('Submit')

from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    narration = StringField('Pitch Narration',validators=[Required()])
    # review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')