from .import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager



 


# class Review:

#     all_reviews = []

#     def __init__(self,movie_id,title,imageurl,review):
#         self.movie_id = movie_id
#         self.title = title
#         self.imageurl = imageurl
#         self.review = review


#     def save_review(self):
#         Review.all_reviews.append(self)


#     @classmethod
#     def clear_reviews(cls):
#         Review.all_reviews.clear()

#     @classmethod
#     def get_reviews(cls,id):

#         response = []

#         for review in cls.all_reviews:
#             if review.movie_id == id:
#                 response.append(review)

#         return response


class User(UserMixin,db.Model):
        __tablename__ = 'users'
        id = db.Column(db.Integer,primary_key = True)
        username = db.Column(db.String(255),index = True)
        email = db.Column(db.String(255),unique = True,index = True)
        pitch = db.relationship('Pitch',backref = 'user',lazy="dynamic")
        # password_hash = db.Column(db.String(255))        
        # bio = db.Column(db.String(255))
        profile_pic_path = db.Column(db.String())
        pass_secure = db.Column(db.String(255))

        

        def is_authenticated(self):
            return True

        def is_active(self):
            return True

        def is_anonymous(self):
            return False

        def get_id(self):
            return self.id

        def __repr__(self):         
            return f'User {self.username}'

       

        @property
        def password(self):
            raise AttributeError('You cannot read the password attribute')

        @password.setter
        def password(self, password):
            self.pass_secure = generate_password_hash(password)


        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))



        def verify_password(self,password):
            return check_password_hash(self.pass_secure, password)



class Pitch(db.Model):
    __tablename__ ='pitches'

    # all_pitches = []

    id = db.Column(db.Integer,primary_key = True)
    pitch= db.Column(db.String(400))
    teaser= db.Column(db.String(50))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))  

 


    def save_pitch(self):
        # Pitch.all_pitches.append(self)
        db.session.add(self)
        db.session.commit()


    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

    @classmethod
    def get_pitches(id):

        pitches= Pitch.query.all()
        # response = []

        # for pitch in cls.all_pitches:
        #     if pitch.user_username == username:
        #         response.append(pitch)

        return pitches




class Comment(db.Model):
    __tablename__ ='comments'

    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String(400))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id= db.Column(db.Integer,db.ForeignKey('pitches.id'))







