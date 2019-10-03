import unittest
from app.models import User, Location
from flask_login import current_user
from app import db

class TestLooking(unittest.TestCase):
    def setUp(self):
        
        self.user1 = User(username = 'clarisse', password="123", email = "klaryc4@gmail.com")
        self.new_location = Location(name = 'Akagera', description ='national park',user_id = '123')
        
    def test_init(self):
        '''
        test case to test if the object is initialized properly
        '''
        self.assertEquals(self.new_location.name, 'Akagera')
        self.assertEquals(self.new_location.description, 'national park')
        self.assertEquals(self.new_location.user_id, '123')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_location, Location))   
        
        
        
