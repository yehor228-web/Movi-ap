from flask import Blueprint,render_template,redirect,request, jsonify
from flask_login import login_required

users = Blueprint("users", __name__, static_url_path="/static",template_folder="../templates",static_folder="../static")


@users.route("/movies/favorite/<movie_id>", methods=["GET", "POST"])
@login_required
def toggle_favorite_movie(movie_id):
    from flask_login import current_user
    from users.models import FavoriteMovies
    from app.extensions import db
    favorite_movies=FavoriteMovies.query.filter_by(movie_id=movie_id,user=current_user).first()
    if favorite_movies:
        db.session.delete(favorite_movies)
        db.session.commit()

        movies = current_user.favorite_movies
        print(movies)
        return'delected'
    fav_movie = FavoriteMovies(movie_id=movie_id, user=current_user)

    print(fav_movie)
    db.session.add(fav_movie)
    db.session.commit()

  

    return "saved"

@users.route('/register',methods=['Get','Post'])
def register():
    from flask import request,flash
    from app.extensions import db
    from users.models import User

    if request.method =="POST":
        username=request.form.get('username','')
        email=request.form.get('email','')
        password=request.form.get('password','')

        error=False

        user_exists=User.query.filter_by(email=email).first() is not None 
        if user_exists:
            flash  ('User already exists', "error"  )
            error=True
        
        if  len (password)<4:
            flash  ('password should contains minimum 4 characters',"error"   )
            error=True
        if not error:
            
            user=User(username=username,email=email,password=password)
            
            db.session.add(user)
            db.session.commit()

    return render_template('register.html')



@users.route('/login',methods=['Get','Post'])
def login():
    from flask import request,flash,redirect
    from flask_login import login_user
    from .models import User
    if request.method =="POST":
        email=request.form.get('email','')
        password=request.form.get('password','')

        error=False

        user=User.query.filter_by(email=email).first() 
        if  not user:
            flash  ('User with  this email not exists!Check your email and try again!', "error"  )
           
        elif  password != user.password:
            flash  ('Ivalid password ',"error"   )
            
        else:
            login_user(user)
            return redirect("/")
           

    return render_template('register.html')


@users.route("/logout")
@login_required
def logout():
    from flask_login import logout_user
    logout_user()
    return redirect("/")






@users.route("/profile")
@login_required
def profile():
    from flask_login import current_user
    from data import get_movies_details
    favorite_movies=[get_movies_details(movie.movie_id) for movie in current_user.favorite_movies]
    print(favorite_movies)
    return render_template('profile.html',favorite_movies=favorite_movies)