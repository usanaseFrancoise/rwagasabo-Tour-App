from flask import render_template,request,redirect,url_for
from . import main
from .forms import BookingForm,CommentForm
from ..models import Booking,User,Comment
# from flask_googlemaps import GoogleMaps
# from flask_googlemaps import Map


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    booking=Booking.query.all()

    
    return render_template('index.html',booking=booking)


@main.route('/new_book/',methods=['GET','POST'])
# @login_required
def new_book():

    virunga=Booking.query.filter_by(name='Virunga').all()
    safari=Booking.query.filter_by(name='Safari').all()
    tembera=Booking.query.filter_by(name='Tembera').all() 
    booking=Booking.query.all()
    form=BookingForm()
    if form.validate_on_submit():
        types=form.types.data
        # date=form.date.data
        name=form.name.data
        # user_id=current_user
        # company_id=current_company
        new_booking_object=Booking(types=types,name=name)
        new_booking_object.save_booking()
        return redirect(url_for('main.index'))
    return render_template('new_book.html',form=form,booking=booking,tembera=tembera,safari=safari,virunga=virunga)



@main.route('/comment/',methods=['GET','POST'])
# @login_required
def comment():
    form=CommentForm()
    # user=User.query.get().first()
    # all_comments=Comment.query.filter_by(user_id=user.id).all()
    if form.validate_on_submit():
        comment=form.comment.data
        user_id=user_id
        # user_id=current_user._get_current_object().id
        new_comment=Comment(comment=comment)
        new_comment.save_comment() 
        return redirect(url_for('.comment'))
    return render_template('comment.html',form=form)






# app = Flask(__name__, template_folder=".")
# GoogleMaps(app)

# @app.route("/")
# def mapview():
#     # creating a map in the view
#     mymap = Map(
#         identifier="view-side",
#         lat=37.4419,
#         lng=-122.1419,
#         markers=[(37.4419, -122.1419)]
#     )
#     sndmap = Map(
#         identifier="sndmap",
#         lat=37.4419,
#         lng=-122.1419,
#         markers=[
#           {
#              'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
#              'lat': 37.4419,
#              'lng': -122.1419,
#              'infobox': "<b>Hello World</b>"
#           },
#           {
#              'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
#              'lat': 37.4300,
#              'lng': -122.1400,
#              'infobox': "<b>Hello World from other place</b>"
#           }
#         ]
#     )
#     return render_template('example.html', mymap=mymap, sndmap=sndmap)