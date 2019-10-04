# from flask_login import UserMixin
# from . import login_manager
# from . import db
# from werkzeug.security import generate_password_hash,check_password_hash

# class User(UserMixin, db.Model):
#     __tablename__='users'
    
#     id = db.Column(db.Integer, primary_key= True)
#     username = db.Column(db.String(255))
#     email = db.Column(db.String(255), unique = True, index = True)
#     # password_hash = db.Column(db.String(255))
#     password_secure = db.Column(db.String(255))
    
#     @login_manager.user_loader
#     def load_user(user_id):
#         return User.query.get(int(user_id))
    
#     @property
#     def password(self):
#         raise AttributeError('You cannot read the password attribute')

#     @password.setter
#     def password(self, password):
#         self.password_secure = generate_password_hash(password)

            

#     def verify_password(self,password):
#         return check_password_hash(self.password_secure,password)

            
    
#     def __repr__(self):
#         return f'User {self.username}'



from .import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
import calendar
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):

   return User.query.get(int(user_id))

class User(UserMixin,db.Model):
   __tablename__='users'
   id=db.Column(db.Integer,primary_key=True)
   username=db.Column(db.String(255),unique=True)
   email=db.Column(db.String(255),unique=True,index=True)
   password_secure =db.Column(db.String(255))
   booking=db.relationship('Booking',backref='users',lazy="dynamic")
   comment=db.relationship('Comment',backref='users',lazy="dynamic")
   @property
   def password(self):
       raise AttributeError('you cannot read the password attribute')
   @password.setter
   def password(self,password):
       self.password_secure=generate_password_hash(password)
   def verify_password(self, password):
       return check_password_hash(self.password_secure,password)
   def save_user(self):
       db.session.add(self)
       db.session.commit()
   def __repr__(self):
       return f'User{self.username}'

class Comment(db.Model):
   __tablename__='comments'
   id=db.Column(db.Integer,primary_key=True)
   comment=db.Column(db.Text())
   user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
   # location_id=db.Column(db.Integer,db.ForeignKey('locations.id'))
   def save_comment(self):
       db.session.add(self)
       db.session.commit()
   @classmethod
   def get_comments(cls,user_id):
       comments=Comment.query.filter_by(user_id=id).all()
       return comments
   def __repr__(self):
       return f'comment{self.comment}'

class Booking(db.Model):
   __tablename__='bookings'
   id=db.Column(db.Integer,primary_key=True)
   types=db.Column(db.String(255),nullable = False)
   name=db.Column(db.String(255),nullable = False)
   loc_name=db.Column(db.String(255),nullable = False)
   start_date=db.Column(db.DateTime,default=datetime.utcnow)
   user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
   def save_booking(self):
       db.session.add(self)
       db.session.commit()
   def __repr__(self):
       return f'Booking{self.type}'

# class Location(db.Model):
#    __tablename__='locations'
#    id=db.Column(db.Integer,primary_key=True)
#    name=db.Column(db.String(255),nullable = False)
#    description=db.Column(db.String(255),nullable = False)
#    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
#    def save_location(self):
#        db.session.add(self)
#        db.session.commit()
#    def __repr__(self):
#        return f'Location{self.name}'


class Location(db.Model):
   __tablename__='locations'
   id=db.Column(db.Integer,primary_key=True)
   name=db.Column(db.String(255),nullable = False)
   description=db.Column(db.String(255),nullable = False)
   user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
   picture_path=db.Column(db.String(255))
   def save_location(self):
       db.session.add(self)
       db.session.commit()
   def __repr__(self):
       return f'Location{self.name}'