# from app.models import Pitch,User
# from app import db 
# import unittest


# def setUp(self):
#         self.user_pauline = User(username = 'Pauline')
#         self.new_pitch = Pitch(pitch_teaser="I am cool",pitch='only am tired',user = self.user_James )
# def tearDown(self):
#         Pitch.query.delete()
#         User.query.delete()

# def test_check_instance_variables(self):
#         self.assertEquals(self.new_pitch.user_id,1)
#         self.assertEquals(self.new_pitch.pitch_teaser,'I am cool')        
#         self.assertEquals(self.new_pitch.pitch_pitch,'This movie is the best thing since sliced bread')
#         self.assertEquals(self.new_pitch.user,self.user_James)


# def test_save_pitch(self):
#         self.new_pitch.save_pitch()
#         self.assertTrue(len(Pitch.query.all())>0)

# def test_get_pitches_by_id(self):

#         self.new_pitch.save_pitch()
#         got_pitches = Pitch.get_pitches(145)
#         self.assertTrue(len(got_pitches) == 1)