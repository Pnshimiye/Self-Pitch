from flask import render_template,redirect,url_for,abort
from . import main  
# from .forms import UpdateProfile
# from ..models import Review,User
# from ..models import User
from flask_login import login_required,current_user
from .. import db,photos    

from ..models import Pitch,User
from .forms import PitchForm



@main.route('/')
def index():
    """ View root page function that returns index page
    """


    title = 'Home- Welcome'
    return render_template('index.html', title = title)

# @main.route('/movies/<int:id>')
# def movies(movie_id):

#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#     return render_template('movie.html',id = movie_id)

# @main.route('/user/review/new/<int:id>', methods = ['GET','POST'])
# def new_review(id):
#     form = ReviewForm()
#     movie = get_movie(id)

#     if form.validate_on_submit():
#         title = form.title.data
#         review = form.review.data
#         new_review = Review(movie.id,title,movie.poster,review)
#         new_review.save_review()
#         return redirect(url_for('movie',id = movie.id ))

#     title = f'{movie.title} review'
#     return render_template('new_review.html',title = title, review_form=form, movie=movie)

 

 

    
# @main.route('/search/<movie_name>')
# def search(movie_name):
#     '''
#     View function to display the search results
#     '''
#     movie_name_list = movie_name.split(" ")
#     movie_name_format = "+".join(movie_name_list)
#     searched_movies = search_movie(movie_name_format)
#     title = f'search results for {movie_name}'
#     return render_template('search.html',movies = searched_movies)


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
    return render_template("pitches.html",all_pitches=all_pitches)


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









    

 

    

