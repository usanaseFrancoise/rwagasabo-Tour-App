import unittest
from app.models import User, Comment
from flask_login import current_user
from app import db

class TestBooking(unittest.TestCase):
    def setUp(self):
        
        self.user1 = User(username = 'clarisse', password="123", email = "klaryc4@gmail.com")
        self.new_comment = Comment(comment = 'trip', user_id = '123')
        
    def test_init(self):
        '''
        test case to test if the object is initialized properly
        '''
        self.assertEquals(self.new_comment.comment, 'trip')
        self.assertNotEquals(self.new_comment.id, '123')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))    
        
                