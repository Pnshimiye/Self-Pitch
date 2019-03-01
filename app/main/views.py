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
    # Pitch = pitch.Pitch
    # movie = get_movie(id)

    if form.validate_on_submit():
        # title = form.title.data
        teaser = form.teaser.data
        pitch = form.pitch.data
        new_pitch = Pitch(user_id=current_user.id,teaser=teaser, pitch=pitch)
        new_pitch.save_pitch()
        return redirect(url_for('.index',pitch = pitch ))

    # username = f'{user.username} pitch'
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

    if form.validate_on_submit():
        comment = form.comment.data
       
        new_comment = Comment(user_id=current_user.id)
        new_comment.save_comment()
        return redirect(url_for('main.index',comment=comment))

    return render_template('comments.html', comment_form=form)


@main.route('/pitches/')
def diplay_comment(id):
    comment = Comment.get_comment()
    # print(all_pitches)
    return render_template("comments.html",comment=comment,pitch_id=pitch.id)



# @main.route('/user/<uname>/update',methods = ['GET','POST'])
# @login_required
# def update_profile(uname):
#     user = User.query.filter_by(username = uname).first()
#     if user is None:
#         abort(404)

#     form = UpdateProfile()
#     user.pitch = form.pitch.data
       

#     if form.validate_on_submit():
#         db.session.add(user)
#         db.session.commit()
       

    

#         return redirect(url_for('.profile',uname=user.username))

#     return render_template('profile/update.html',form =form)

# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))

# @main.route('/user/<uname>/update/pitcf',methods= ['POST'])
# @login_required
# def update_pitch(uname):
#     user = User.query.filter_by(username = uname).first()
#     if pitch:
#         # filename = photos.save(request.files['photo'])
#         # path = f'photos/{filename}'
#         # user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))

# @main.route('/')
# def index():
#     """ View root page function that returns index page
#     """
     

#     title = 'Home- Welcome'
#     return render_template('index.html', title = title, )









    

 

    

