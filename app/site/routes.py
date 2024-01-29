from flask import Blueprint, render_template
from forms import PostCar

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile' , methods = ['GET', 'POST'])
def profile():
    form = PostCar
    return render_template('car_form.html', title = 'New_Car', form=form)