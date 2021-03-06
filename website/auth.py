from flask import Blueprint ,render_template ,request , flash ,redirect ,url_for
from  .models import Note , User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user , logout_user , login_required , current_user


auth = Blueprint('auth' , __name__)

@auth.route('/login' , methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password , password):
                flash('Logged in successfully' ,category='success')

                # for remembering the logged in user
                login_user(user , remember=True)
                return redirect(url_for('views.home'))


            else:
                flash('Incorrect password , try again' ,category= 'error')
        else:
            flash("Email doesn't exist" , category='error')



    return render_template("login.html" , user = current_user)


# the logout route cant be used unless the user is logged in
@auth.route('/logout')
@login_required
def logout():
    # for logging out user
    logout_user()
    flash('Logout Successfull' , category='success')
    return redirect(url_for('auth.login'))
    



@auth.route('/signup' , methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email = email).first()
        if user:
            flash('Email already exist' ,category='error')
        elif len(email) < 4 :
            flash('Invalid Email' , category='error')
        elif len(firstname) < 2:
            flash('First name must be greater then 1 character' , category='error')
        elif len(lastname) < 2:
            flash('Last name must be greater then 1 character' , category='error')
        elif password1!= password2:
            flash("Passwords don't match" ,category='error')
        elif len(password1) < 8:
            flash('Password must be at least 8 characters long' , category='error')
        else:
            # add user to data base
            
            new_user = User(email=email , password = generate_password_hash(password1 , method='sha256') , firstname = firstname , lastname = lastname)
            # for adding the new_user to the database
            db.session.add(new_user)
            db.session.commit()
            
            flash('Account Created' , category='success')
            print(request.form)
            # for remembering the logged in user
            login_user(new_user , remember=True)

            return redirect(url_for('views.home'))
            

    return render_template("signup.html" , user = current_user)

