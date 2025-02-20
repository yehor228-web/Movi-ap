from flask import render_template,Blueprint,request,flash
from flask_login  import current_user,login_required
from data import get_toprated_movies,get_popular_movies,search_movies

core= Blueprint("core", __name__, static_url_path="/static",template_folder="../templates",static_folder="../static")
@core.route('/')
@core.route('/home')
def home():   
    popular =get_popular_movies() 
    top = get_toprated_movies()
    if current_user.is_authenticated:
        favorite_movies=[ movie.movie_id for movie in current_user.favorite_movies]
    else:
        favorite_movies=[]
        
    return render_template("index.html", popular_movies=popular, toprated_movies=top, favorite_movies=favorite_movies)

@core.route('/movies/toprated')
def top_rated_movies():
    from flask import request
    page=int(request.args.get('page', 1)) 
    movies=get_toprated_movies(page)

    page_start_index=max(page-4,1)
    page_end_index=page_start_index+10
    if current_user.is_authenticated :
        favorite_movies=[movie.movie_id for movie in current_user.favorite_movies]
    else:
        favorite_movies=[]
    return render_template('movie_list.html',movies=movies,page=page, page_start_index=page_start_index,page_end_index=page_end_index,favorite_movies=favorite_movies )


@core.route('/movies/popular')
def popular_movies():
    from flask import request
    page=int(request.args.get('page', 1)) 
    movies=get_popular_movies(page)
    page_start_index=max(page-4,1)
    page_end_index=page_start_index+10
    if current_user.is_authenticated :
        favorite_movies=[movie.movie_id for movie in current_user.favorite_movies]
    else:
        favorite_movies=[]
    return render_template('movie_list.html',movies=movies, page=page,page_start_index=page_start_index,page_end_index=page_end_index,favorite_movies=favorite_movies  )




@core.route('/movies/<movie_id>',methods=['GET','POST'])
def movie_detalis(movie_id):
    from data import get_movies_details,get_movies_images,get_movies_recommendations,get_movies_videos
    from users.models import Comment
    from flask_login import current_user
    from .extensions import db
    movie=get_movies_details(movie_id) 
    images=get_movies_images(movie_id)
    
    recommendations=get_movies_recommendations(movie_id) 

    videos=get_movies_videos(movie_id)
    
    videos=[item for item in videos if item.get('type')=="Trailer" and item.get('official')]

    if request.method=="POST":
        content=request.form.get("content")
        if  not content:
            flash  ('Comment content can not be empty! ',"error"   )     
        else:
            comment=Comment(movie_id=movie_id,content=content,user=current_user)
            db.session.add(comment)
            db.session.commit()
   

    comments=Comment.query.filter_by(movie_id=movie_id).all()
    print(comments)
    return render_template('details.html', movie=movie, images=images, recommendations=recommendations,video_key=videos[0]["key"],comments=comments)

@core.route("/comment/<int:comment_id>/delete", methods=["POST"])
@login_required
def delete_comment(comment_id):
    from users.models import Comment
    from .extensions import db
    from flask import jsonify

    comment = Comment.query.get_or_404(comment_id)

    if current_user.id == comment.user_id:
        db.session.delete(comment)
        db.session.commit()
        return jsonify({"status": "success"}), 200
    else:
        return (
            jsonify(
                {
                    "status": "error",
                    "message": "This comment can be deleted only by it's author!",
                }
            ),
            400,
        )
@core.route("/movies/search")
def search():
    page = int(request.args.get("page", 1))
    query = request.args.get("query", "")
    movies = search_movies(query,page )
    
   
    page_start_index = max(page - 4, 1)
    page_end_index = page_start_index + 10


    return render_template(
        "movie_list.html",
        movies=movies,
        page=page,
        page_start_index=page_start_index,
        page_end_index=page_end_index,
    )