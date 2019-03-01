# from app.models import Pitch,Comment
# from app import db 
# import unittest


# def setUp(self):
#         self.pitch_id = Pitch(id= 1)
#         self.new_comment = Comment(comment_comment="talk about that" )
# def tearDown(self):
#         comment.query.delete()
#         pitch.query.delete()

# def test_check_instance_variables(self):
#         self.assertEquals(self.new_comment.pitch_id,1)
#         self.assertEquals(self.new_comment.comment ='yeah yeah')        
 


# def test_save_comment(self):
#         self.new_comment.save_comment()
#         self.assertTrue(len(Comment.query.all())>0)
  
  
  
# def test_get_comments(self):

#         self.new_comment.save_comment()
#         got_comments = Comment.get_comments(12)
#         self.assertTrue(got_comments)