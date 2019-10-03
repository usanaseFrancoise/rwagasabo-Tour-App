import unittest
from app.models import User, Booking
from flask_login import current_user
from app import db

class TestBooking(unittest.TestCase):
    def setUp(self):
        
        self.user1 = User(username = 'clarisse', password="123", email = "klaryc4@gmail.com")
        self.new_booking = Booking(types = 'trip', name='akagera', user_id = '123')
        
    def test_init(self):
        '''
        test case to test if the object is initialized properly
        '''
        self.assertEquals(self.new_booking.types, 'trip')
        self.assertEquals(self.new_booking.name, 'akagera')
        self.assertNotEquals(self.new_booking.id, '123')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_booking, Booking))    
        
                