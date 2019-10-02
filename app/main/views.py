from flask import render_template,request,redirect,url_for
from . import main
from .forms import BookingForm
from ..models import Booking
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''


    
    return render_template('index.html')


@main.route('/new_book/',methods=['GET','POST'])
# @login_required
def new_book():
    form=BookingForm()
    if form.validate_on_submit():
        type=form.type.data
        # date=form.date.data
        company=form.company_choice.data
        # user_id=current_user
        # company_id=current_company
        new_booking_object=Booking(type=type,company=company)
        new_booking_object.save_p()
        return redirect(url_for('main.index'))
    return render_template('new_book.html',form=form)