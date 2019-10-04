from flask import render_template,request,redirect,url_for, abort
from . import main
from ..models import User,Booking,Comment,Location
from .forms import UpdateProfile,CommentForm,LocationForm,BookingForm
from .. import db, photos
from flask_login import login_required, current_user
from ..email import mail_message

# @main.route('/')
# def index():
#     '''
#     View root page function that returns the index page and its data
#     '''

    
#     return render_template('index.html')
@main.route('/')
def index():
   '''
   View root page function that returns the index page and its data
   '''
   booking=Booking.query.all()
   location=Location.query.all()
   form=CommentForm()
   return render_template('index.html',booking=booking,form=form)
#    -----------------------------
@main.route('/about')
def About():
    '''
    View root page function that returns the index page and its data
    '''

    
    return render_template('about.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

#--------booking--------- 
@main.route('/new_book/',methods=['GET','POST'])
@login_required
def new_book():
   user=User.query.filter_by(username =current_user.username).first()
   virunga=Booking.query.filter_by(name='Virunga').all()
   safari=Booking.query.filter_by(name='Safari').all()
   tembera=Booking.query.filter_by(name='Tembera').all()
   akagera_park=Booking.query.filter_by(loc_name='Akagera park').all()
   volcano=Booking.query.filter_by(loc_name='Volcano park').all()
   Nyungwe=Booking.query.filter_by(loc_name='Nyungwe park').all()
   booking=Booking.query.all()
   form=BookingForm()
   if form.validate_on_submit():
       types=form.types.data
       name=form.name.data
       loc_name=form.loc_name.data
       start_date=form.start_date.data
       new_booking_object=Booking(types=types,name=name,loc_name=loc_name,start_date=start_date)
       new_booking_object.save_booking()
       mail_message("Welcome to Rwagasabo Tour","email/booking",user.email,user=user)
       return redirect(url_for('main.index'))
       flash('successfully booked')
   return render_template('new_book.html',form=form,booking=booking,tembera=tembera,safari=safari,virunga=virunga,akagera_park=akagera_park,volcano=volcano,Nyungwe=Nyungwe)

#  -------Comment---------
@main.route('/comment/',methods=['GET','POST'])
# @login_required
def comment():
   form=CommentForm()
   all_comments=Comment.query.all()
   if form.validate_on_submit():
       comment=form.comment.data
       new_comment=Comment(comment=comment)
       new_comment.save_comment()
   return render_template('comment.html',form=form,all_comments=all_comments)

#   -----Suggestion------
@main.route('/location/add/pic/',methods=['POST','GET'])
# @login_required
def add_pic():
   location=Location.query.all()
   form=LocationForm()
   if form.validate_on_submit():
       name=form.name.data
       description=form.description.data
       filename=photos.save(form.image.data)
       path=f'photos/{filename}'
       new_location=Location(description=description,name=name,picture_path=path)
       new_location.save_location()
       return redirect(url_for('main.locatn'))
   return render_template('location/location.html',form=form)

@main.route('/location/',methods=['POST','GET'])
def locatn():
   location=Location.query.all()
#    user=User.query.filter_by(username =current_user.username).first()
   form=LocationForm()
   if form.validate_on_submit():
       name=form.name.data
       description=form.description.data
       filename=photos.save(form.image.data)
       path=f'photos/{filename}'
       new_location=Location(description=description,name=name,picture_path=path)
       new_location.save_location()
       return redirect(url_for('main.locatn',description=description,name=name,picture_path=path))
   return render_template('location/location.html',form=form,location=location)