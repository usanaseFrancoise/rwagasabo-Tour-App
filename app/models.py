from flask_login import UserMixin
from . import login_manager
from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin, db.Model):
    __tablename__='users'
    
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    # password_hash = db.Column(db.String(255))
    password_secure = db.Column(db.String(255))
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)

            

    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

            
    
    def __repr__(self):
        return f'User {self.username}'