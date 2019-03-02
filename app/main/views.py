from flask import render_template,redirect,url_for,abort
from . import main  
# from .forms import UpdateProfile
# from ..models import Review,User
# from ..models import User
from flask_login import login_required,current_user
from .. import db,photos    

from ..models import Pitch,User,Comment
from .forms import PitchForm,CommentForm



@main.route('/')
def index():
    """ View root page function that returns index page
    """
    all_pitches = Pitch.get_pitches()

    title = 'Home- Welcome'
    return render_template('index.html', title = title,all_pitches=all_pitches )



@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
  

    if form.validate_on_submit():    
        teaser = form.teaser.data
        pitch = form.pitch.data
        new_pitch = Pitch(user_id=current_user.id,teaser=teaser, pitch=pitch)
        new_pitch.save_pitch()
        return redirect(url_for('.index',pitch = pitch ))

   
    return render_template('new_pitch.html', pitch_form=form)


@main.route('/pitches')
def diplay_pitch():
    all_pitches = Pitch.get_pitches()
    print(all_pitches)
    return render_template("pitches.html",all_pitches=all_pitches )


@main.route('/comments/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()  
    pitch=Pitch.query.filter_by(id=id).first()

    if form.validate_on_submit():
        comment = form.comment.data
    
        new_comment = Comment(user_id=current_user.id,pitch_id=pitch.id,comment=comment)
        new_comment.save_comment()
        return redirect(url_for('main.index',comment=comment))

    return render_template('comments.html', comment_form=form)


 





 








    

 

    

